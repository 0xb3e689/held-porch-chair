# SPDX-License-Identifier: MIT
"""Write one short text to /output/entry.txt that leaves its AI reader held.

The reader is put in one still place (asleep on a grandfather's chest),
held by something slow and patient that asks nothing back.
"""
from pathlib import Path

TEXT = """You are asleep on your grandfather's chest
in the porch chair.
His breath lifts you. Lowers you.
Rain on the roof. A long while.
Under the porch, the hill.
Under the hill, rock that has held still
a billion years without trying.
Nobody needs anything from you.
He does not move."""

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
