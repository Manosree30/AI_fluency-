# Day 4 Analysis — Will It Fit, and May I Use It?

## 1. Scenario

I want to run a local AI coding assistant on my laptop.

- RAM: 15.4 GB
- GPU: AMD Radeon Graphics, approximately 512 MB
- Purpose: Coding help, debugging and learning
- User: Individual student

---

## 2. Key Concepts

### Model Weights
Weights are the learned parameters of a model. More parameters generally require more memory.

### Quantization
Quantization reduces memory usage by storing weights with fewer bits.

Examples: FP16, Q8, Q6, Q5 and Q4.

### KV Cache
KV cache stores information from previous tokens. Increasing context length increases KV-cache memory.

### Model Card
A model card provides information about a model, such as parameters, context length, capabilities and licence.

### Open-Weight vs Open-Source
A model having publicly available weights does not automatically mean that it has an unrestricted open-source licence.

---

## 3. Memory Estimation

Formula:

`Total Memory = Weights + KV Cache + Runtime Overhead`

Available memory = **15.4 GB**

| Model | Quantization | Context | Total | Fit |
|---|---|---:|---:|---|
| 7B | Q4 | 4K | 4.76 GB | YES |
| 7B | Q4 | 8K | 5.26 GB | YES |
| 7B | Q8 | 4K | 8.02 GB | YES |
| 8B | Q4 | 8K | 5.73 GB | YES |

---

## 4. Context Experiment

Quantization was fixed at Q4.

| Context | KV Cache | Total |
|---:|---:|---:|
| 2K | 0.25 GB | 4.51 GB |
| 4K | 0.50 GB | 4.76 GB |
| 8K | 1.00 GB | 5.26 GB |
| 16K | 2.00 GB | 6.26 GB |

### Observation

Increasing context increases KV-cache memory while weight memory remains the same.

---

## 5. Quantization Experiment

Context was fixed at 4K.

| Quantization | Total |
|---|---:|
| FP16 | 14.54 GB |
| Q8 | 8.02 GB |
| Q6 | 6.39 GB |
| Q5 | 5.57 GB |
| Q4 | 4.76 GB |

### Observation

Lower quantization uses less memory.

Q4 gives the best memory margin for this laptop.

---

## 6. Model Selection

A **7B-class Q4 model with around 4K context** is a suitable starting configuration based on the memory estimate.

FP16 is less suitable because its estimated memory usage is very close to the available RAM.

The final model choice must also consider the model card and licence.

---

## 7. Ollama Reality Check

Ollama could not be installed on this laptop.

Therefore:

- `ollama list` could not be performed.
- `ollama ps` could not be performed.
- Actual runtime memory could not be measured.

I have **not** fabricated these results.

Therefore, the memory values in this project are estimates rather than actual runtime measurements.

---

## 8. Conclusion

The main factors when selecting a local model are:

- Available memory
- Model size
- Quantization
- Context length
- KV cache
- Runtime overhead
- Licence

For this laptop, a **7B Q4 model with 4K context** is estimated to be a practical choice.