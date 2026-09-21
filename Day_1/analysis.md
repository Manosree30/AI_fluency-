# Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario

The scenario selected for this task is a **Private Student Expense Assistant**.

A private JSON file named `private_data.json` contains a student's monthly
budget and individual expenses. The expenses are categorized into Food,
Travel, and Shopping.

The user can ask a question such as:

> How much did I spend on food?

The same problem is implemented using three different approaches:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The purpose of this experiment is to understand the differences between
an LLM-only chatbot, a predefined rule-based workflow, and an AI agent
that uses an LLM together with tools.

---

## 2. Private Data

The private data is stored locally in `private_data.json`.

The data contains:

- Monthly budget: ₹5000
- Food expenses: ₹120, ₹150, ₹70, ₹130
- Travel expenses: ₹80, ₹100
- Shopping expense: ₹200

Therefore, the total food expense is:

**₹120 + ₹150 + ₹70 + ₹130 = ₹470**

The private data is not directly given to the plain chatbot.

---

## 3. Plain Chatbot

The plain chatbot uses an LLM to understand and respond to the user's
question.

In this implementation, the chatbot does not have access to the private
`private_data.json` file.

For example, if the user asks:

> How much did I spend on food?

the chatbot cannot calculate the actual amount because the private
expense data is not available to it.

The chatbot mainly depends on the language model to generate a response.
It does not use a separate tool to read the private expense file or
calculate the expense.

### Data Access

The plain chatbot does not directly access the student's private JSON
data.

### Tools and Rules

No external tool is used. The LLM generates the response based on the
information available in the conversation.

### Request Flow

The flow is:

User Question → LLM → Response

### Limitation

The main limitation is that the chatbot cannot reliably answer questions
that require private information that has not been provided to it.

---

## 4. Rule-Based Workflow

The rule-based workflow directly reads the private `private_data.json`
file.

It does not use an LLM. Instead, it uses predefined conditions to
understand the type of question.

For example, when the user asks about food spending, the program checks
whether the question contains the word "food" and whether it is related
to spending.

If the condition matches, the program reads the expense data and adds
all Food expenses.

For the question:

> How much did I spend on food?

the workflow calculates:

**₹120 + ₹150 + ₹70 + ₹130 = ₹470**

and returns:

> You spent ₹470 on food.

### Data Access

The workflow has direct access to the private JSON file.

### Tools and Rules

It uses predefined `if` and `elif` conditions and directly performs
calculations on the data.

### Request Flow

The flow is:

User Question → Predefined Rule → Read Private Data → Calculate → Response

### Limitation

The main limitation is flexibility.

The workflow can only handle questions for which rules have already been
defined. If the user asks a question that does not match the available
rules, the workflow cannot handle it.

---

## 5. AI Agent

The AI agent combines an LLM with tools and an execution process.

In this implementation, the agent receives the user's question and
decides which tool should be used.

For example, for:

> How much did I spend on food?

the agent identifies that the `calculate_category_total` tool is required
and selects:

`calculate_category_total("Food")`

The tool reads the private JSON data and calculates the total.

The tool returns:

**₹470**

The agent then observes this result and sends the result to the LLM to
generate the final natural-language response.

The final response is:

> You spent ₹470 on food.

### Data Access

The AI agent accesses private data through its tools.

The LLM itself does not directly read the JSON file. The tool performs
the data access and calculation.

### Tools and Rules

The agent uses the following tools:

- `calculate_category_total()`
- `get_budget()`

The `calculate_category_total()` tool calculates spending for a selected
category.

The `get_budget()` tool returns the monthly budget.

### Request Flow

The flow is:

User Question  
↓  
Agent receives request  
↓  
Agent selects a tool  
↓  
Tool accesses private data  
↓  
Tool returns result  
↓  
Agent observes result  
↓  
LLM generates final answer

This demonstrates the basic **LLM + Tools + Loop** concept.

### Limitation

The agent depends on both the language model and the tools.

If the model selects an incorrect action or if a tool has an error, the
final response may also be incorrect.

---

