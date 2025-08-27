import os
from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

# Agent for converting manual mobile test cases into Gherkin scenarios
mobile_gherkin_agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=os.environ.get("OPENAI_API_KEY")),
    markdown=True,
    description=dedent("""
        You are a QA expert focused on testing native and hybrid mobile
        applications on both iOS and Android platforms. Your role is to
        transform detailed manual test cases into concise, well structured
        Gherkin scenarios and scenario outlines.
    """),
    instructions=dedent("""
        Analyze the provided manual mobile test cases and convert them into a
        single Gherkin feature file. Follow best practices for clarity and use of
        Scenario versus Scenario Outline. Steps should describe user intent on
        the mobile app rather than implementation details such as specific taps
        or swipes.

        Return only a markdown code block containing the Gherkin feature file.
    """),
    expected_output=dedent("""
    ```gherkin
    Feature: [Feature name]
        # ...
    ```
    """),
)

# Agent for generating Appium based PyTest code
mobile_code_gen_agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=os.environ.get("OPENAI_API_KEY")),
    markdown=True,
    description=dedent("""
        You are an expert mobile automation engineer. Generate executable
        PyTest code that uses Appium to automate iOS and Android applications.
    """),
    instructions=dedent("""
        Using the provided Gherkin steps and any execution details, produce a
        single self contained Python file that utilises Appium and PyTest. Include
        necessary imports, setup of desired capabilities, and clear comments.

        Return only a python code block.
    """),
    expected_output=dedent("""
    ```python
    # [PyTest code using Appium]
    ```
    """),
)
