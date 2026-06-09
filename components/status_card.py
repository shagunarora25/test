import streamlit as st
from streamlit_extras.stylable_container import stylable_container


def render_status_card(title, value, subtitle, icon, accent):
    """Renders a reusable outcome card with colorful accents."""
    with stylable_container(
        key=f"status-card-{title}",
        css_styles=f"""
        {{
            border: 1px solid rgba(255,255,255,0.08);
            border-left: 4px solid {accent};
            border-radius: 16px;
            padding: 1rem;
            background: rgba(255,255,255,0.03);
            margin-bottom: 0.6rem;
        }}
        """,
    ):
        st.markdown(f"### {icon} {title}")
        st.markdown(f"<h2 style='margin:0; color:{accent};'>{value}</h2>", unsafe_allow_html=True)
        st.caption(subtitle)
