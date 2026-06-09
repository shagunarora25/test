import streamlit as st
from streamlit_option_menu import option_menu

from components.navbar import render_navbar
from pages.dashboard import render_dashboard
from pages.pipelines import render_pipelines
from pages.logs import render_logs
from pages.artifacts import render_artifacts
from pages.approvals import render_approvals
from pages.deployments import render_deployments


st.set_page_config(page_title="Axiom SL Release Automation", page_icon="🏦", layout="wide")


if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "dark"


def apply_theme():
    """Injects custom CSS to create a polished banking dashboard look."""
    theme = st.session_state.theme_mode
    if theme == "dark":
        st.markdown(
            """
            <style>
            :root {
                color-scheme: dark;
            }
            .stApp {
                background: linear-gradient(135deg, #07111f 0%, #13253d 100%);
                color: #f3f7ff;
            }
            .block-container {
                padding-top: 1rem;
                padding-bottom: 2rem;
            }
            .stTabs [data-baseweb="tab-list"] {
                gap: 8px;
            }
            .stTabs [data-baseweb="tab"] {
                border-radius: 999px;
                padding: 8px 14px;
                background: rgba(255,255,255,0.06);
            }
            .st-emotion-cache-1r6slb0, .st-emotion-cache-1wmy9hl {
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 18px;
                background: rgba(6, 15, 26, 0.88);
                box-shadow: 0 10px 30px rgba(0,0,0,0.22);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            .stApp {
                background: linear-gradient(135deg, #f4f7fc 0%, #eef4ff 100%);
                color: #1b2433;
            }
            .block-container {
                padding-top: 1rem;
                padding-bottom: 2rem;
            }
            .stTabs [data-baseweb="tab-list"] {
                gap: 8px;
            }
            .stTabs [data-baseweb="tab"] {
                border-radius: 999px;
                padding: 8px 14px;
                background: rgba(255,255,255,0.8);
            }
            .st-emotion-cache-1r6slb0, .st-emotion-cache-1wmy9hl {
                border: 1px solid rgba(16, 24, 40, 0.08);
                border-radius: 18px;
                background: rgba(255,255,255,0.9);
                box-shadow: 0 10px 30px rgba(16,24,40,0.08);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )


apply_theme()
render_navbar()

pages = {
    "Overview": render_dashboard,
    "Pipelines": render_pipelines,
    "Logs": render_logs,
    "Artifacts": render_artifacts,
    "Approvals": render_approvals,
    "Deployments": render_deployments,
}

with st.sidebar:
    st.markdown("### Navigation")
    selected_page = option_menu(
        menu_title=None,
        options=list(pages.keys()),
        icons=["house", "cpu", "journal-text", "box-seam", "check2-circle", "rocket-takeoff"],
        default_index=0,
        orientation="vertical",
    )

    st.divider()
    st.toggle("🌙 Dark mode", value=st.session_state.theme_mode == "dark", key="theme_toggle")
    if st.session_state.theme_toggle:
        st.session_state.theme_mode = "dark"
    else:
        st.session_state.theme_mode = "light"

pages[selected_page]()
