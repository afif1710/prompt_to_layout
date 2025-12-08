"""
Template-based UI generation (no external AI).

- Classifies the description into one of: dashboard, auth, pricing, settings
- Returns a JSX file (src/GeneratedUI.jsx) built from hand-written templates
"""

from typing import Dict


# ---------------- Classification ---------------- #

def classify_layout(description: str) -> str:
    """Very simple keyword-based classifier."""
    desc = (description or "").lower()

    if any(word in desc for word in ["login", "sign in", "signin", "signup", "auth", "authentication"]):
        return "auth"

    if any(word in desc for word in ["pricing", "plans", "subscription", "billing tier", "monthly", "yearly"]):
        return "pricing"

    if any(word in desc for word in ["settings", "profile", "account", "preferences", "api key", "team", "billing"]):
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


# ---------------- JSX Templates ---------------- #

# NOTE: These are plain triple-quoted strings, NOT f-strings.
# React { ... } syntax is safe here because Python does not treat
# braces specially in normal strings.
# We later replace __DESC__ and __THEME__ in Python.

DASHBOARD_TEMPLATE = """
import React from "react";
import { motion } from "framer-motion";

export default function GeneratedUI() {
  const description = "__DESC__";

  const stats = [
    { label: "Users", value: "1.2k" },
    { label: "Revenue", value: "$42k" },
    { label: "Conversion", value: "4.7%" }
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 p-8">
      <div className="mx-auto max-w-5xl rounded-3xl border border-white/10 bg-white/5 shadow-xl shadow-slate-950/60 backdrop-blur-xl">
        <header className="flex items-center justify-between border-b border-white/10 px-6 py-4">
          <div>
            <p className="text-xs uppercase tracking-[0.2em] text-slate-400">AI Generated __THEME__</p>
            <h1 className="mt-1 text-xl font-semibold">Analytics dashboard</h1>
            <p className="mt-1 text-xs text-slate-400">{description}</p>
          </div>
        </header>
        <main className="grid gap-4 px-6 py-4 md:grid-cols-[220px,1fr]">
          <aside className="rounded-2xl border border-white/10 bg-white/5 p-4">
            <p className="text-xs font-medium uppercase text-slate-400">Navigation</p>
            <ul className="mt-3 space-y-1 text-sm">
              <li className="rounded-xl bg-white/10 px-3 py-2">Overview</li>
              <li className="rounded-xl px-3 py-2 hover:bg-white/5">Analytics</li>
              <li className="rounded-xl px-3 py-2 hover:bg-white/5">Settings</li>
            </ul>
          </aside>
          <section className="space-y-4">
            <div className="grid gap-3 md:grid-cols-3">
              {stats.map((stat, index) => (
                <motion.div
                  key={stat.label}
                  className="rounded-2xl border border-white/10 bg-white/5 p-4"
                  initial={{ opacity: 0, y: 8 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                >
                  <p className="text-xs text-slate-400">{stat.label}</p>
                  <p className="mt-2 text-2xl font-semibold">{stat.value}</p>
                </motion.div>
              ))}
            </div>
          </section>
        </main>
      </div>
    </div>
  );
}
"""

