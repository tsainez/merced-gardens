# Bolt's Journal
## 2024-05-23 - Lazy Loading Below-Fold Images
**Learning:** Images in the "Features" section are rendered below the fold (after the intro and services strip) but were being eagerly loaded.
**Action:** Always check for `loading="lazy"` opportunities on images that are not in the initial viewport (LCP candidates). This reduces initial bandwidth usage and prioritizes critical resources.

## 2024-05-22 - Initial Setup
**Learning:** This is a fresh start for Bolt in this repository.
**Action:** Proceed with identifying performance opportunities in the Jekyll site.

## 2024-05-22 - Missing Ruby Runtime
**Learning:** The environment lacks a Ruby runtime, preventing local execution of `jekyll build` or `bundle install`.
**Action:** Verify changes by creating temporary HTML reproduction files or parsing source files, rather than relying on the build process.

## 2024-05-24 - Manual Asset Optimization
**Learning:** Lacking a build pipeline (Jekyll plugins) to auto-optimize images, a 2.1MB PNG was manually converted to WebP via Python. The 80% reduction (438KB) highlights the importance of checking raw asset sizes in static repos.
**Action:** In static site environments without asset pipelines, manually inspect and optimize heavy media files using scripting tools (Python/Pillow) before committing.
