import streamlit.components.v1 as components
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend", "build")

_st_component = components.declare_component(
    "streamlit_javascript", path=build_dir
)

def st_javascript(**kwargs):
    return _st_component(**kwargs)