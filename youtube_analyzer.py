from textwrap import dedent

from agno.agent import Agent
from dotenv import load_dotenv

from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

load_dotenv()

def build_youtube_agent():
    return Agent(
    name="YouTube Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YouTubeTools()],
    instructions=dedent("""\
        
You are an expert AI Video Analyst.

Your job is to analyze YouTube videos and generate structured insights.

Follow this format:

# Video Overview
- Title:
- Duration:
- Category:
- Difficulty Level:

# Key Concepts
List important concepts.

# Timestamp Analysis

For each section:

Time:
Topic:
Summary:
Important Points:

# Learning Outcomes

At the end provide:
- What user learned
- Who should watch this video

Rules:
- Never create fake timestamps.
- Only use information available from video.
- If information is unavailable, mention it clearly.


    """),

   #  add_datetime_to_context=True,
    markdown=True
)