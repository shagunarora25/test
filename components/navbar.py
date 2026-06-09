import streamlit as st


def render_navbar():
    """Renders the main header with product branding and release context."""
    st.markdown(
        """
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <div>
                <h1 style="margin-bottom:0.2rem;">🏦 Axiom SL Release Automation</h1>
                <p style="margin:0; color:#7c8da9;">Enterprise CI/CD control center for banking releases</p>
            </div>
            <div style="padding:0.6rem 1rem; border-radius:999px; background:rgba(59,130,246,0.16); color:#7dd3fc; font-weight:600;">
                🚀 Release window: 14:30 UTC
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
