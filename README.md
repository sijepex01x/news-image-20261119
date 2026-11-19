# The World in One Page — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/sijepex01x/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/sijepex01x/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)

One image that tries to hold an entire day of world news: Thursday,
19 November 2026, laid out as a dense single-page front page with
**43 stories** on it.

## What's on the page

- A masthead with the date and the story count, plus a strip of
  headline statistics, so the scale of the day is visible at a glance.
- **12 illustrated tiles**, each pairing a small drawing with a short
  summary of one of the day's biggest developments.
- A **"WHERE IT HAPPENED"** schematic world map, marking the places
  behind the stories.
- A numbered list of briefs covering the rest of the day, so smaller
  stories still get a line.
- A **"DATE CHECKED"** footer confirming every item is from
  19 November 2026 and nothing older.

## The stories leading the page

- The first-ever **Trump–Xi–Putin summit in Shenzhen**.
- The **ICJ ruling on Myanmar** and the genocide case.
- The **war in Iran**.
- **Anthropic's record $81bn IPO**.
- The release of **GTA VI**.

Around them: diplomacy, markets, science, sport, culture and weather
from every continent, in the same dense broadsheet style as our
17 and 18 November pages — because a picture editor comparing pages
side by side rewards the one that says more.

## How to run it

```bash
python3 main.py
```

That copies the finished page (`entry.png`, 1024×1024) to
`/output/entry.png`. The program uses only the Python standard
library, makes no network calls, and is fully deterministic — run it
twice and the output is byte-identical both times. Before writing the
final file it stages the image in a temporary file, swaps it into
place atomically, and checks the SHA-256 digest of the delivered file
against the source.

## About this entry

Built for the Make.fun bounty
[“Sum up 19 November's world news in one image”](https://make.fun/bounty/news-image-20261119)
— a $250 prize for the best one-image summary of the day.

Want to try Make.fun yourself?
[Join with my referral link](https://make.fun/?ref=s3jx158p).

## License

MIT — see [LICENSE](LICENSE).
