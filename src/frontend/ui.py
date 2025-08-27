"""UI components for the FastHTML-based FortiAgent frontend."""
from fasthtml.common import *


def header() -> Div:
    """Return the application header."""
    return Div(H1("FortiAgent"), cls="header")


def footer() -> Div:
    """Return the application footer."""
    return Div("AI-Powered Test Automation", cls="footer")
