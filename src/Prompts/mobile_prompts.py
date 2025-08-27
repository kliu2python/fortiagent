import json
import re
from typing import Dict, Any

from appium import webdriver

from src.Agents.mobile_agents import mobile_gherkin_agent, mobile_code_gen_agent
from src.Prompts.agno_prompts import extract_code_content
from src.Utilities.utils import extract_selectors_from_history, analyze_actions


def generate_mobile_gherkin_scenarios(manual_test_cases_markdown: str) -> str:
    """Generate Gherkin scenarios for mobile apps."""
    run_response = mobile_gherkin_agent.run(manual_test_cases_markdown)
    return extract_code_content(run_response.content)


def execute_mobile_steps(
    gherkin_steps: str,
    appium_server_url: str,
    desired_capabilities: Dict[str, Any],
) -> Dict[str, Any]:
    """Execute Gherkin steps on a mobile device using Appium.

    Returns a history dictionary similar to the browser agent containing
    action names and extracted content that can be used for code generation.
    """
    driver = webdriver.Remote(appium_server_url, desired_capabilities)
    history: Dict[str, Any] = {"action_names": [], "extracted_content": [], "urls": []}
    try:
        for raw_line in gherkin_steps.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or line.endswith(":"):
                continue
            history["action_names"].append(line)
            lower = line.lower()
            if "tap" in lower:
                match = re.search(r'"([^\"]+)"', line)
                if match:
                    element_id = match.group(1)
                    try:
                        el = driver.find_element("accessibility id", element_id)
                        el.click()
                        history["extracted_content"].append(f"Tapped element {element_id}")
                    except Exception as e:  # pragma: no cover - best effort
                        history["extracted_content"].append(
                            f"Error tapping element {element_id}: {e}"
                        )
            elif "enter" in lower or "type" in lower:
                # Expect pattern: enter "value" into "field"
                matches = re.findall(r'"([^\"]+)"', line)
                if len(matches) >= 2:
                    value, element_id = matches[:2]
                    try:
                        el = driver.find_element("accessibility id", element_id)
                        el.send_keys(value)
                        history["extracted_content"].append(
                            f"Entered {value} into {element_id}"
                        )
                    except Exception as e:  # pragma: no cover
                        history["extracted_content"].append(
                            f"Error entering text into {element_id}: {e}"
                        )
            elif "see" in lower or "should" in lower:
                match = re.search(r'"([^\"]+)"', line)
                if match:
                    element_id = match.group(1)
                    try:
                        driver.find_element("accessibility id", element_id)
                        history["extracted_content"].append(
                            f"Verified element {element_id} is visible"
                        )
                    except Exception as e:  # pragma: no cover
                        history["extracted_content"].append(
                            f"Verification failed for {element_id}: {e}"
                        )
        return history
    finally:
        driver.quit()


def generate_appium_pytest(gherkin_steps: str, history_data: Dict[str, Any]) -> str:
    """Generate a PyTest file using Appium based on executed mobile steps."""
    selectors = extract_selectors_from_history(history_data)
    actions = analyze_actions(history_data)

    code_file_prompt = f"""
    Generate Appium PyTest code based on the following:

    Gherkin Steps:
    ```gherkin
    {gherkin_steps}
    ```

    Agent Execution Details:
    - Element Selectors: {json.dumps(selectors, indent=2)}
    - Actions Performed: {json.dumps(actions, indent=2)}
    - Extracted Content: {json.dumps(history_data.get('extracted_content', []), indent=2)}
    """

    code_response = mobile_code_gen_agent.run(code_file_prompt)
    return extract_code_content(code_response.content)
