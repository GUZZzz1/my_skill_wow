#!/usr/bin/env python3
import json
import math
import sys


WEIGHTS = {
    "D1": 0.15,
    "D2": 0.15,
    "D3": 0.15,
    "D4": 0.15,
    "D5": 0.10,
    "D6": 0.10,
    "D7": 0.10,
    "D8": 0.10,
}

CRITICAL = ("D1", "D2", "D4", "D5")


def grade(score):
    if score >= 9.0:
        return "S"
    if score >= 7.5:
        return "A"
    if score >= 6.0:
        return "B"
    if score >= 4.0:
        return "C"
    return "D"


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: calculate_score.py '{\"D1\": 8, ..., \"D8\": 8}'")

    scores = json.loads(sys.argv[1])
    missing = [key for key in WEIGHTS if key not in scores]
    extra = [key for key in scores if key not in WEIGHTS]
    if missing or extra:
        raise SystemExit(f"invalid dimensions: missing={missing}, extra={extra}")

    for key, value in scores.items():
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
            or not 0 <= value <= 10
        ):
            raise SystemExit(f"{key} must be a number between 0 and 10")

    total = round(sum(scores[key] * weight for key, weight in WEIGHTS.items()), 2)
    critical_pass = all(scores[key] >= 6.0 for key in CRITICAL)
    result = {
        "score": total,
        "grade": grade(total),
        "design_pass": total >= 7.5 and critical_pass,
        "critical_dimensions_pass": critical_pass,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
