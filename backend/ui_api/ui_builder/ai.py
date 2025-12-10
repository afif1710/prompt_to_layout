"""
Template-based UI generation (no external AI).

- Classifies the description into one of: dashboard, auth, pricing, settings, landing
- Returns:
  - component_tree: JSON spec for the frontend renderer
  - files: React source files for the ZIP download that use the same spec + renderer
"""

from typing import Dict
import json

from .frontend_source import LAYOUT_RENDERER_CODE, TOKENS_CODE


# ---------------- GeneratedUI wrapper for ZIP ---------------- #

GENERATED_UI_TEMPLATE = """
import React from "react";
import { renderFromSpec } from "./layoutRenderer";

const SPEC = __SPEC__;

export default function GeneratedUI() {
  return (
    <div className="min-h-screen">
      {renderFromSpec(SPEC)}
    </div>
  );
}
"""


# ---------------- Classification ---------------- #

def classify_layout(description: str) -> str:
    """Very simple keyword-based classifier."""
    desc = (description or "").lower()

    # landing / marketing page detection
    if any(
        phrase in desc
        for phrase in [
            "landing page",
            "marketing site",
            "marketing page",
            "homepage",
            "home page",
            "product page",
            "hero section",
            "hero layout",
            "splash page",
        ]
    ):
        return "landing"

    if any(
        word in desc
        for word in ["login", "sign in", "signin", "signup", "auth", "authentication"]
    ):
        return "auth"

    if any(
        word in desc
        for word in ["pricing", "plans", "subscription", "billing tier", "monthly", "yearly"]
    ):
        return "pricing"

    if any(
        word in desc
        for word in ["settings", "profile", "account", "preferences", "api key", "team", "billing"]
    ):
        return "settings"

    # Default
    return "dashboard"


def _shorten(text: str, limit: int) -> str:
    if not text:
        return ""
    text = text.strip().replace("\n", " ")
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


# ---------------- Spec builder used by Preview & ZIP ---------------- #

def _build_spec(layout: str, description: str, theme: str) -> Dict:
    """
    Build the JSON spec that the frontend renderer (renderFromSpec)
    will consume.
    """
    desc_short = _shorten(description or "", 180)
    spec: Dict = {
        "layout": layout,
        "theme": theme,
        "sections": [],
    }

    if layout == "pricing":
        # One pricing-grid section with three tiers
        spec["sections"].append(
            {
                "type": "pricing-grid",
                "title": "Pricing that scales with you",
                "subtitle": desc_short
                or "Transparent pricing for modern SaaS teams.",
                "tiers": [
                    {
                        "id": "starter",
                        "name": "Starter",
                        "price": 19,
                        "interval": "month",
                        "popular": False,
                    },
                    {
                        "id": "pro",
                        "name": "Pro",
                        "price": 49,
                        "interval": "month",
                        "popular": True,
                    },
                    {
                        "id": "enterprise",
                        "name": "Enterprise",
                        "price": None,
                        "interval": "month",
                        "popular": False,
                    },
                ],
            }
        )

    elif layout == "landing":
        hero_subtitle = (
            desc_short
            or "Describe your product and generate an on-brand landing layout."
        )

        spec["sections"].append(
            {
                "type": "hero",
                "eyebrow": "AI landing layout",
                "title": "Turn a prompt into a polished landing page.",
                "subtitle": hero_subtitle,
                "bullets": [
                    "Token-based, theme-aware sections.",
                    "Structured JSON spec ready for your backend.",
                    "Layouts only, not full app scaffolding.",
                ],
                "stats": [
                    {"label": "Layouts generated", "value": "1.2k+"},
                    {"label": "Avg. setup time", "value": "3 min"},
                    {"label": "Themes", "value": "3+"},
                ],
                "primaryCta": {"label": "Generate layout"},
                "secondaryCta": {"label": "View JSON spec"},
            }
        )

        spec["sections"].append(
            {
                "type": "features",
                "title": "Crafted for modern product teams",
                "subtitle": "Swap these feature cards to match your actual value props.",
                "items": [
                    {
                        "id": "feat-tokens",
                        "name": "Design tokens first",
                        "description": "Swap themes without touching your layout or JSX.",
                    },
                    {
                        "id": "feat-schema",
                        "name": "LLM-friendly schema",
                        "description": "Ask your model to fill a predictable JSON spec.",
                    },
                    {
                        "id": "feat-preview",
                        "name": "Preview before export",
                        "description": "Validate copy and hierarchy before generating code.",
                    },
                    {
                        "id": "feat-layouts",
                        "name": "Multiple layouts",
                        "description": "Dashboard, auth, pricing, settings, and landing.",
                    },
                ],
            }
        )

        spec["sections"].append(
            {
                "type": "social-proof",
                "label": "Concept teams experimenting with AI-assisted UI flows",
                "logos": [
                    {"id": "acme", "name": "ACME"},
                    {"id": "pulse", "name": "PULSE"},
                    {"id": "zenstack", "name": "ZENSTACK"},
                    {"id": "northwind", "name": "NORTHWIND"},
                ],
            }
        )

        spec["sections"].append(
            {
                "type": "cta",
                "title": "Ready to ship your next layout?",
                "subtitle": "Use this JSON schema with your own prompts and preview themes in real time.",
                "primaryCta": {"label": "Try a prompt"},
                "secondaryCta": {"label": "Inspect schema"},
            }
        )

    elif layout == "auth":
        spec["sections"].append(
            {
                "type": "auth-layout",
                "title": "Welcome back",
                "subtitle": desc_short
                or "Modern authentication experience for your product.",
            }
        )

    elif layout == "settings":
        spec["sections"].append(
            {
                "type": "settings-layout",
                "title": "Account settings",
                "subtitle": desc_short
                or "Manage profile, team, billing and developer settings.",
                "tabs": ["Profile", "Team", "Billing", "API Keys"],
            }
        )

    else:  # dashboard
        spec["sections"].append(
            {
                "type": "dashboard-layout",
                "title": "Analytics dashboard",
                "subtitle": desc_short
                or "AI generated analytics dashboard overview.",
                "stats": [
                    {"label": "Users", "value": "1.2k"},
                    {"label": "Revenue", "value": "$42k"},
                    {"label": "Conversion", "value": "4.7%"},
                ],
            }
        )

    return spec


# --------------- Public API used by views.py --------------- #

def generate_from_description(description: str, theme: str) -> Dict:
    """
    Main entry point used by the /generate-ui endpoint.

    Returns:
    - component_tree: JSON spec for the frontend renderer
    - files: React source files for the ZIP / Code tab
    """
    layout = classify_layout(description)

    # Build spec for frontend Preview tab
    spec = _build_spec(layout, description, theme)

    # GeneratedUI.jsx that uses the same renderer + spec as the Preview
    spec_json = json.dumps(spec, indent=2)
    jsx_code = GENERATED_UI_TEMPLATE.replace("__SPEC__", spec_json)

    files = {
        "src/GeneratedUI.jsx": jsx_code,
        "src/layoutRenderer.jsx": LAYOUT_RENDERER_CODE,
        "src/theme/tokens.js": TOKENS_CODE,
    }

    return {
        "component_tree": spec,           # rich spec for Preview
        "files": files,                   # code for ZIP / Code tab
        "preview_html": "<div id='root'></div>",
        "theme": theme,
    }


def generate_from_sketch(file_obj, theme: str) -> Dict:
    # For now: treat sketch as generic dashboard
    description = "Layout inferred from sketch image."
    return generate_from_description(description, theme)
