# Palette's Journal

## 2024-05-23 - Accessibility Improvements
**Learning:** `target="blank"` is often used incorrectly instead of `target="_blank"`, and it's important to include `rel="noopener noreferrer"` for security and performance when opening links in new tabs. Also, ensuring `aria-current="page"` is present on active navigation links is a simple but high-impact accessibility win.
**Action:** Always check `target` attributes and active states in navigation menus during accessibility reviews.
## 2024-05-23 - Skip to Content & Utility Classes
**Learning:** Adding a "Skip to content" link was straightforward using Bootstrap 5's `visually-hidden-focusable` utility. However, to ensure it overlays sticky headers properly, I needed `position-absolute` and a high z-index. The default `z-index` utilities were insufficient (max 3), so an inline style `z-index: 2000` was necessary to guarantee visibility over potential sticky elements (often z-index 1000+).
**Action:** For future a11y overlays, check z-index context of headers first. If existing utilities are insufficient, inline styles or a dedicated utility class in `_sass` is acceptable for critical a11y features.
