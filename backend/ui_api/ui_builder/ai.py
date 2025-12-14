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

  # Landing / marketing page detection
  landing_keywords = [
      "landing page",
      "landing site",
      "landing webpage",
      "landing website",
      "landing ui",
      "marketing site",
      "marketing page",
      "homepage",
      "home page",
      "product page",
      "product site",
      "hero section",
      "hero layout",
      "hero banner",
      "splash page",
      "promo page",
      "promo site",
      "campaign page",
      "campaign landing",
      "saas landing",
      "startup landing",
      "coming soon",
      "waitlist page",
      "one page site",
      "single page site",
      "sales page",
      "marketing homepage",
  ]
  if any(phrase in desc for phrase in landing_keywords):
      return "landing"

  # Auth / sign-in / sign-up flows
  auth_keywords = [
      "login",
      "log in",
      "log-in",
      "log on",
      "log-on",
      "signin",
      "sign in",
      "sign-in",
      "signup",
      "sign up",
      "sign-up",
      "register",
      "registration",
      "create account",
      "account creation",
      "auth",
      "authentication",
      "forgot password",
      "reset password",
      "change password",
      "password reset",
      "two factor",
      "2fa",
      "otp verification",
      "verification code",
      "magic link",
      "passwordless",
      "sso",
      "single sign on",
      "single sign-on",
      "oauth",
  ]
  if any(phrase in desc for phrase in auth_keywords):
      return "auth"

  # Pricing / plans / tiers
  pricing_keywords = [
      "pricing",
      "pricing page",
      "pricing table",
      "pricing grid",
      "pricing plans",
      "price plans",
      "plans and pricing",
      "plans page",
      "plan tiers",
      "tiers",
      "tiered plans",
      "subscription",
      "subscriptions",
      "subscription plans",
      "billing tier",
      "billing tiers",
      "billing plans",
      "monthly pricing",
      "yearly pricing",
      "per month",
      "per user",
      "per seat",
      "compare plans",
      "pricing comparison",
      "upgrade plan",
      "downgrade plan",
      "choose a plan",
      "select a plan",
  ]
  if any(phrase in desc for phrase in pricing_keywords):
      return "pricing"

  # Settings / account / profile / team / billing / API keys
  settings_keywords = [
      "settings",
      "profile settings",
      "account settings",
      "user settings",
      "workspace settings",
      "organization settings",
      "organisation settings",
      "org settings",
      "team settings",
      "preferences",
      "user preferences",
      "account page",
      "account center",
      "profile page",
      "edit profile",
      "team management",
      "manage team",
      "team members",
      "members and roles",
      "roles and permissions",
      "role management",
      "permissions",
      "access control",
      "billing",
      "billing settings",
      "billing & invoices",
      "invoices",
      "payment methods",
      "subscription settings",
      "api key",
      "api keys",
      "api token",
      "developer settings",
      "developer options",
      "integrations",
      "connected apps",
      "integration settings",
      "notification settings",
      "notifications",
      "security settings",
      "security center",
  ]
  if any(phrase in desc for phrase in settings_keywords):
      return "settings"

  # Dashboard / analytics / admin / reporting
  dashboard_keywords = [
      "dashboard",
      "analytics dashboard",
      "analytics",
      "reporting dashboard",
      "reporting",
      "kpi dashboard",
      "kpis",
      "metrics",
      "metric overview",
      "stats page",
      "statistics page",
      "stats overview",
      "overview page",
      "overview dashboard",
      "admin panel",
      "admin dashboard",
      "control panel",
      "management console",
      "monitoring",
      "monitoring view",
      "insights",
      "performance overview",
      "traffic chart",
      "charts and graphs",
      "data visualization",
  ]
  if any(phrase in desc for phrase in dashboard_keywords):
      return "dashboard"

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
