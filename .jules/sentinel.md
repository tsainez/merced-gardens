## 2024-05-23 - Static Site Security Header Configuration
**Vulnerability:** Missing HTTP security headers (HSTS, X-Frame-Options, CSP, etc.) in a static site deployment.
**Learning:** For static sites deployed on platforms like Netlify, security headers must be configured in the deployment configuration file (e.g., `netlify.toml`) rather than in application code.
**Prevention:** Always check `netlify.toml`, `vercel.json`, or `firebase.json` for security header configurations in static site projects. Standard headers like HSTS and X-Content-Type-Options provide significant protection with zero code changes.
