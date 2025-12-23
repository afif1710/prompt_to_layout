# Prompt_to_layout

Prompt_to_layout is a small layout playground: it turns a user prompt into a JSON layout spec, then renders a themed React + Tailwind preview using design tokens.

This is not a full “production UI code generator” yet — the goal is to explore layout ideas quickly while keeping styling consistent through a token system.

---

## What it does

- Prompt → JSON layout spec
- JSON spec → React layout preview (renderer)
- Theme switching via semantic design tokens (single source of truth)

---

## Tech

- React + Vite (frontend)
- Tailwind CSS (styling)
- Token-based theming (semantic tokens)
- Python backend may exist in the repo, but it’s not required for theme/layout work

---

## Current layouts

- Dashboard
- Auth
- Pricing
- Settings

---

## Themes

- premium-dark
- minimal-light
- frosted-glass

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

- frontend/src/theme/tokens.js
  - All theme tokens live here (single source of truth).
- frontend/src/layoutRenderer.jsx
  - Renders from a spec and applies tokens.
- frontend/src/components/LayoutShell.jsx
  - Editor/studio shell (kept consistent; not themed by preview theme).
- frontend/src/App.jsx
  - Passes theme to the preview (not to the shell).

---

## Run locally

cd frontend
npm install
npm run dev
