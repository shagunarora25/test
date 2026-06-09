import streamlit as st

from services.gitlab_service import get_pipeline_logs
from utils.constants import STATUS_COLORS


def render_logs():
    """Displays pipeline logs with search and severity-based color coding."""
    logs = get_pipeline_logs()
    st.markdown("## Pipeline Logs")
    st.caption("Structured log inspection for release diagnostics")

    search_term = st.text_input("Search logs")
    level_filter = st.selectbox("Filter by severity", ["All", "success", "warning", "error"])

    filtered_logs = logs
    if search_term:
        filtered_logs = [entry for entry in filtered_logs if search_term.lower() in entry["message"].lower()]
    if level_filter != "All":
        filtered_logs = [entry for entry in filtered_logs if entry["level"] == level_filter]

    for entry in filtered_logs:
        color = STATUS_COLORS.get(entry["level"], STATUS_COLORS["neutral"])
        with st.expander(f"{entry['id']} · {entry['timestamp']} · {entry['pipeline_id']}", expanded=False):
            st.markdown(
                f"<span style='color:{color}; font-weight:700;'>[{entry['level'].upper()}]</span> {entry['message']}",
                unsafe_allow_html=True,
            )
