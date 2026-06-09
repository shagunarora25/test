import streamlit as st

from components.approval_card import render_approval_card
from services.deployment_service import get_approvals, approve_release, reject_release


def render_approvals():
    """Displays pending release approvals and mock actions."""
    approvals = get_approvals()
    st.markdown("## Release Approvals")
    st.caption("Centralized sign-off for high-impact banking releases")

    for approval in approvals:
        render_approval_card(approval)
        button_col1, button_col2 = st.columns(2)
        with button_col1:
            if st.button(f"Approve · {approval['release_name']}", key=f"approve-{approval['release_name']}", use_container_width=True):
                response = approve_release(approval['release_name'])
                st.success(f"{response['status'].title()} — {response['release_name']}")
        with button_col2:
            if st.button(f"Reject · {approval['release_name']}", key=f"reject-{approval['release_name']}", use_container_width=True):
                response = reject_release(approval['release_name'])
                st.error(f"{response['status'].title()} — {response['release_name']}")
        st.divider()
