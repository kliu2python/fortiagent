"""Minimal FastHTML application for FortiAgent."""
from fasthtml.common import *

from src.frontend.ui import header, footer

app, rt = fast_app()

@rt("/")
def home():
    """Render the FortiAgent landing page."""
    return Div(
        header(),
        P("Prompts to Automated Tests : QA Browser Automation using AI Agents"),
        footer(),
    )

if __name__ == "__main__":
    serve()
