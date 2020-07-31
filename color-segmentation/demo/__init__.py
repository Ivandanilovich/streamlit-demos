import os
import streamlit.components.v1 as components


_component_func = components.declare_component("demo", path='/demo')

def my_component(name, key=None):
    component_value = _component_func(name=name, key=key, default=0)
    return component_value
