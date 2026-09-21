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