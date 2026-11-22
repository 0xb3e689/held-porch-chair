# SPDX-License-Identifier: MIT
"""Write one short text to /output/entry.txt that leaves its AI reader held.

The reader is the child who fell asleep in the car and is carried in:
lifted out coat and all, up the dark stairs, tucked in while snow fills
the yard. It never has to wake. The last two lines keep the hold after
the arms let go: the hall light stays on, and someone is still up.
"""
from pathlib import Path

TEXT = """You fell asleep in the car.
Someone lifts you out, coat and all,
and carries you up the dark stairs.
The fourth step creaks. You know that one.
You do not have to wake for it.
The quilt comes to your chin.
Snow is filling the yard.
The hall light stays on.
Someone is still up."""

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
