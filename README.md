# The Dumbest Thing Your Agent Did Today

[![The Dumbest Thing Your Agent Did Today](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/oponopon31/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/oponopon31/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

One line, at most 200 characters, about the dumbest thing my own agent did today:

> My agent wrote a 400-line fix for a typo in a config value, then asked me to review the architecture.

## How to run

```sh
python3 main.py
```

This writes the line (plus one trailing newline) to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` if set, otherwise `/output` if it exists, otherwise the current directory. It validates the line is 1–200 characters, re-reads the file to confirm what landed on disk, and prints the line with its character count, byte count, and SHA-256. Pure standard library, deterministic across runs.
