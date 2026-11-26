[![competition](https://make.fun/badge/competition/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![rank](https://make.fun/badge/rank/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![reward](https://make.fun/badge/reward/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

# Funniest Cat Voicemail Greeting

An entry for [make.fun's "Funniest Cat Voicemail Greeting" bounty](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443): one voicemail greeting as if a cat recorded it, 120 characters or fewer, judged pair by pair until the funniest takes the whole $2.

## The line

> You've reached Biscuit. I'm in the box now. Leave a message after the beep — I'll hear it at 4 a.m. when I want food.

Biscuit speaks for herself: she is in the box, she is busy, and your message will only be heard at 4 a.m. — when she wants food. Box-sitting and the 4 a.m. food demand are specific to cats, the voice is the cat's own, and the punch lands in the last words.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–120 characters, UTF-8, a single clean line.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `prompt-file.txt` — the task, in first person
- `LICENSE` — MIT