AUTH_TEMPLATE = """
import React from "react";

export default function GeneratedUI() {
  const description = "__DESC__";

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 flex items-center justify-center px-6 py-10 text-slate-50">
      <div className="grid w-full max-w-5xl gap-8 rounded-3xl border border-white/10 bg-white/5 p-8 shadow-xl shadow-slate-950/60 backdrop-blur-2xl md:grid-cols-[1.2fr,1fr]">
        <section className="flex flex-col justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.2em] text-slate-400">AI Generated __THEME__</p>
            <h1 className="mt-2 text-3xl font-semibold">Welcome back</h1>
            <p className="mt-3 max-w-md text-sm text-slate-300">
              {description}
            </p>
          </div>
        </section>

        <section className="rounded-2xl border border-white/10 bg-slate-950/60 p-6 shadow-inner">
          <form className="space-y-4">
            <div>
              <label className="text-xs font-medium text-slate-300">Email</label>
              <input
                type="email"
                className="mt-1 w-full rounded-xl border border-white/10 bg-slate-900/80 px-3 py-2 text-sm outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-400"
                placeholder="you@example.com"
              />
            </div>
            <div>
              <label className="text-xs font-medium text-slate-300">Password</label>
              <input
                type="password"
                className="mt-1 w-full rounded-xl border border-white/10 bg-slate-900/80 px-3 py-2 text-sm outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-400"
                placeholder="••••••••"
              />
            </div>
            <div className="flex items-center justify-between text-xs text-slate-400">
              <label className="flex items-center gap-2">
                <input type="checkbox" className="h-3 w-3 rounded border-white/20 bg-slate-900" />
                <span>Remember me</span>
              </label>
              <button type="button" className="text-emerald-300 hover:text-emerald-200">
                Forgot password?
              </button>
            </div>
            <button
              type="submit"
              className="mt-2 w-full rounded-xl bg-emerald-500 px-3 py-2 text-sm font-medium text-slate-950 shadow-lg shadow-emerald-500/40 hover:bg-emerald-400"
            >
              Sign in
            </button>
          </form>
        </section>
      </div>
    </div>
  );
}
"""

PRICING_TEMPLATE = """
import React from "react";

export default function GeneratedUI() {
  const description = "__DESC__";

  const tiers = [
    { name: "Starter", price: "$19", note: "/ month" },
    { name: "Pro", price: "$49", note: "/ month", popular: true },
    { name: "Enterprise", price: "Custom", note: "" }
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 px-6 py-12">
      <div className="mx-auto max-w-5xl text-center">
        <p className="text-xs uppercase tracking-[0.2em] text-slate-400">AI Generated __THEME__</p>
        <h1 className="mt-2 text-3xl font-semibold">Pricing that scales with you</h1>
        <p className="mt-2 text-sm text-slate-400">
          {description}
        </p>
      </div>

      <div className="mx-auto mt-8 grid max-w-5xl gap-4 md:grid-cols-3">
        {tiers.map((tier, index) => (
          <div
            key={tier.name}
            className={[
              "rounded-3xl border border-white/10 bg-white/5 p-6 text-left shadow-xl shadow-slate-950/50",
              tier.popular ? "scale-[1.03] border-emerald-400/60 bg-gradient-to-b from-emerald-500/20 to-slate-950/60" : ""
            ].join(" ")}
          >
            <div className="flex items-baseline justify-between">
              <h2 className="text-sm font-semibold">{tier.name}</h2>
              {tier.popular && (
                <span className="rounded-full bg-emerald-500/20 px-2 py-0.5 text-[10px] text-emerald-200">
                  Most popular
                </span>
              )}
            </div>
            <p className="mt-3 text-2xl font-semibold">
              {tier.price}
              <span className="text-xs font-normal text-slate-400"> {tier.note}</span>
            </p>
            <ul className="mt-4 space-y-2 text-xs text-slate-200">
              <li>✔ Unlimited projects</li>
              <li>✔ Team workspaces</li>
              <li>✔ Advanced analytics</li>
              <li>✔ Priority support</li>
            </ul>
            <button
              className={[
                "mt-5 w-full rounded-xl px-3 py-2 text-sm font-medium",
                tier.popular ? "bg-emerald-500 text-slate-950 hover:bg-emerald-400" : "bg-white/10 text-slate-50 hover:bg-white/15"
              ].join(" ")}
            >
              {tier.name === "Enterprise" ? "Contact sales" : "Start free trial"}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
"""

