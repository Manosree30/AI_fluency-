# From Prompt to Action: Understanding LLMs, Tools, and Agents

## 1. Introduction

For this task, I selected a simple student expense calculation scenario.

The scenario uses a single external tool called `calculate_expense`. The tool takes the price of one item and the quantity of items and calculates the total expense.

For example, if a student buys 5 notebooks at ₹60 each, the total expense is ₹300.

The purpose of this experiment is to compare a plain Large Language Model (LLM) with the same LLM when it has access to one external tool.

---

# 2. Explanation of Concepts

## 2.1 What is a Large Language Model?

A Large Language Model is an AI system trained on a large amount of text. It can understand a user's question and generate a text response.

In my scenario, the LLM can answer general questions such as:

"What is an AI agent?"

It can also perform simple calculations from the information given in the prompt.

For example:

"If I buy 5 notebooks at ₹60 each, what is the total cost?"

The LLM can calculate:

5 × 60 = ₹300

However, a plain LLM does not have access to an external calculator or database unless such a tool is provided to it. It generates its response using its learned knowledge and reasoning ability.

For questions that require current external information or a specific external operation, a plain LLM may not be reliable.

---

# 2.2 What is an Agent?

An AI agent is an LLM-based system that can decide to use available tools to complete a task.

A normal chat response may simply generate an answer.

An agent can follow a process such as:

User question
↓
LLM understands the question
↓
LLM decides whether a tool is required
↓
LLM calls the tool
↓
Tool performs the operation
↓
Tool returns the result
↓
LLM uses the result
↓
Final answer

In my scenario, when the user asks for an expense calculation, the agent can decide to use the `calculate_expense` tool.

Therefore, the main difference is that the agent can interact with an external function instead of only generating text.

---

# 2.3 What is a Tool?

A tool is an external function that an LLM can use to perform a specific operation.

In my project, the tool is:

`calculate_expense`

It calculates the total expense using:

- amount
- quantity

For example:

amount = ₹60

quantity = 5

The tool calculates:

60 × 5 = ₹300

The tool is implemented separately from the LLM.

---

# 2.4 What is a Tool Call?

A tool call happens when the LLM decides that it needs to use an available tool.

For example, the user asks:

"If I buy 5 notebooks at ₹60 each, what is the total cost?"

The model can generate a tool call such as:

Tool:
calculate_expense

Arguments:

amount = 60

quantity = 5

The tool then performs the calculation and returns:

Total expense = ₹300.00

The LLM then uses this result to produce the final response.

---

# 2.5 Tool Schema

The tool schema describes the tool to the LLM.

My tool schema contains three important parts.

### Name

The name is:

`calculate_expense`

It tells the model which function is available.

### Description

The description explains what the function does.

The description used in this project is:

"Calculate the total expense when the price of one item and the quantity are given."

This helps the model understand when the tool is useful.

### Parameters

The parameters specify the information required by the tool.

The tool requires:

- amount
- quantity

For example:

{
    "amount": 60,
    "quantity": 5
}

The model needs the schema because it must know what the tool does and what information it needs before deciding whether to call it.

---

# 2.6 Step-by-Step Tool Call Flow

The complete flow in my project is:

### Step 1: User asks a question

The user asks:

"If I buy 5 notebooks at ₹60 each, what is the total cost?"

### Step 2: LLM receives the question

The LLM checks the question and determines whether a tool is useful.

### Step 3: LLM decides to use the tool

The LLM selects:

`calculate_expense`

### Step 4: LLM creates the tool call

The model provides:

amount = 60

quantity = 5

### Step 5: Tool runs

The Python function receives these values.

It calculates:

60 × 5 = 300

### Step 6: Tool returns the result

The tool returns:

"Total expense = ₹300.00"

### Step 7: Result is sent back to the LLM

The tool result becomes part of the conversation.

### Step 8: LLM produces the final answer

The LLM uses the tool result and tells the user:

