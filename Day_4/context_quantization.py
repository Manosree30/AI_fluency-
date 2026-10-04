"""
Day 4 - Context Length and Quantization Experiment

Experiment 1:
    Keep quantization fixed.
    Change context length.

Experiment 2:
    Keep context length fixed.
    Change quantization.
"""

from vram_estimate import (
    estimate_model,
    AVAILABLE_MEMORY_GB
)


# ---------------------------------------------------------
# Model architecture used for the experiment
# ---------------------------------------------------------

MODEL_NAME = "7B Model"

PARAMS = 7

LAYERS = 32
KV_HEADS = 8
HEAD_DIM = 128


# ---------------------------------------------------------
# Experiment 1
# Context length changes
# Quantization remains Q4
# ---------------------------------------------------------

def context_experiment():

    print("\n")
    print("=" * 75)
    print("EXPERIMENT 1 - CONTEXT LENGTH")
    print("=" * 75)

    precision = "Q4"

    context_lengths = [
        2048,
        4096,
        8192,
        16384
    ]

    print(
        f"\nFixed quantization: {precision}"
    )

    print()

    print(
        f"{'Context':<12}"
        f"{'Weights':<15}"
        f"{'KV Cache':<15}"
        f"{'Total':<15}"
        f"{'Fits?'}"
    )

    print("-" * 75)

    for context in context_lengths:

        result = estimate_model(
            name=MODEL_NAME,
            params_billion=PARAMS,
            precision=precision,
            context_length=context,
            layers=LAYERS,
            kv_heads=KV_HEADS,
            head_dim=HEAD_DIM
        )

        print(
            f"{context:<12}"
            f"{result['weights']:<15.2f}"
            f"{result['kv_cache']:<15.2f}"
            f"{result['total']:<15.2f}"
            f"{'YES' if result['fits'] else 'NO'}"
        )


# ---------------------------------------------------------
# Experiment 2
# Quantization changes
# Context remains 4096
# ---------------------------------------------------------

def quantization_experiment():

    print("\n")
    print("=" * 75)
    print("EXPERIMENT 2 - QUANTIZATION")
    print("=" * 75)

    context = 4096

    quantizations = [
        "FP16",
        "Q8",
        "Q6",
        "Q5",
        "Q4"
    ]

    print(
        f"\nFixed context length: {context} tokens"
    )

    print()

    print(
        f"{'Quantization':<15}"
        f"{'Weights':<15}"
        f"{'KV Cache':<15}"
        f"{'Total':<15}"
        f"{'Fits?'}"
    )

    print("-" * 75)

    for precision in quantizations:

        result = estimate_model(
            name=MODEL_NAME,
            params_billion=PARAMS,
            precision=precision,
            context_length=context,
            layers=LAYERS,
            kv_heads=KV_HEADS,
            head_dim=HEAD_DIM
        )

        print(
            f"{precision:<15}"
            f"{result['weights']:<15.2f}"
            f"{result['kv_cache']:<15.2f}"
            f"{result['total']:<15.2f}"
            f"{'YES' if result['fits'] else 'NO'}"
        )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 75)
    print("DAY 4 - CONTEXT AND QUANTIZATION EXPERIMENT")
    print("=" * 75)

    print(
        f"\nAvailable memory: {AVAILABLE_MEMORY_GB} GB"
    )

    context_experiment()

    quantization_experiment()