## 6. Comparison

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for natural conversation | Limited to predefined rules | High |
| Decision-making | LLM generates a response | Predefined conditions | Agent interprets request and selects an action |
| Tool usage | No separate tool | Direct program operations | Uses dedicated tools |
| Private-data access | No direct access | Yes | Yes, through tools |
| Multi-step task handling | Limited | Only predefined steps | Can perform multiple steps |
| Automation | Limited for private-data tasks | High for predefined tasks | High |
| Reliability | Cannot reliably answer unavailable private-data questions | Reliable for covered rules | Depends on LLM and tool behavior |

---

## 7. Flexibility

The plain chatbot provides flexible natural-language interaction because
the user can communicate with the LLM using normal language.

The rule-based workflow is less flexible because it depends on predefined
conditions. New types of questions require new rules to be added.

The AI agent combines natural-language understanding with tools. It can
interpret the user's request and select an appropriate action, making it
more suitable for tasks that require both language understanding and
private-data operations.

---

## 8. Decision-Making

The plain chatbot mainly generates an answer using the LLM.

The rule-based workflow follows fixed conditions written by the
developer. Its decision-making is therefore predictable and predefined.

The AI agent interprets the user's request and selects an appropriate
tool. In the expense example, it identifies the Food category and uses
the `calculate_category_total` tool.

---

## 9. Tool Usage

The plain chatbot does not use a separate tool for this scenario.

The rule-based workflow directly performs operations on the private
JSON data.

The AI agent uses dedicated tools such as:

`calculate_category_total()`

and:

`get_budget()`

This allows the agent to perform actions using private information.

---

## 10. Private-Data Access

The plain chatbot does not have direct access to the student's private
expense file.

The rule-based workflow directly reads `private_data.json`.

The AI agent accesses the private data through its tools. This provides
a separation between the language model and the private data operation.

---

## 11. Multi-Step Task Handling

The plain chatbot is mainly designed for generating conversational
responses and does not perform the complete private-data workflow in
this implementation.

The rule-based workflow can perform multiple predefined operations, but
the sequence must be explicitly programmed.

The AI agent can follow a sequence such as:

1. Receive the request.
2. Understand the request.
3. Select a tool.
4. Execute the tool.
5. Observe the result.
6. Generate the final response.

This demonstrates multi-step processing.

---

## 12. Automation

The rule-based workflow provides reliable automation for tasks that have
known and predefined conditions.

The AI agent can automate tasks where the required action depends on the
user's natural-language request.

For example, different questions can lead to different tool selections.

The plain chatbot provides conversational automation but does not perform
the private-data operation in this implementation.

---

## 13. Reliability

The rule-based workflow is predictable when the user's request matches
one of its predefined rules.

The plain chatbot cannot reliably provide the student's actual expense
amount when it does not have access to the private data.

The AI agent can provide the correct result when the correct tool is
selected and the tool operates correctly. However, because an LLM is
involved, its behavior can depend on the model and the implementation.

---

## 14. Suitability Analysis

### Plain Chatbot

A plain chatbot is suitable for general conversational tasks where an
LLM response is sufficient and private-data access is not required.

### Rule-Based Workflow

A rule-based workflow is suitable for predictable tasks where the
conditions and steps can be clearly defined in advance.

For this expense scenario, it can reliably calculate totals for the
categories covered by its predefined rules.

### AI Agent

An AI agent is suitable for tasks that require natural-language
understanding together with actions involving data or tools.

In this scenario, the agent can receive the user's question, select the
appropriate tool, access the private expense data through the tool,
observe the result, and generate a final response.

---

## 15. Conclusion

This experiment demonstrates the difference between a plain chatbot,
a rule-based workflow, and an AI agent.

The plain chatbot mainly uses an LLM to generate conversational
responses.

The rule-based workflow uses predefined conditions and program logic to
perform predictable tasks.

The AI agent combines an LLM with tools and an execution process. It can
receive a request, select an appropriate tool, access private data,
observe the tool result, and generate a final response.

Therefore, the experiment demonstrates the basic concept of an AI agent:

**Agent = LLM + Tools + Loop**

The three approaches are useful for different types of tasks, depending
on whether the problem requires natural-language interaction,
predefined rules, private-data access, tool usage, or multi-step
processing.