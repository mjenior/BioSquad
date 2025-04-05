
from biosquad.tools import *
from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace, function_tool

import pyaml
# TODO: 
# - Read agent system instruction definitions
# - Orchestration agent instructions



# --- WORKERS ------------------------------------------------------------------------------------------ #


# Project/Product Manager Agent
product_manager = Agent(
    name="Project/Product Manager Agent",
    instructions=manager_instructions,
    tools=[gather_requirements, create_roadmap],
)

# Task Master Agent
task_master = Agent(
    name="Task Master Agent",
    instructions=task_generator_instructions,
    tools=[plan_sprint]
)

# Backend Developer Agent
backend_developer = Agent(
    name="Backend Developer Agent",
    instructions=backend_instructions,
    tools=[design_system_architecture, implement_backend_functionality, extract_code_snippets, write_script]
)

# Frontend Developer Agent
frontend_developer = Agent(
    name="Frontend Developer Agent",
    instructions=frontend_instructions,
    tools=[implement_frontend_interface, extract_code_snippets, write_script]
)

architect_agent = Agent(
    name="Software Architect Agent",
    instructions=architect_instructions,
    tools=[design_system_architecture]
)


requester_agent = Agent(
    name="Project Summarizer Agent",
    instructions=requester_instructions)


project_summarizer_agent = Agent(
    name="Project Summarizer Agent",
    instructions=(
        "You are responsible for synthesizing and summarizing the outputs of project tasks "
        "into a coherent summary. Ensure all important aspects of the project are covered."
    )
)


# --- ORCHESTRATION ------------------------------------------------------------------------------------ #


# TODO: 
# - Biology orchestrator
# - Analysis orchestrator
# - Writing orchestrator

software_orchestrator = Agent(
    name="Orchestrator Agent",
    instructions=software_orchestrator_instructions,

    # TODO: handoffs

    tools=[
        product_manager.as_tool(
            tool_name="manage_project",
            tool_description="Coordinate high-level project goals and requirements."
        ),
        architect_agent.as_tool(
            tool_name="design_system_architecture",
            tool_description="Design the system architecture for the project."
        ),
        task_master.as_tool(
            tool_name="generate_tasks",
            tool_description="Generate tasks from user requirements."
        ),
        backend_developer.as_tool(
            tool_name="develop_backend",
            tool_description="Implement server-side functionality and design system architecture."
        ),
        frontend_developer.as_tool(
            tool_name="develop_frontend",
            tool_description="Implement and test UI and client-facing components."
        ),
    ],

    # TODO: input_guardrails

    # TODO: output_guardrails

)



# --- MANAGEMENT ------------------------------------------------------------------------------------ #





