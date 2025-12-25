# prompt_to_layout

**prompt_to_layout** is a layout playground: it turns a user prompt into a JSON layout spec, then renders a themed React + Tailwind preview using semantic design tokens.

This is not a full “production UI code generator” yet — the goal is to explore layout ideas quickly while keeping styling consistent through a token system.

---

## What it does

- Prompt → JSON layout spec (currently template-based)
- JSON spec → React layout preview (renderer)
- Theme switching via semantic design tokens (single source of truth)

---

## Tech

- React + Vite (frontend)
- Tailwind CSS (styling)
- Token-based theming (semantic tokens)
- Django backend (API) for layout generation
- PostgreSQL (used in the full-stack Docker setup)

---

## Current layouts (v1 templates)

The generator currently maps supported prompt patterns to these 5 curated templates:

- Dashboard
- Auth
- Pricing
- Settings
- Landing page

---

## Themes

- premium-dark
- minimal-light
- frosted-glass
- soft-pastel
- high-contrast

---

## Token system (single source of truth)

Layouts/components should use semantic tokens only (no hard-coded colors inside layout components).

### Surfaces

- page
- surface
- card

### Text

- text.primary
- text.secondary
- text.muted
- text.label
- text.bullet

### Buttons

- button.primary
- button.secondary
- button.ghost

### Navigation

- nav.active
- nav.inactive

---

## Key files

- `frontend/src/theme/tokens.js`
  - All theme tokens live here (single source of truth).
- `frontend/src/layoutRenderer.jsx`
  - Renders from a spec and applies tokens.
- `frontend/src/components/LayoutShell.jsx`
  - Editor/studio shell (kept consistent; not themed by preview theme).
- `frontend/src/App.jsx`
  - Passes theme to the preview (not to the shell).

---

## Run locally (frontend only)

cd frontend
npm install
npm run dev

> Note: Prompt → layout generation requires the backend. Running only the frontend will limit you to whatever preview/demo behavior the UI provides.

---

## Docker (full stack)

This repo includes a full-stack `docker compose` setup.

### Run the full stack

docker compose up -d --build

### Stop

docker compose down

### Services

- Frontend: http://localhost:5173
- Backend: http://localhost:8000

---

## Export / “Download ZIP” (current)

The ZIP export is developer-focused right now. It may require manual steps (install deps / run locally) to view the exported layout outside the in-app preview.

---

## Limitations / roadmap

- Expand beyond 5 templates (more layouts + better prompt coverage).
- Better scaffolding + clearer docs.
- Improve the prompt → spec logic and add validation for the JSON schema.
- Make the upload sketch feature functioning.
- User authentication + Saving layout feature

---

## Docker Hub images

- Frontend: https://hub.docker.com/r/afif1710/aiui-frontend
- Backend: https://hub.docker.com/r/afif1710/aiui-backend

---

## Documentation evidence

- `docs/docker-commands.md`
- `docs/image-analysis.md`
- `docs/dockerhub-push.md`
