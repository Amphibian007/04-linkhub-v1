# LinkHub — Claude Context File

## What This Project Is
A link classifier and organizer REST API. Users save URLs, the app
auto-classifies the platform, fetches metadata, generates an AI summary,
and suggests tags using Google Gemini API.

## Tech Stack
- Python + FastAPI
- Supabase (Postgres database)
- Google AI Studio — Gemini 2.5 Flash (AI layer)
- Hosted on Render or Railway
- Frontend: Next.js PWA (separate repo)

## Folder Structure
- app/routers/ → all API route files
- app/services/ → business logic (metadata, AI, supabase)
- app/models/ → Pydantic request/response models
- app/main.py → FastAPI app entry point

## Coding Conventions
- All functions must be async
- All endpoints use Pydantic models for input and output
- No hardcoded secrets — always use environment variables
- Every endpoint must have a docstring
- Return proper HTTP status codes always

## Environment Variables Required
- SUPABASE_URL
- SUPABASE_ANON_KEY
- GEMINI_API_KEY

## What NOT To Build Yet
- No auth endpoints (V2)
- No frontend (separate repo)
- No sharing features (V3)
- No CLI (optional later)

## Current Version
V1 — solo use, no auth, core endpoints only