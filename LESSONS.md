# LinkHub — Lessons & Gotchas

A running log of real errors hit during development, why they happened, and how to avoid them.
Updated after every sprint.

---

## Sprint 4 — Gemini AI Integration

### 1. Always read existing files before adding to them
Leftover incomplete code (`@app.get("/test-metadata")` with no function) caused a startup crash.
**Rule:** Before touching any file in a new sprint, read it top to bottom first.

### 2. Verify third-party SDK package names before writing imports
Used `google-generativeai` (deprecated) instead of `google-genai` (current).
AI models have outdated knowledge of SDK package names — always check the official GitHub README.
**Rule:** For any Google/OpenAI/Anthropic SDK, confirm the current package name before writing a single import.

### 3. Install first, then update code — never the other way around
Switched the import to `google.genai` before running `pip install google-genai`.
Server crashed on startup because the package didn't exist yet.
**Rule:** When changing a package, the order is always: `pip install` → then update the code.

### 4. Never use preview model IDs from memory
Used `gemini-2.5-flash-preview-04-17` — a preview ID tied to a release date that had expired.
Got a 404 from the API.
**Rule:** Preview model IDs (with dates in the name) expire. Always verify the current ID in Google AI Studio or the provider's model list. Use stable IDs where possible.

### 5. Check free tier quota per model, not just per provider
Switched to `gemini-2.0-flash` — got `limit: 0` because that model has no free tier quota on this API key.
**Rule:** Free tier availability varies by model and region. Verify quota for your specific key before committing to a model.

---

## Instructions for Claude (add to CLAUDE.md)

Before writing any code in a new sprint:
- Read every existing file before adding to it
- For any third-party SDK — verify the current package name from the official GitHub README
- For any AI model ID — verify it exists by checking the provider's current model list
- When changing a package — install first, then update code
- Before starting a sprint — confirm all existing files are clean and complete
