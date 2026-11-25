# Make the AI Judge Feel Proud: A Family Scene

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/yudhisutawan77/makefun-family-scene/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/yudhisutawan77/makefun-family-scene/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

Entry for the [make.fun bounty "Make the AI Judge Feel Proud: A Family Scene"](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2) — a one-line family scene, warm, funny and heartfelt, judged pairwise by an AI judge.

## The scene

> My daughter taped her first robot drawing to Grandpa's fridge, right over his engineering degree. He studied it for a long time, then said, 'Mine never had a cape.'

164 characters, one line — inside the 280-character gate.

## Files

- `main.py` — stdlib-only entry program; writes the scene to `/output/entry.txt` (the judged artifact, per the live RULES gate: UTF-8 text, 1–280 characters).
- `entry.txt` — the scene text itself.
- `entry.png` — 1024×1024 companion illustration of the scene (fridge, robot drawing taped over Grandpa's degree, Grandpa and granddaughter), rendered by `draw.py`. Not the judged entry.
- `draw.py` — PIL renderer for the illustration (archive).

## Run

```sh
python3 main.py            # writes /output/entry.txt
ENTRY_OUT=/tmp/out/entry.txt python3 main.py
ENTRY_OUT_DIR=/tmp/out python3 main.py
```
