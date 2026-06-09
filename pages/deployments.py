import streamlit as st
import pandas as pd
import plotly.express as px

from services.deployment_service import get_deployments, deploy_release
from utils.constants import ENVIRONMENT_ORDER


def render_deployments():
    """Shows deployment history and environment-level monitoring."""
    deployments = get_deployments()
    st.markdown("## Deployment Monitoring")
    st.caption("Track environment readiness and deployment outcomes")

    env_summary = {env: 0 for env in ENVIRONMENT_ORDER}
    for item in deployments:
        env_summary[item["environment"]] = 1

    env_cols = st.columns(4)
    for index, env in enumerate(ENVIRONMENT_ORDER):
        with env_cols[index]:
            status = deployments[index]["status"]
            color = "#20c997" if status == "Success" else "#f59f00" if status == "Warning" else "#3b82f6"
            st.markdown(
                f"""
                <div style="border:1px solid rgba(255,255,255,0.08); border-radius:16px; padding:1rem; background:linear-gradient(135deg, rgba(59,130,246,0.16), rgba(0,0,0,0.05)); margin-bottom:0.6rem;">
                    <h4>{env}</h4>
                    <div style="font-size:1.3rem; font-weight:700; color:{color};">{status}</div>
                    <div>Release {deployments[index]['release']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()
    if st.button("Deploy to PROD", use_container_width=True):
        response = deploy_release("PROD", "24.06.1")
        st.success(f"{response['status'].title()} — {response['environment']} deployment requested")

    deployment_df = pd.DataFrame(deployments)
    timeline = px.timeline(
        deployment_df,
        x_start="deployed_at",
        x_end="deployed_at",
        y="environment",
        color="status",
        title="Deployment timeline"
    )
    st.plotly_chart(timeline, use_container_width=True)

    st.subheader("Deployment history")
    st.dataframe(deployment_df[["environment", "status", "release", "deployed_at", "owner"]], use_container_width=True, hide_index=True)
