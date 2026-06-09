import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from components.status_card import render_status_card
from services.gitlab_service import get_pipelines
from services.deployment_service import get_deployments, get_approvals
from services.nexus_service import get_artifacts
from services.jira_service import get_jira_status


def render_dashboard():
    """Renders the executive overview for the release control center."""
    pipelines = get_pipelines()
    deployments = get_deployments()
    approvals = get_approvals()
    artifacts = get_artifacts()
    jira_status = get_jira_status()

    total_pipelines = len(pipelines)
    successful_deployments = sum(1 for item in deployments if item["status"].lower() == "success")
    failed_deployments = sum(1 for item in deployments if item["status"].lower() == "warning")
    pending_approvals = len(approvals)

    st.markdown("## Executive Release Dashboard")
    st.caption("Financial-grade visibility for pipeline health, approvals, and releases")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_status_card("Total Pipelines", str(total_pipelines), "Across active release branches", "🔄", "#3b82f6")
    with col2:
        render_status_card("Successful Deployments", str(successful_deployments), "Validated release states", "✅", "#20c997")
    with col3:
        render_status_card("Failed Deployments", str(failed_deployments), "Attention required", "⚠️", "#f59f00")
    with col4:
        render_status_card("Pending Approvals", str(pending_approvals), "Awaiting release sign-off", "📝", "#ef4444")

    st.divider()

    col_left, col_right = st.columns([1.3, 0.9])
    with col_left:
        df = pd.DataFrame(pipelines)
        pie = px.pie(df, names="status", title="Pipeline health distribution", hole=0.45)
        pie.update_traces(marker=dict(colors=["#20c997", "#3b82f6", "#f59f00", "#ef4444"]))
        st.plotly_chart(pie, use_container_width=True)

    with col_right:
        release_df = pd.DataFrame(jira_status)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=release_df["environment"], y=[3, 4, 2, 1], name="Release readiness", marker_color="#3b82f6"))
        fig.update_layout(title="Environment readiness", margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Release summary")
    summary_cols = st.columns(3)
    with summary_cols[0]:
        st.info("📦 Latest artifact: Axiom SL Core Banking v24.06.1-001")
    with summary_cols[1]:
        st.info("🧪 QA validation: 94% pass rate")
    with summary_cols[2]:
        st.info("🔐 Compliance: Approved for production readiness")

    st.subheader("Recent activity")
    timeline = [
        "09:15 UTC — Approval requested for Payments Gateway release",
        "08:58 UTC — Nexus artifact promoted to UAT",
        "08:20 UTC — QA deployment completed successfully",
        "07:05 UTC — DEV deployment completed successfully",
    ]
    for entry in timeline:
        st.markdown(f"- {entry}")

    st.subheader("Artifact overview")
    artifact_df = pd.DataFrame(artifacts)
    st.dataframe(artifact_df[["name", "version", "created_at"]], use_container_width=True, hide_index=True)
