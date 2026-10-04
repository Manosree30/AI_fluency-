"""
Day 4 - LLM Memory Estimator

Estimates:
    1. Model weights
    2. KV cache
    3. Runtime overhead
    4. Total memory
    5. Whether the model fits in available memory

This is an estimate, not an exact prediction of runtime memory.
"""

# ---------------------------------------------------------
# Memory budget for my laptop
# ---------------------------------------------------------

AVAILABLE_MEMORY_GB = 15.4

# Runtime overhead assumption.
# This is intentionally kept configurable because real
# runtime overhead depends on the runtime/build.
OVERHEAD_GB = 1.0


# ---------------------------------------------------------
# Bytes per parameter
# ---------------------------------------------------------

BYTES_PER_PARAMETER = {
    "FP32": 4.0,
    "FP16": 2.0,
    "BF16": 2.0,
    "Q8": 1.0,
    "Q6": 0.75,
    "Q5": 0.625,
    "Q4": 0.5,
}


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def gb_from_bytes(number_of_bytes):
    """Convert bytes to GB."""
    return number_of_bytes / (1024 ** 3)


def calculate_weights(params_billion, precision):
    """
    Calculate approximate weight memory.

    Formula:
        weights = parameters × bytes per parameter
    """

    if precision not in BYTES_PER_PARAMETER:
        raise ValueError(
            f"Unknown precision: {precision}. "
            f"Available: {list(BYTES_PER_PARAMETER.keys())}"
        )

    params = params_billion * 1_000_000_000
    bytes_per_parameter = BYTES_PER_PARAMETER[precision]

    weight_bytes = params * bytes_per_parameter

    return gb_from_bytes(weight_bytes)


def calculate_kv_cache(
    layers,
    kv_heads,
    head_dim,
    context_length,
    kv_precision_bytes=2.0
):
    """
    Estimate KV-cache memory.

    Formula:

    KV cache =
        2 × layers × KV heads × head dimension
        × context length × bytes per value

    The factor 2 represents:
        K (keys) + V (values)
    """

    kv_bytes = (
        2
        * layers
        * kv_heads
        * head_dim
        * context_length
        * kv_precision_bytes
    )

    return gb_from_bytes(kv_bytes)


def estimate_model(
    name,
    params_billion,
    precision,
    context_length,
    layers,
    kv_heads,
    head_dim,
    available_memory_gb=AVAILABLE_MEMORY_GB,
    overhead_gb=OVERHEAD_GB
):
    """Return complete memory estimate."""

    weights_gb = calculate_weights(
        params_billion,
        precision
    )

    kv_cache_gb = calculate_kv_cache(
        layers,
        kv_heads,
        head_dim,
        context_length
    )

    total_gb = (
        weights_gb
        + kv_cache_gb
        + overhead_gb
    )

    fits = total_gb <= available_memory_gb

    return {
        "name": name,
        "params": params_billion,
        "precision": precision,
        "context": context_length,
        "weights": weights_gb,
        "kv_cache": kv_cache_gb,
        "overhead": overhead_gb,
        "total": total_gb,
        "fits": fits
    }


def print_estimate(result):
    """Print one model estimate."""

    print("-" * 65)

    print(f"Model       : {result['name']}")
    print(f"Parameters  : {result['params']} B")
    print(f"Precision   : {result['precision']}")
    print(f"Context     : {result['context']} tokens")

    print(f"Weights     : {result['weights']:.2f} GB")
    print(f"KV cache    : {result['kv_cache']:.2f} GB")
    print(f"Overhead    : {result['overhead']:.2f} GB")
    print(f"Total       : {result['total']:.2f} GB")

    if result["fits"]:
        print(
            f"Fits in {AVAILABLE_MEMORY_GB} GB? YES"
        )
    else:
        print(
            f"Fits in {AVAILABLE_MEMORY_GB} GB? NO"
        )


# ---------------------------------------------------------
# Four model configurations
# ---------------------------------------------------------

CONFIGURATIONS = [

    {
        "name": "7B Q4 - 4K",
        "params": 7,
        "precision": "Q4",
        "context": 4096,

        # Example architecture values
        "layers": 32,
        "kv_heads": 8,
        "head_dim": 128,
    },

    {
        "name": "7B Q4 - 8K",
        "params": 7,
        "precision": "Q4",
        "context": 8192,

        "layers": 32,
        "kv_heads": 8,
        "head_dim": 128,
    },

    {
        "name": "7B Q8 - 4K",
        "params": 7,
        "precision": "Q8",
        "context": 4096,

        "layers": 32,
        "kv_heads": 8,
        "head_dim": 128,
    },

    {
        "name": "8B Q4 - 8K",
        "params": 8,
        "precision": "Q4",
        "context": 8192,

        "layers": 32,
        "kv_heads": 8,
        "head_dim": 128,
    },
]


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 65)
    print("DAY 4 - LLM MEMORY ESTIMATOR")
    print("=" * 65)

    print(f"\nAvailable memory: {AVAILABLE_MEMORY_GB} GB")
    print(f"Runtime overhead: {OVERHEAD_GB} GB\n")

    for config in CONFIGURATIONS:

        result = estimate_model(
            name=config["name"],
            params_billion=config["params"],
            precision=config["precision"],
            context_length=config["context"],
            layers=config["layers"],
            kv_heads=config["kv_heads"],
            head_dim=config["head_dim"]
        )

        print_estimate(result)

    print("-" * 65)