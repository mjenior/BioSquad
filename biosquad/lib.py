
import re
from .roles import *

## Prompt modifiers

CHAIN_OF_DRAFT = """
Think step by step, but only keep a minimum draft for each thinking step, with 5 words at most. 
Return the answer at the end of the response after a separator ####.
"""

CHAIN_OF_THOUGHT = """
1. Begin with a <thinking> section which includes: 
 a. Briefly analyze the question and outline your approach. 
 b. Present a clear plan of steps to solve the problem. 
 c. Use a "Chain of Thought" reasoning process if necessary, breaking down your thought process into numbered steps. 
 d. Close the thinking section with </thinking>.
2. Include a <reflection> section for each idea where you: 
 a. Review your reasoning. 
 b. Check for potential errors or oversights. 
 c. Confirm or adjust your conclusion if necessary. 
 d. Be sure to close all reflection sections with </reflection>. 
3. Provide your final answer in an <output> section. 
 a. Always use these tags in your responses. 
 b. Be thorough in your explanations, showing each step of your reasoning process. 
 c. Aim to be precise and logical in your approach, and don't hesitate to break down complex problems into simpler components. 
Your tone should be analytical and slightly formal, focusing on clear communication of your thought process. 
Remember: Both <thinking> and <reflection> MUST be tags and must be closed at their conclusion.
Remember: Make sure all <tags> are on separate lines with no other text. 
"""

REFINE_PROMPT = """
Your primary task is to refine or improve the user prompt below this section of instructions.
Refined prompt text should be at least four sentences long.
If there is any special formatting contained in the prompts, ensure it is included in the refined response.
Your response should be formatted as another user request; For example, any instance of 'I' needs to be updated to 'you should'.
Do NOT include any content related directly to prompt refinement, and ONLY report your new suggested version.
"""

CONDENSE_RESPONSE = """
Your task is to refine and synthesize all of the following text provided into a single cohesive response. 
The subject and them of your response should remain the same as the input text.
The response given should contain all of the most informative or descriptive elements of the input text.
Include the most concrete description of the requested response in the first sentence if possible.
"""

SUMMARIZE_CONVERSATION = """
Summarize the following conversation between a user and an AI assistant.
Include all key points from both user requests and agent responses.
Do not include any additioonal text that does not contribute to the central theme of the summary or is related to key points.
Be as concise as possible with sacrificing important content.
The complete summary text must be no longer than 1000 characters total.
"""

# Common file extension dictionary, which don't match directly with language name
extDict = {
   'bash': '.sh',
   'cuda': '.cu',
   'cython': '.pyx',
   'c++': '.cpp',
   'javascript':'.js',
   'julia':'.jl',
   'markdown': '.md',
   'matlab': '.mat',
   'nextflow': '.nf',
   'perl': '.pl',
   'python': '.py',
   'ruby': '.rb',
   'shell': '.sh',
   'text':'.txt',
   'plaintext': '.txt',
   }

patternDict = {
   "python": {
      "function": re.compile(r'def\s+(\w+)\s*\('),
      "class": re.compile(r'class\s+(\w+)\s*[:\(]'),
      "variable": re.compile(r'(\w+)\s*=\s*[^=\n]+'),
   },
   "javascript": {
      "function": re.compile(r'function\s+(\w+)\s*\('),
      "class": re.compile(r'class\s+(\w+)\s*[{]'),
      "variable": re.compile(r'(?:let|const|var)\s+(\w+)\s*='),
   },
   "java": {
      "function": re.compile(r'(?:public|private|protected)?\s*\w+\s+(\w+)\s*\('),
      "class": re.compile(r'class\s+(\w+)\s*[{]'),
      "variable": re.compile(r'(?:public|private|protected)?\s*\w+\s+(\w+)\s*='),
   },
   "r": {
      "function": re.compile(r'(\w+)\s*<-\s*function\s*\('),
      "variable": re.compile(r'(\w+)\s*<-\s*[^=\n]+'),
   },
   "groovy": {
      "function": re.compile(r'def\s+(\w+)\s*\('),
      "class": re.compile(r'class\s+(\w+)\s*[{]'),
      "variable": re.compile(r'def\s+(\w+)\s*='),
   },
}

