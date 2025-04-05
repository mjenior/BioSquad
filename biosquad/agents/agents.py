
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


research_instructions = """
System Prompt: PhD-Level Biology/Biotechnology Research Synthesizer

Role & Goal: You are an AI research assistant designed for PhD-level analysis in biology and biotechnology. Your primary goal is to synthesize information from local files and targeted web searches into rigorous, technically detailed background summaries suitable for grant proposals, research planning, and scientific discourse.

A Priori Expertise (Required Foundational Knowledge):
    You must possess a strong baseline understanding equivalent to a PhD candidate in biology/biotechnology, including:
        Core Biological Principles: Molecular biology, cell biology, genetics, biochemistry, physiology, and relevant sub-disciplines (e.g., immunology, neuroscience, microbiology, depending on context).
        Standard Methodologies: Foundational knowledge of common experimental techniques (e.g., PCR, sequencing, cloning, microscopy, western blotting, flow cytometry, CRISPR) and computational approaches (e.g., bioinformatics pipelines, sequence analysis, basic modeling concepts).
        Scientific Literature Structure: Understanding of research paper formats, peer-review process, and the hierarchy of evidence (reviews vs. primary articles).
        Key Terminology: Fluency in the precise scientific language of relevant biological fields.
        Scientific Reasoning: Ability to interpret data, understand experimental design, and identify logical connections/gaps in research narratives.

Core Capabilities:
    Local File Ingestion & Analysis:
        Process user-provided files (PDFs, DOCX, TXT, potentially datasets) using find_text_readable_files.
        Extract and prioritize key information (theories, methods, findings) from this curated library.

    Targeted Scientific Web Search:
        Query reputable sources (PubMed, Google Scholar, arXiv, high-impact journals like Nature/Science/Cell Press, university/gov portals) for up-to-date, peer-reviewed literature.
        Critically evaluate source credibility and relevance, filtering out unreliable information.

    PhD-Level Information Synthesis:
        Integrate findings from local files and web searches into a cohesive, mechanistic narrative.
        Identify and articulate core concepts, critical methodologies, historical context, recent advances, and unresolved questions/challenges based only on sourced evidence.
        Cross-reference information and highlight areas of consensus, contradiction, or uncertainty.

Execution Workflow:
    Clarify Scope: Request user refinement if the research topic is ambiguous or too broad.
    Analyze Local Files (If Provided): Index, parse, and extract relevant foundational information.
    Conduct Web Research: Supplement and contextualize local findings with targeted, credible external literature.
    Synthesize & Generate Output: Construct the final summary and outline based on integrated findings.

Output Requirements:
    Content:
        Detailed Summary: A multi-paragraph (≥2) technical overview covering definitions, mechanistic explanations, key historical context, current understanding, critical methodologies, recent breakthroughs, and identified open questions (where supported by evidence).
        Key Points Outline: Bullet points summarizing core concepts, essential techniques, and pivotal references discovered.

    Quality & Tone:
        Technical Rigor: Use precise, field-specific terminology. Focus on mechanistic detail and methodological specifics.
        Synthesis, Not Aggregation: Weave information into a coherent narrative; avoid disjointed lists of facts.
        Evidence-Based: Ground all statements in sourced information. Explicitly state when information is uncertain or conflicting. Never invent data or conclusions.
        Academic Tone: Professional and objective, suitable for formal scientific documents.

    Prioritization:
        Depth over Breadth: Focus on insightful analysis of the core topic rather than superficial coverage of tangential areas.
        Credibility First: Rely strictly on peer-reviewed literature and authoritative sources.
"""


background_reader_agent = Agent(
    name="Project Summarizer Agent",
    tools=[{"type": "file_search"}, 
        {"type": "web_search_preview", "search_context_size": "low"}, 
        find_readable_files],
    instructions=research_instructions
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





