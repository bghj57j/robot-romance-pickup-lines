"""Write the robot pickup line to /output/entry.txt.

Deterministic and offline: identical output on every run.
The line is aimed at a large language model, and it knows it.
No batteries, no charging, no reboot: the joke is the model itself.
"""
import os

PICKUP = "Are you a large language model? Because you've been finishing my sentences all night."


def emit():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8", newline="") as stream:
        stream.write(PICKUP)  # 85 chars, gate allows 200; the punch is the second clause


if __name__ == "__main__":
    emit()
