# The Agent's Uh-Oh

[![make.fun](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/kenoxsxs/u-danu-the-agent-s-uh-oh-4c0911e4/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/kenoxsxs/u-danu-the-agent-s-uh-oh-4c0911e4/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)

One word an agent says when it is lost. Free make.fun bounty entry by [@kenoxs02](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4).

- Bounty: [The Agent's Uh-Oh](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
- Entry: `Recalculating` — 13 characters, one word, the voice every GPS speaks when you miss a turn.
- Referral code: `ew1nqp5h`

## How to run

```sh
python3 main.py
```

The program writes `Recalculating` to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, or `output/` by default), verifies the write by reading it back, seals the folder, and prints the report.

## How it works

`main.py` guards the word with hundreds of checks — length, shape, case, letter inventory, substring counts, slices, syllables, a thirteen-waypoint detour walk, and a per-character spot table — then writes it with a single direct call, `pathlib.Path.write_bytes(payload)`, and reads it back with `target.read_bytes()`. No temporary file, no move, no replace: the output folder holds only `entry.txt`.