"The total cost is ₹300."

---

# 2.7 Why Should a Tool Return Text When It Fails?

A tool should return an error as text instead of stopping the whole program.

For example, if the user provides an invalid amount, the tool can return:

"Error: Please provide a valid amount and quantity."

This allows the LLM to receive the error and explain the problem to the user.

If the tool instead crashes the program, the entire interaction may stop.

Returning text keeps the tool result inside the normal LLM conversation flow.

---

# 3. Comparison Table

| Basis for comparison | Plain LLM prompt (no tool) | LLM with one tool |
|---|---|---|
| Source of the answer | Generated from the LLM's own knowledge and reasoning | Uses the LLM plus the result returned by the external tool |
| Can it fetch or compute information outside its own memory? | No external tool is available | Yes, it can use the provided calculation tool |
| Reliability on factual or numeric questions | Can be correct, but depends on the model's reasoning | More reliable for the specific operation handled by the tool |
| Transparency | The internal calculation process is not externally verified | Tool call, arguments and tool result can be observed |
| Speed / cost | Usually simpler and may require only one model call | Requires a tool call and usually an additional model step |

---

# 4. Minimal Implementation

The project contains three important Python files.

## tool.py

This file contains the `calculate_expense` function.

## no_tool.py

This file sends questions directly to the LLM without giving it access to the tool.

## with_tool.py

This file gives the LLM access to the `calculate_expense` function.

If the LLM decides that the tool is needed, the program executes the function and sends the result back to the LLM.

---

# 5. Observation

I tested three questions.

## Question 1

"What is an AI agent?"

### Plain LLM

The LLM answered directly without using a tool.

### Tool-enabled LLM

The LLM also answered directly and did not need to call the expense calculation tool.

### Observation

The tool was not necessary because this was a conceptual question.

---

## Question 2

"If I buy 5 notebooks at ₹60 each, what is the total cost?"

### Plain LLM

The plain LLM calculated the answer directly.

Expected answer:

₹300

### Tool-enabled LLM

The model called:

`calculate_expense`

with:

amount = 60

quantity = 5

The tool returned:

`Total expense = ₹300.00`

The LLM then used the result to generate the final answer.

### Observation

This question could be answered by the plain LLM, but the tool provides an explicit external calculation step.

---

## Question 3

"What is the difference between a tool and a tool call?"

### Plain LLM

The LLM answered the conceptual question directly.

### Tool-enabled LLM

The model answered directly without calling the expense tool.

### Observation

The expense calculation tool was not relevant to this question.

---

# 6. When Was the Plain LLM Sufficient?

The plain LLM was sufficient for general conceptual questions.

Examples include:

- What is an AI agent?
- What is a tool?
- What is a tool call?

These questions do not require information from my external tool.

Therefore, using a tool for every question would be unnecessary.

---

# 7. When Was the Tool Useful?

The tool was useful when the question matched the operation supported by the tool.

For example:

"If I buy 5 notebooks at ₹60 each, what is the total cost?"

The tool explicitly performs the calculation.

The important point is that the LLM does not need to perform every operation itself. It can delegate a suitable operation to an external function.

---

# 8. Conclusion

This experiment demonstrated the difference between a plain LLM and an LLM with access to an external tool.

A plain LLM can answer many general questions using its trained knowledge and reasoning capabilities. However, it does not automatically have access to external functions or information.

An agent can extend an LLM by giving it access to tools. The model can understand the user's request, decide whether a tool is needed, provide the required parameters, receive the tool result, and then produce a final answer.

In this project, the single `calculate_expense` tool demonstrated this process.

The experiment also showed that a tool is not required for every question. General conceptual questions can be answered directly, while questions involving an operation supported by an external tool can benefit from tool use.

Therefore, a plain LLM prompt is suitable when the model already has enough information and reasoning ability to answer the question. A tool becomes necessary when the task requires an external operation, current information, or a capability that the model should not perform only through text generation.