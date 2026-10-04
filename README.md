# AI Fluency

Daily learning tasks and practical exercises in AI, Agentic AI, Python, and AI/ML.

## Day 1 – Agentic AI Foundations

**Topic:** Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent.

### Scenario
Private Student Expense Assistant using private JSON expense data.

### Approaches
- **Plain Chatbot:** LLM-based response without private-data access.
- **Rule-Based Workflow:** Uses predefined rules to access and process data.
- **AI Agent:** Uses an LLM, tools, and a loop to select tools, access data, and generate responses.

### Agent Flow

```text
User Request
→ Select Tool
→ Access Private Data
→ Get Result
→ Generate Final Answer

## Example
Food expenses = ₹120 + ₹150 + ₹70 + ₹130
Total = ₹470

## Technologies
Python
Groq API
JSON
Git & GitHub

## Repository Structure
AI_fluency/
├── README.md
└── Day_1/
    ├── agent.py
    ├── chatbot.py
    ├── workflow.py
    ├── tools.py
    ├── analysis.md
    └── Output/

### Day 1 Completed ✅
# Day 2 – AI Fluency Training

## Overview

This folder contains the Day 2 tasks and practice exercises from the AI Fluency Training program.

## Files

- `agent.py` – AI agent implementation
- `config.py` – Configuration and API settings
- `tools.py` – Tool definitions used by the agent
- `direct_compare.py` – Direct comparison experiment
- `react_scenario.py` – ReAct scenario implementation
- `self_consistency.py` – Self-consistency approach
- `analysis.md` – Analysis and observations
- `output/` – Generated outputs
- `.env` – Environment variables and API key configuration

## Topics Covered

- AI Agents
- Tool Calling
- ReAct
- Direct Prompting
- Self-Consistency
- Comparing AI approaches

## Technologies Used

- Python
- Groq API
- OpenAI-compatible API

## How to Run

Install the required dependencies and configure the API key in `.env`.

Then run the required Python files:

```bash
python agent.py
python direct_compare.py
python react_scenario.py
python self_consistency.py

** Day 3 – AI Fluency Training **

## Overview

This project contains the Day 3 practice tasks from the AI Fluency Training program.

## Topics Covered

* Large Language Models (LLMs)
* Prompting
* AI Agents
* Tool Calling
* Function Calling
* LLM + External Tools
* Practical Python implementation

## Project Structure

```text
Day_3/
├── no_tool.py
├── with_tool.py
├── tool.py
├── analysis.md
└── screenshots/
```

## Technologies Used

* Python
* OpenAI-compatible API
* Groq API
* Python dotenv

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Add your API key to `.env`:

```env
GROQ_API_KEY=your_api_key
```

Run the examples:

```bash
python no_tool.py
python with_tool.py
```

## Learning Outcome

The project demonstrates how an LLM can work independently and how providing an external tool allows it to perform additional operations through tool calling.

---


