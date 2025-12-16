## 2024-05-23 - Lazy Loading Below-Fold Images
**Learning:** Images in the "Features" section are rendered below the fold (after the intro and services strip) but were being eagerly loaded.
**Action:** Always check for `loading="lazy"` opportunities on images that are not in the initial viewport (LCP candidates). This reduces initial bandwidth usage and prioritizes critical resources.
