import streamlit as st
import sys, os

# Add the project root to Python path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from backend.main import *

from backend.main import *

title = st.title('Welecome to Super Shop')
div = st.divider()


