# Bolt's Journal

## 2024-05-23 - Lazy Loading Below-Fold Images
**Learning:** Images in the "Features" section are rendered below the fold (after the intro and services strip) but were being eagerly loaded.
**Action:** Always check for `loading="lazy"` opportunities on images that are not in the initial viewport (LCP candidates). This reduces initial bandwidth usage and prioritizes critical resources.

## 2024-05-22 - Missing Ruby Runtime
**Learning:** The environment lacks a Ruby runtime, preventing local execution of `jekyll build` or `bundle install`.
**Action:** Verify changes by creating temporary HTML reproduction files or parsing source files, rather than relying on the build process.