SETTINGS_TEMPLATE = """
import React from "react";

export default function GeneratedUI() {
  const description = "__DESC__";

  const tabs = ["Profile", "Team", "Billing", "API Keys"];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 px-6 py-10">
      <div className="mx-auto max-w-6xl rounded-3xl border border-white/10 bg-white/5 p-8 shadow-xl shadow-slate-950/60 backdrop-blur-xl">
        <header className="border-b border-white/10 pb-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">AI Generated __THEME__</p>
          <h1 className="mt-2 text-2xl font-semibold">Account settings</h1>
          <p className="mt-1 max-w-2xl text-sm text-slate-400">
            {description}
          </p>
        </header>

        <div className="mt-6 grid gap-6 md:grid-cols-[220px,1fr]">
          <nav className="space-y-1 text-sm">
            {tabs.map((item, index) => (
              <button
                key={item}
                className={[
                  "flex w-full items-center justify-between rounded-xl px-3 py-2 text-left",
                  index === 2 ? "bg-white/15 text-slate-50" : "text-slate-300 hover:bg-white/5"
                ].join(" ")}
              >
                <span>{item}</span>
                {index === 2 && <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />}
              </button>
            ))}
          </nav>

          <section className="flex flex-col gap-4">
            <div className="rounded-2xl border border-white/10 bg-slate-950/60 p-5">
              <h2 className="text-sm font-medium">Billing overview</h2>
              <p className="mt-1 text-xs text-slate-400">
                Current plan, payment method and upcoming invoice.
              </p>
              <div className="mt-4 grid gap-4 md:grid-cols-3 text-xs">
                <div>
                  <p className="text-slate-400">Plan</p>
                  <p className="mt-1 font-semibold text-slate-100">Pro Annual</p>
                </div>
                <div>
                  <p className="text-slate-400">Next invoice</p>
                  <p className="mt-1 font-semibold text-slate-100">$588 · 01 Aug 2025</p>
                </div>
                <div>
                  <p className="text-slate-400">Payment method</p>
                  <p className="mt-1 font-semibold text-slate-100">Visa •••• 4242</p>
                </div>
              </div>
            </div>

            <footer className="flex justify-end gap-2 border-t border-white/5 bg-slate-950/60 px-4 py-3 text-xs">
              <button className="rounded-xl border border-white/15 px-3 py-1.5 text-slate-300 hover:bg-white/5">
                Cancel
              </button>
              <button className="rounded-xl bg-emerald-500 px-3 py-1.5 font-medium text-slate-950 hover:bg-emerald-400">
                Save changes
              </button>
            </footer>
          </section>
        </div>
      </div>
    </div>
  );
}
"""


def _render_template(template: str, description: str, theme: str) -> str:
    """Fill in placeholders in a JSX template."""
    desc_short = _shorten(description or "", 180)
    theme_label = (theme or "").replace("-", " ").title() or "UI"
    code = template.replace("__DESC__", desc_short)
    code = code.replace("__THEME__", theme_label)
    return code


# --------------- Public API used by views.py --------------- #
def _build_spec(layout: str, description: str, theme: str, complexity: int) -> Dict:
    """
    Build the JSON spec that the frontend renderer (renderFromSpec)
    will consume. This replaces the old simple component_tree.
    """
    desc_short = _shorten(description or "", 180)
    spec: Dict = {
        "layout": layout,
        "theme": theme,
        "complexity": complexity,
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


def generate_from_description(description: str, theme: str, complexity: int) -> Dict:
    """
    Main entry point used by the /generate-ui endpoint.

    Now returns:
    - component_tree: JSON spec for the frontend renderer
    - files: JSX string for download/Code tab (unchanged)
    """
    layout = classify_layout(description)

    # Build spec for frontend Preview tab
    spec = _build_spec(layout, description, theme, complexity)

    # Still generate JSX from templates for Code/ZIP
    if layout == "auth":
        jsx_code = _render_template(AUTH_TEMPLATE, description, theme)
    elif layout == "pricing":
        jsx_code = _render_template(PRICING_TEMPLATE, description, theme)
    elif layout == "settings":
        jsx_code = _render_template(SETTINGS_TEMPLATE, description, theme)
    else:
        jsx_code = _render_template(DASHBOARD_TEMPLATE, description, theme)

    files = {"src/GeneratedUI.jsx": jsx_code}

    return {
        "component_tree": spec,            # <‑‑ now the rich spec
        "files": files,
        "preview_html": "<div id='root'></div>",
        "theme": theme,
        "complexity": complexity,
    }


def generate_from_sketch(file_obj, theme: str, complexity: int) -> Dict:
    # For now: treat sketch as generic dashboard
    description = "Layout inferred from sketch image."
    return generate_from_description(description, theme, complexity)
