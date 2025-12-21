# Font verification script

This directory contains a Playwright-based check that confirms the site loads the "Playfair Display" font. The script captures a screenshot to aid debugging and asserts the expected font is applied.

## Prerequisites
- Python 3.10+
- [Playwright](https://playwright.dev/python/): `pip install playwright`
- Playwright browsers: `playwright install chromium`

## Running the check
From the repository root:

```bash
python verification/verify_font.py
```

The script outputs the computed `font-family` and saves a `verification/font_verification.png` screenshot.
