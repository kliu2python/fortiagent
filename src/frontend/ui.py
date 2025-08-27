from pathlib import Path
import streamlit as st

CSS_PATH = Path(__file__).with_name("styles.css")

def set_page_config() -> None:
    """Configure basic page settings."""
    st.set_page_config(page_title="AI BROWSER AUTOMATION", layout="wide")

def load_css() -> None:
    """Load the CSS stylesheet for the Streamlit app."""
    if CSS_PATH.exists():
        css = CSS_PATH.read_text()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_header() -> None:
    """Render the application header."""
    st.markdown(
        """
        <div class="header">
            <h1>AI Browser Automation</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_footer() -> None:
    """Render the application footer."""
    st.markdown(
        '<div class="footer">AI-Powered Test Automation</div>',
        unsafe_allow_html=True,
    )
