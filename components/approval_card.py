import streamlit as st


def render_approval_card(approval):
    """Renders an approval card with contextual details."""
    with st.container():
        st.markdown(
            f"""
            <div style="border:1px solid rgba(255,255,255,0.08); border-left:4px solid #f59f00; border-radius:16px; padding:1rem; margin-bottom:0.8rem; background:rgba(255,255,255,0.03);">
                <strong>{approval['release_name']}</strong><br>
                <span style="color:#94a3b8;">{approval['service']}</span><br>
                <span>Requested by <b>{approval['requested_by']}</b> · {approval['requested_at']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(approval['notes'])
