import streamlit as st

from services.nexus_service import get_artifacts, create_artifact, promote_artifact


def render_artifacts():
    """Displays Nexus artifacts and provides placeholder actions."""
    artifacts = get_artifacts()

    st.markdown("## Nexus Artifact Management")
    st.caption("Track release build outputs and future promotion workflows")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Create Artifact", use_container_width=True):
            response = create_artifact("axiom-sl-core-banking", "24.06.2")
            st.success(f"{response['status'].title()} — {response['name']} {response['version']}")
    with col2:
        if st.button("Promote Artifact", use_container_width=True):
            response = promote_artifact("axiom-sl-core-banking", "PROD")
            st.info(f"{response['status'].title()} — {response['name']} -> {response['target']}")

    st.divider()
    for artifact in artifacts:
        with st.container():
            st.markdown(
                f"""
                <div style="border:1px solid rgba(255,255,255,0.08); border-radius:16px; padding:1rem; margin-bottom:0.8rem; background:rgba(255,255,255,0.03);">
                    <strong>{artifact['name']}</strong><br>
                    <span>Version: {artifact['version']}</span><br>
                    <span>Created: {artifact['created_at']}</span><br>
                    <a href="{artifact['download_url']}" target="_blank">Download artifact</a>
                </div>
                """,
                unsafe_allow_html=True,
            )
