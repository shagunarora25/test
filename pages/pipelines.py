import streamlit as st

from components.pipeline_table import render_pipeline_table
from services.gitlab_service import get_pipelines, trigger_pipeline, retry_pipeline


def render_pipelines():
    """Renders the GitLab pipeline management view."""
    pipelines = get_pipelines()

    st.markdown("## Pipeline Operations")
    st.caption("Trigger, retry, and inspect release pipelines with mock enterprise responses")

    action_col1, action_col2, action_col3 = st.columns(3)
    with action_col1:
        if st.button("▶ Trigger Pipeline", use_container_width=True):
            response = trigger_pipeline()
            st.success(response["message"])
    with action_col2:
        if st.button("↻ Retry Pipeline", use_container_width=True):
            response = retry_pipeline(pipelines[0]["pipeline_id"])
            st.warning(response["message"])
    with action_col3:
        if st.button("🔄 Refresh", use_container_width=True):
            st.cache_data.clear()
            st.info("Pipeline view refreshed.")

    st.divider()
    render_pipeline_table(pipelines)

    with st.expander("Pipeline health notes"):
        st.markdown("- Main branch is healthy with active deployment activity.")
        st.markdown("- Hotfix branch requires immediate review after the latest QA failure.")
