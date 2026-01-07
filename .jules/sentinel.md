# Sentinel's Journal

## 2024-05-23 - Static Site Security Header Configuration
**Vulnerability:** Missing HTTP security headers (HSTS, X-Frame-Options, CSP, etc.) in a static site deployment.
**Learning:** For static sites deployed on platforms like Netlify, security headers must be configured in the deployment configuration file (e.g., `netlify.toml`) rather than in application code.
**Prevention:** Always check `netlify.toml`, `vercel.json`, or `firebase.json` for security header configurations in static site projects. Standard headers like HSTS and X-Content-Type-Options provide significant protection with zero code changes.

## 2024-05-23 - Reverse Tabnabbing Vulnerability
**Vulnerability:** Found `target="blank"` usage without `rel="noopener noreferrer"` in `_includes/social.html`.
**Learning:** `target="blank"` opens a new window named "blank", which is persistent and allows window manipulation just like `_blank`. Developers often mistake it for `_blank` or think it's safer, but it's not.
**Prevention:** Always use `rel="noopener noreferrer"` when using `target="_blank"` (or any named target) for external links.

## 2024-02-14 - Enhanced Permissions-Policy Header
**Vulnerability:** The default `Permissions-Policy` header was missing newer directives like `browsing-topics` and standard hardware sensor restrictions, potentially allowing unnecessary browser features.
**Learning:** Even with a good baseline `netlify.toml`, modern browser features evolve (e.g., FLoC -> Topics API), requiring regular updates to security headers.
**Prevention:** Regularly review and update `Permissions-Policy` to follow the principle of least privilege, disabling all features not explicitly needed by the application.
