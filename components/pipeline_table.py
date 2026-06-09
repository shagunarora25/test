import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder


def render_pipeline_table(pipelines):
    """Displays pipeline history using an interactive grid."""
    df = pd.DataFrame(pipelines)
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(enabled=True, paginationAutoPageSize=True)
    gb.configure_default_column(editable=False, resizable=True, filter=True)
    gb.configure_column("Pipeline ID", width=120)
    gb.configure_column("Branch", width=140)
    gb.configure_column("Status", width=140)
    gb.configure_column("Triggered By", width=140)
    gb.configure_column("Start Time", width=180)
    grid_options = gb.build()
    AgGrid(df, grid_options=grid_options, height=420, theme="balham", allow_unsafe_jscode=True)
