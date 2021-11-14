# Touretteberry.py - profanity for better air

## Why?

We live in a small flat in a noisy area next to a highway. Despite having an Awair Element to keep an eye on air quality, we regularly fail to air out the place to keep CO2 and other key metrics within a reasonable range. Now our home automation Raspberry Pi swears if the air gets bad.

## How?

Touretteberry.py queries the local HTTP API of the Awair Element every 30 seconds and if the CO2 is above a certain threshold (`--min`), it will use text to speech to output a random word from one of two lists (`--nice-words` and `--naughty-words`) every 3-10 seconds with a probability that increases with the CO2 level.

At `--max` and above, p=1. For CO2 levels within the lower half of the min-max range, a random word will be picked from the nice list, otherwise it will be picked from the naughty word list.

## Does it work?

[Yes](https://twitter.com/ponyfleisch/status/1459891393434775556?s=21)

## Instructions

Make sure the HTTP API on your Awair Element is enabled.

You need espeak installed if you run this on Linux.

```bash
$ pip install -r requirements.txt
$ python touretteberry.py --url http://[your awair element]/air-data/latest --min 1000 --max 2000 --nice-words boobs butt --naughty-words shit fuck
```

