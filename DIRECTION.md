# LinkHub — Direction & Progress Tracker

## End Vision for V1
A fully working FastAPI backend with 6 endpoints, testable in Swagger UI.
Saves links to Supabase with AI-generated summary and tags via Gemini API.

## Supported Platforms
YouTube, Facebook, GitHub, Google Drive, Google Docs, Google Sheets

## Database
Supabase — single table: `links`

## The 6 Endpoints
- [x] POST   /links/preview         → fetch metadata + AI tags
- [ ] POST   /links                 → save confirmed link
- [ ] GET    /links                 → get all links
- [ ] GET    /links/search          → search + filter by tag/platform
- [ ] GET    /links/check-duplicate → check if URL already saved
- [ ] DELETE /links/{id}            → delete a link

## Sprint Checklist
- [x] Sprint 0 — Foundation & repo
- [x] Sprint 1 — FastAPI skeleton running
- [x] Sprint 2 — Supabase connected
- [x] Sprint 3 — Metadata fetcher working
- [x] Sprint 4 — Gemini AI integration
- [x] Sprint 5 — Preview endpoint
- [ ] Sprint 6 — Save endpoint
- [ ] Sprint 7 — Duplicate detection
- [ ] Sprint 8 — Browse + search
- [ ] Sprint 9 — Delete + polish
- [ ] Sprint 10 — V1 sign-off

## V2 Considerations
- TikTok platform support (metadata + thumbnail fetching)

## Red Flags (Stop and Check If You See These)
- Adding auth before V1 is complete
- Building frontend before all endpoints work
- Hardcoding API keys anywhere
- Skipping Pydantic models for any endpoint

## Current Sprint
Sprint 6