### 2. `docs/browser_policy.md`
Enterprise projects mein "safe browsing" dikhana zaroori hota hai. Yeh file wahi kaam karegi:
```markdown
# Browser Policy & Safety Guidelines

To ensure safe, controlled, and compliant web scraping, this agent strictly adheres to the following policies:

1. **Domain Allowlisting:** The Playwright instance is restricted to target only predefined domains (e.g., `makemytrip.com`).
2. **Rate Limiting:** Automated interactions include natural delays to mimic human behavior and avoid server overload.
3. **No Sensitive Data Storage:** No user session tokens, login credentials, or PII (Personally Identifiable Information) are stored during the extraction phase.
4. **Visibility:** All browser actions are performed in a traceable environment, and failures (e.g., captchas, blocked pages) are surfaced directly to the frontend UI rather than silently failing.