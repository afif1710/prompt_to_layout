// src/layoutRenderer.jsx
// Renders different layouts from the JSON spec in result.component_tree

import React from "react";
import { getThemeTokens } from "./theme/tokens";

export function renderFromSpec(spec) {
  if (!spec) return null;

  const layout = spec.layout || "dashboard";

  switch (layout) {
    case "pricing":
      return <PricingFromSpec spec={spec} />;
    case "auth":
      return <AuthFromSpec spec={spec} />;
    case "settings":
      return <SettingsFromSpec spec={spec} />;
    case "dashboard":
    default:
      return <DashboardFromSpec spec={spec} />;
  }
}

/* ---------------- Dashboard ---------------- */

function DashboardFromSpec({ spec }) {
  const section = spec.sections?.[0] || {};
  const stats = section.stats || [
    { label: "Users", value: "1.2k" },
    { label: "Revenue", value: "$42k" },
    { label: "Conversion", value: "4.7%" },
  ];

  const t = getThemeTokens(spec.theme);

  return (
    <div className={"min-h-[420px] rounded-2xl p-6 " + (t.page || "bg-slate-950 text-slate-50")}>
      <header
        className={
          "flex items-center justify-between rounded-2xl px-4 py-3 mb-4 " +
          (t.surface || "bg-slate-950 border border-white/10")
        }
      >
        <div>
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">
            AI Generated {(spec.theme || "UI").replace("-", " ").toUpperCase()}
          </p>
          <h1 className="mt-1 text-xl font-semibold">
            {section.title || "Analytics dashboard"}
          </h1>
          {section.subtitle && (
            <p className={"mt-1 text-xs " + (t.text?.muted || "text-slate-400")}>
              {section.subtitle}
            </p>
          )}
        </div>
      </header>

      <main className="grid gap-4 md:grid-cols-[220px,1fr]">
        <aside className={"rounded-2xl p-4 " + (t.surface || "bg-white/5 border border-white/10")}>
          <p className={"text-xs font-medium uppercase " + (t.text?.label || "text-slate-400")}>
            Navigation
          </p>
          <ul className="mt-3 space-y-1 text-sm">
            <li className="rounded-xl bg-white/10 px-3 py-2">Overview</li>
            <li className="rounded-xl px-3 py-2 hover:bg-white/5">Analytics</li>
            <li className="rounded-xl px-3 py-2 hover:bg-white/5">Settings</li>
          </ul>
        </aside>

        <section className="space-y-4">
          <div className="grid gap-3 md:grid-cols-3">
            {stats.map((stat) => (
              <div
                key={stat.label}
                className={
                  "rounded-2xl p-4 " +
                  (t.card ||
                    "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/50")
                }
              >
                <p className={"text-xs " + (t.text?.muted || "text-slate-400")}>{stat.label}</p>
                <p className={"mt-2 text-2xl font-semibold " + (t.text?.primary || "")}>
                  {stat.value}
                </p>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

/* ---------------- Auth ---------------- */

function AuthFromSpec({ spec }) {
  const section = spec.sections?.[0] || {};
  const title = section.title || "Welcome back";
  const subtitle =
    section.subtitle || "Modern authentication experience for your product.";

  const t = getThemeTokens(spec.theme);

  return (
    <div
      className={
        "min-h-[420px] rounded-2xl p-6 flex items-center justify-center " +
        (t.page || "bg-slate-950 text-slate-50")
      }
    >
      <div
        className={
          "grid w-full max-w-5xl gap-8 rounded-3xl p-8 md:grid-cols-[1.2fr,1fr] " +
          (t.surface ||
            "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/60 backdrop-blur-2xl")
        }
      >
        <section className="flex flex-col justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.2em] text-slate-400">
              AI Generated {(spec.theme || "UI").replace("-", " ").toUpperCase()}
            </p>
            <h1 className="mt-2 text-3xl font-semibold">{title}</h1>
            <p className={"mt-3 max-w-md text-sm " + (t.text?.muted || "text-slate-300")}>
              {subtitle}
            </p>
          </div>
        </section>

        <section
          className={
            "rounded-2xl p-6 shadow-inner " +
            (t.card || "bg-slate-950/60 border border-white/10 backdrop-blur-xl")
          }
        >
          <form className="space-y-4">
            <div>
              <label className={"text-xs font-medium " + (t.text?.label || "text-slate-300")}>
                Email
              </label>
              <input
                type="email"
                className="mt-1 w-full rounded-xl border border-white/10 bg-slate-900/80 px-3 py-2 text-sm outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-400"
                placeholder="you@example.com"
              />
            </div>
            <div>
              <label className={"text-xs font-medium " + (t.text?.label || "text-slate-300")}>
                Password
              </label>
              <input
                type="password"
                className="mt-1 w-full rounded-xl border border-white/10 bg-slate-900/80 px-3 py-2 text-sm outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-400"
                placeholder="••••••••"
              />
            </div>
            <div className={"flex items-center justify-between text-xs " + (t.text?.muted || "text-slate-400")}>
              <label className="flex items-center gap-2">
                <input
                  type="checkbox"
                  className="h-3 w-3 rounded border-white/20 bg-slate-900"
                />
                <span>Remember me</span>
              </label>
              <button type="button" className="text-emerald-300 hover:text-emerald-200">
                Forgot password?
              </button>
            </div>
            <button
              type="submit"
              className={"mt-2 w-full rounded-xl px-3 py-2 text-sm font-medium " + (t.button?.primary || "bg-emerald-500 text-slate-950 hover:bg-emerald-400")}
            >
              Sign in
            </button>
          </form>
        </section>
      </div>
    </div>
  );
}

/* ---------------- Pricing ---------------- */

function PricingFromSpec({ spec }) {
  const section = spec.sections?.[0] || {};
  const tiers = section.tiers || [];
  const title = section.title || "Pricing that scales with you";
  const subtitle =
    section.subtitle ||
    "Transparent pricing for modern SaaS teams. Change this text to see different copy.";

  const t = getThemeTokens(spec.theme);

  return (
    <div
      className={
        "min-h-[420px] rounded-2xl px-6 py-8 " +
        (t.page || "bg-slate-950 text-slate-50")
      }
    >
      <div
        className={
          "mx-auto max-w-5xl text-center rounded-3xl p-6 " +
          (t.surface || "bg-slate-950 border border-white/10")
        }
      >
        <p className="text-xs uppercase tracking-[0.2em] text-slate-400">
          AI Generated {(spec.theme || "UI").replace("-", " ").toUpperCase()}
        </p>
        <h1 className="mt-2 text-3xl font-semibold">{title}</h1>
        {subtitle && (
          <p className={"mt-2 text-sm " + (t.text?.muted || "text-slate-400")}>
            {subtitle}
          </p>
        )}
      </div>

      <div className="mx-auto mt-8 grid max-w-5xl gap-4 md:grid-cols-3">
        {tiers.map((tier) => (
          <div
            key={tier.id || tier.name}
            className={[
              "rounded-3xl p-6 text-left transition-transform",
              t.card ||
                "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/50",
              tier.popular
                ? "scale-[1.04] border-emerald-400/70 ring-2 ring-emerald-400/70 bg-gradient-to-b from-emerald-400/30 via-emerald-500/15 to-slate-950/70"
                : "",
            ].join(" ")}
          >
            <div className="flex items-baseline justify-between">
              <h2 className="text-sm font-semibold">{tier.name}</h2>
              {tier.popular && (
                <span className="rounded-full bg-emerald-400 text-emerald-950 px-3 py-0.5 text-[11px] font-semibold tracking-wide shadow-md shadow-emerald-500/40 border border-emerald-300">
                  MOST POPULAR
                </span>
              )}
            </div>
            <p className="mt-3 text-2xl font-semibold">
              {tier.price != null ? `$${tier.price}` : "Custom"}
              <span className={"text-xs font-normal " + (t.text?.muted || "text-slate-400")}>
                {tier.price != null ? ` / ${tier.interval || "month"}` : ""}
              </span>
            </p>
            <ul className={"mt-4 space-y-2 text-xs " + (t.text?.bullet || "text-slate-200")}>
              <li>✔ Unlimited projects</li>
              <li>✔ Team workspaces</li>
              <li>✔ Advanced analytics</li>
              <li>✔ Priority support</li>
            </ul>

            <button
              className={[
                "mt-5 w-full rounded-xl px-3 py-2 text-sm font-medium",
                tier.popular
                  ? (t.button?.primary || "bg-emerald-500 text-slate-950 hover:bg-emerald-400")
                  : (t.button?.secondary || "bg-white/10 text-slate-50 hover:bg-white/15"),
              ].join(" ")}
            >
              {tier.id === "enterprise" ? "Contact sales" : "Start free trial"}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ---------------- Settings ---------------- */

function SettingsFromSpec({ spec }) {
  const section = spec.sections?.[0] || {};
  const tabs = section.tabs || ["Profile", "Team", "Billing", "API Keys"];
  const title = section.title || "Account settings";
  const subtitle =
    section.subtitle ||
    "Manage profile, team, billing and developer settings from a single panel.";

  const t = getThemeTokens(spec.theme);

  return (
    <div
      className={
        "min-h-[420px] rounded-2xl px-6 py-8 " +
        (t.page || "bg-slate-950 text-slate-50")
      }
    >
      <div
        className={
          "mx-auto max-w-6xl rounded-3xl p-6 " +
          (t.surface ||
            "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/60 backdrop-blur-xl")
        }
      >
        <header className="border-b border-white/10 pb-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">
            AI Generated {(spec.theme || "UI").replace("-", " ").toUpperCase()}
          </p>
          <h1 className="mt-2 text-2xl font-semibold">{title}</h1>
          {subtitle && (
            <p className={"mt-1 max-w-2xl text-sm " + (t.text?.muted || "text-slate-400")}>
              {subtitle}
            </p>
          )}
        </header>

        <div className="mt-6 grid gap-6 md:grid-cols-[220px,1fr]">
          <nav className="space-y-1 text-sm">
            {tabs.map((item, index) => {
              const base =
                "flex w-full items-center justify-between rounded-xl px-3 py-2 text-left";
              const active = t.nav?.active || "bg-emerald-500/15 text-slate-50";
              const inactive = t.nav?.inactive || "text-slate-300 hover:bg-white/5";

              return (
                <button
                  key={item}
                  className={[base, index === 2 ? active : inactive].join(" ")}
                >
                  <span>{item}</span>
                  {index === 2 && (
                    <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
                  )}
                </button>
              );
            })}
          </nav>

          <section className="flex flex-col gap-4">
            <div
              className={
                "rounded-2xl p-5 " +
                (t.card || "bg-slate-950/60 border border-white/10 shadow-inner")
              }
            >
              <h2 className="text-sm font-medium">Billing overview</h2>
              <p className={"mt-1 text-xs " + (t.text?.muted || "text-slate-400")}>
                Current plan, payment method and upcoming invoice.
              </p>
              <div className="mt-4 grid gap-4 md:grid-cols-3 text-xs">
                <div>
                  <p className={t.text?.label || "text-slate-400"}>Plan</p>
                  <p className={"mt-1 font-semibold " + (t.text?.primary || "text-slate-100")}>
                    Pro Annual
                  </p>
                </div>
                <div>
                  <p className={t.text?.label || "text-slate-400"}>Next invoice</p>
                  <p className={"mt-1 font-semibold " + (t.text?.primary || "text-slate-100")}>
                    $588 · 01 Aug 2025
                  </p>
                </div>
                <div>
                  <p className={t.text?.label || "text-slate-400"}>Payment method</p>
                  <p className={"mt-1 font-semibold " + (t.text?.primary || "text-slate-100")}>
                    Visa •••• 4242
                  </p>
                </div>
              </div>
            </div>

            <footer
              className={
                "flex justify-end gap-2 border-t border-white/5 px-4 py-3 text-xs rounded-2xl " +
                (t.card ? "" : "bg-slate-950/60")
              }
            >
              <button
                className={
                  "rounded-xl px-3 py-1.5 font-medium " +
                  (t.button?.ghost || "border border-white/15 text-slate-300 hover:bg-white/5")
                }
              >
                Cancel
              </button>
              <button
                className={
                  "rounded-xl px-3 py-1.5 font-medium " +
                  (t.button?.primary || "bg-emerald-500 text-slate-950 hover:bg-emerald-400")
                }
              >
                Save changes
              </button>
            </footer>
          </section>
        </div>
      </div>
    </div>
  );
}
