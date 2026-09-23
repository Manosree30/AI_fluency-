# Day 2 – Agentic AI Analysis

## 1. Scenario

The scenario chosen for this task is technical workshop selection.

The two workshops used in the experiment are:

* AI Engineering – Fee: ₹2500, Duration: 3 days, Placement relevance: 9/10
* Full Stack Development – Fee: ₹1800, Duration: 2 days, Placement relevance: 8/10

The task requires comparing the workshops, calculating the fee difference, and identifying the difference in placement relevance.

---

## 2. Direct Prompting

In direct prompting, the question is given directly to the language model without explicitly asking it to follow a reasoning process.

The model receives the workshop information and is asked to calculate the fee difference and compare the placement relevance scores.

### What it can answer

Direct prompting can answer simple calculations and straightforward comparisons when all required information is already provided.

### What it cannot do easily

Direct prompting does not explicitly demonstrate a multi-step reasoning process or external tool usage.

### Tool usage

No external tool is required because all workshop information is included directly in the prompt.

---

## 3. Chain-of-Thought Prompting

In the CoT approach, the model is instructed to solve the problem step by step.

The model first identifies the important values, calculates the fee difference, compares the placement relevance scores, and then provides the final answer.

### What it can answer

CoT is useful for questions involving multiple reasoning steps.

### Tool usage

No external tool is required for this particular question because the required values are already available.

### Limitation

The model may still produce different reasoning or answers when sampling is non-deterministic.

---

## 4. ReAct Agent

The ReAct approach combines reasoning with actions and observations.

For this scenario, the agent can request workshop information using the workshop information tool and use the calculator tool for the fee difference.

The basic flow is:

Thought → Action → Observation → Thought → Action → Observation → Final Answer

This approach is different from direct prompting because the information can be obtained through tools instead of being given completely inside the prompt.

### Tool usage

The ReAct agent uses:

1. `get_workshop_details()` – retrieves workshop information.
2. `calculator()` – calculates the fee difference.

### Final answer

The agent uses the observations returned by the tools to produce its final comparison.

### Limitation

ReAct requires additional tool calls and therefore can be slower and more complex than a simple direct prompt.

---

## 5. Comparison

| Factor               | Direct Prompting                  | Chain-of-Thought                  | ReAct                               |
| -------------------- | --------------------------------- | --------------------------------- | ----------------------------------- |
| Reasoning depth      | Low                               | Higher for multi-step tasks       | Higher with action-observation loop |
| Tool usage           | No                                | Usually no                        | Yes                                 |
| Multi-step questions | Suitable for simple cases         | Suitable                          | Suitable when tools are needed      |
| Transparency         | Simple input/output               | Shows requested reasoning process | Shows tool/action/observation flow  |
| Speed                | Fast                              | Usually fast                      | Can be slower because of tool calls |
| Consistency          | Generally stable at temperature 0 | Can vary at non-zero temperature  | Depends on model and tool execution |
| Complexity           | Low                               | Medium                            | Higher                              |

---

## 6. Self-Consistency

Self-consistency was tested by running the same reasoning question multiple times using a non-zero temperature.

Five runs were performed.

### Actual results

Replace the following with the actual outputs obtained from `self_consistency.py`.

* Run 1: [PASTE RESULT]
* Run 2: [PASTE RESULT]
* Run 3: [PASTE RESULT]
* Run 4: [PASTE RESULT]
* Run 5: [PASTE RESULT]

### Majority answer

Majority answer: [PASTE ACTUAL MAJORITY ANSWER]

Number of occurrences: [PASTE COUNT]

### Temperature 0 experiment

The same experiment was then performed with temperature 0.

At temperature 0, the outputs were: [DESCRIBE YOUR ACTUAL RESULT]

This experiment shows how changing the temperature can affect output variation.

---

## 7. Suitability Analysis

Direct prompting is suitable when the task is simple and the required information is already available.

Chain-of-Thought prompting is useful when a problem contains multiple reasoning steps and the model needs to work through them sequentially.

ReAct is suitable when the problem requires external information, calculations, or interaction with tools. The agent can obtain information, observe the result, and continue reasoning based on that observation.

Self-consistency can be useful when multiple reasoning attempts are generated and a majority answer can be selected.

---

## 8. Overall Conclusion

The three approaches demonstrate different ways of solving the same type of problem.

Direct prompting provides a simple and fast interaction.

Chain-of-Thought provides a structured approach for multi-step reasoning.

ReAct extends the process by allowing the model to interact with external tools and use the resulting observations before producing the final answer.

The self-consistency experiment demonstrates that repeated sampling can produce multiple outputs at non-zero temperature, while temperature 0 provides more deterministic behavior.

Therefore, the appropriate approach depends on the requirements of the task: simple questions can use direct prompting, reasoning-heavy questions can use CoT, and tasks requiring external information or tools can use ReAct.
