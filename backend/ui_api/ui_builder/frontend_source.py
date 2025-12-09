# backend/ui_api/ui_builder/frontend_source.py
# Copies of the frontend renderer and tokens for ZIP export.

LAYOUT_RENDERER_CODE = """
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
    case "landing":
      return <LandingFromSpec spec={spec} />;
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




/* ---------------- Landing ---------------- */

function LandingFromSpec({ spec }) {
  const t = getThemeTokens(spec.theme);

  const isLightTheme =
  spec.theme === "minimal-light" || spec.theme === "soft-pastel";
  
  const sections = spec.sections || [];

  const hero =
    sections.find((s) => s.type === "hero") || {
      eyebrow: "AI Generated Layout",
      title: "Turn a prompt into a polished landing page.",
      subtitle:
        "Describe your product once. Get a themed React/Tailwind layout you can refine, test, and ship.",
      bullets: [
        "Token-based, theme-aware sections",
        "Structured JSON spec for your backend",
        "Layouts only, no full app scaffold (yet)",
      ],
      stats: [
        { label: "Layouts generated", value: "1.2k+" },
        { label: "Avg. setup time", value: "3 min" },
        { label: "Themes", value: "3+" },
      ],
      primaryCta: { label: "Generate layout" },
      secondaryCta: { label: "View JSON spec" },
    };

  const features =
    sections.find((s) => s.type === "features") || {
      title: "Crafted for modern product teams",
      subtitle:
        "Show how your product helps. Swap these items to match your actual value props.",
      items: [
        {
          id: "features-1",
          name: "Design tokens first",
          description: "Swap themes without touching your layout or JSX.",
        },
        {
          id: "features-2",
          name: "LLM-friendly schema",
          description: "Ask your model to fill a predictable JSON spec.",
        },
        {
          id: "features-3",
          name: "Preview before export",
          description: "Validate copy and hierarchy before generating code.",
        },
        {
          id: "features-4",
          name: "Multiple layouts",
          description: "Dashboard, auth, pricing, settings, and landing.",
        },
      ],
    };

  const socialProof =
    sections.find((s) => s.type === "social-proof") || {
      label: "Concept brands using AI-assisted UI flows",
      logos: [
        { id: "acme", name: "ACME" },
        { id: "pulse", name: "PULSE" },
        { id: "zenstack", name: "ZENSTACK" },
        { id: "northwind", name: "NORTHWIND" },
      ],
    };

  const cta =
    sections.find((s) => s.type === "cta") || {
      title: "Ready to ship your next layout?",
      subtitle:
        "Use this JSON schema with your own model prompts and preview themes in real time.",
      primaryCta: { label: "Try a prompt" },
      secondaryCta: { label: "Inspect schema" },
    };

  return (
    <div
      className={
        "min-h-[420px] rounded-2xl px-6 py-8 " +
        (t.page || "bg-slate-950 text-slate-50")
      }
    >
      {/* subtle radial glow behind hero */}
      <div className="relative mx-auto max-w-6xl">
        <div className="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(circle_at_top,_rgba(56,189,248,0.20),_transparent_55%)] opacity-80" />

        <div className="flex flex-col gap-10">
          {/* Hero with overlapping content + mosaic preview */}
          <section
            className={
              "relative grid gap-10 rounded-[1.75rem] p-6 md:grid-cols-[minmax(0,1.3fr),minmax(0,1fr)] " +
              (t.surface ||
                "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/60 backdrop-blur-2xl")
            }
          >
            {/* floating top badge */}
            <div className="pointer-events-none absolute -top-4 left-6">
              <span className="inline-flex items-center gap-2 rounded-full border border-white/20 bg-black/40 px-3 py-1 text-[10px] font-medium uppercase tracking-[0.18em]">
                <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
                Live preview schema
              </span>
            </div>

            {/* Left: copy + CTAs */}
            <div className="space-y-4 pt-3 md:pt-4">
              <p className="text-[10px] font-medium uppercase tracking-[0.3em] text-slate-400">
                AI Generated {(spec.theme || "UI").replace("-", " ").toUpperCase()}
              </p>
              {hero.eyebrow && (
                <p
                  className={
                    "text-xs " + (t.text?.label || "text-slate-300")
                  }
                >
                  {hero.eyebrow}
                </p>
              )}
              <h1 className="text-3xl font-semibold leading-tight md:text-[2.1rem]">
                {hero.title}
              </h1>
              {hero.subtitle && (
                <p
                  className={
                    "max-w-md text-sm " + (t.text?.muted || "text-slate-300")
                  }
                >
                  {hero.subtitle}
                </p>
              )}

              {Array.isArray(hero.bullets) && hero.bullets.length > 0 && (
                <ul
                  className={
                    "mt-2 grid gap-1.5 text-xs sm:grid-cols-2 " +
                    (t.text?.bullet || "text-slate-200")
                  }
                >
                  {hero.bullets.map((item, idx) => (
                    <li key={idx} className="flex items-start gap-2">
                      <span className="mt-[5px] h-1.5 w-1.5 rounded-full bg-emerald-400" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              )}

              <div className="mt-4 flex flex-wrap gap-3 text-sm">
                {hero.primaryCta?.label && (
                  <button
                    type="button"
                    className={
                      "rounded-xl px-4 py-2 font-medium shadow-md shadow-emerald-500/40 " +
                      (t.button?.primary ||
                        "bg-emerald-500 text-slate-950 hover:bg-emerald-400")
                    }
                  >
                    {hero.primaryCta.label}
                  </button>
                )}
                {hero.secondaryCta?.label && (
                  <button
                    type="button"
                    className={
                      "rounded-xl px-4 py-2 font-medium " +
                      (t.button?.ghost ||
                        "border border-white/20 text-slate-200 hover:bg-white/10")
                    }
                  >
                    {hero.secondaryCta.label}
                  </button>
                )}
              </div>

              {/* Stat strip under CTAs */}
              {Array.isArray(hero.stats) && hero.stats.length > 0 && (
                <div
                  className={
                    "mt-4 grid gap-4 rounded-2xl px-4 py-3 text-xs sm:grid-cols-3 " +
                    (t.card ||
                      "bg-slate-950/60 border border-white/10 shadow-inner")
                  }
                >
                  {hero.stats.map((stat) => (
                    <div key={stat.label}>
                      <p className={t.text?.label || "text-slate-400"}>
                        {stat.label}
                      </p>
                      <p
                        className={
                          "mt-1 text-sm font-semibold " +
                          (t.text?.primary || "text-slate-50")
                        }
                      >
                        {stat.value}
                      </p>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Right: overlapping mosaic preview */}
            <div className="relative flex items-center justify-center">
              <div
                className={
                  "relative h-[230px] w-full max-w-xs rounded-2xl p-3 " +
                  (t.card ||
                    "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/60")
                }
              >
                <div className="flex items-center justify-between text-[9px]">
                  <span className={t.text?.muted || "text-slate-400"}>
                    layout.json
                  </span>
                  <span
                    className={
                      "h-1.5 w-10 rounded-full " +
                      (isLightTheme ? "bg-slate-300" : "bg-white/10")
                    }
                  />
                </div>

                {/* overlapping cards */}
                <div className="mt-3 space-y-3">
                  <div className="flex gap-2">
                    <div
                      className={
                        "h-10 flex-1 rounded-xl " +
                        (isLightTheme ? "bg-slate-200" : "bg-white/5")
                      }
                    />
                    <div
                      className={
                        "h-10 w-10 rounded-xl " +
                        (isLightTheme ? "bg-slate-300" : "bg-white/5")
                      }
                    />
                  </div>
                  <div className="grid grid-cols-3 gap-2">
                    <div
                      className={
                        "h-14 rounded-xl " +
                        (isLightTheme ? "bg-slate-200" : "bg-white/6")
                      }
                    />
                    <div
                      className={
                        "h-14 rounded-xl " +
                        (isLightTheme ? "bg-slate-300" : "bg-white/8")
                      }
                    />
                    <div
                      className={
                        "h-14 rounded-xl " +
                        (isLightTheme ? "bg-slate-400" : "bg-white/5")
                      }
                    />
                  </div>
                  <div
                    className={
                      "h-10 rounded-xl " +
                      (isLightTheme ? "bg-slate-300" : "bg-white/6")
                    }
                  />
                </div>

                {/* floating mini preview overlapping bottom-right */}
                <div
                  className={
                    "absolute -bottom-6 right-4 w-32 rounded-xl px-3 py-2 text-[9px] " +
                    (t.surface ||
                      "bg-slate-950 border border-white/15 shadow-lg shadow-slate-950/80")
                  }
                >
                  <p className={t.text?.label || "text-slate-300"}>
                    Theme preview
                  </p>
                  <p
                    className={
                      "mt-1 text-[10px] " +
                      (t.text?.muted || "text-slate-400")
                    }
                  >
                    {spec.theme || "premium-dark"}
                  </p>
                </div>
              </div>
            </div>

          </section>

          {/* Features with staggered cards */}
          <section className="mx-auto max-w-5xl space-y-6">
            <div className="text-center">
              <h2 className="text-xl font-semibold">{features.title}</h2>
              {features.subtitle && (
                <p
                  className={
                    "mt-1 text-sm " + (t.text?.muted || "text-slate-400")
                  }
                >
                  {features.subtitle}
                </p>
              )}
            </div>

            <div className="grid gap-4 md:grid-cols-2">
              {(features.items || []).map((feature, idx) => (
                <div
                  key={feature.id || feature.name}
                  className={
                    "relative overflow-hidden rounded-2xl p-4 " +
                    (t.card ||
                      "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/50") +
                    (idx % 2 === 1 ? " md:translate-y-3" : "")
                  }
                >
                  <div className="absolute inset-x-0 top-0 h-0.5 bg-gradient-to-r from-emerald-400/70 via-sky-400/70 to-fuchsia-400/70 opacity-70" />
                  <h3 className="text-sm font-semibold">{feature.name}</h3>
                  {feature.description && (
                    <p
                      className={
                        "mt-2 text-xs " + (t.text?.muted || "text-slate-400")
                      }
                    >
                      {feature.description}
                    </p>
                  )}
                </div>
              ))}
            </div>
          </section>

          {/* Social proof / logos */}
          <section
            className={
              "mx-auto flex max-w-5xl flex-wrap items-center justify-between gap-4 rounded-2xl px-4 py-3 " +
              (t.surface ||
                "bg-white/5 border border-white/10 backdrop-blur-xl")
            }
          >
            <p
              className={
                "text-[11px] font-medium " +
                (t.text?.muted || "text-slate-400")
              }
            >
              {socialProof.label}
            </p>
            <div className="flex flex-wrap gap-4 text-[11px] font-semibold uppercase tracking-[0.18em]">
              {(socialProof.logos || []).map((logo) => (
                <span
                  key={logo.id || logo.name}
                  className={t.text?.label || "text-slate-300"}
                >
                  {logo.name}
                </span>
              ))}
            </div>
          </section>

          {/* Bottom CTA with glow ring */}
          <section className="relative mx-auto max-w-5xl">
            <div className="pointer-events-none absolute -inset-x-10 -top-6 -bottom-6 -z-10 bg-[radial-gradient(circle_at_center,_rgba(52,211,153,0.25),_transparent_60%)] opacity-70" />
            <div
              className={
                "rounded-3xl p-6 text-center " +
                (t.card ||
                  "bg-slate-950/70 border border-white/10 shadow-2xl shadow-slate-950/80 backdrop-blur-xl")
              }
            >
              <h2 className="text-lg font-semibold">{cta.title}</h2>
              {cta.subtitle && (
                <p
                  className={
                    "mt-1 text-sm " + (t.text?.muted || "text-slate-400")
                  }
                >
                  {cta.subtitle}
                </p>
              )}
              <div className="mt-4 flex flex-wrap justify-center gap-3 text-sm">
                {cta.primaryCta?.label && (
                  <button
                    type="button"
                    className={
                      "rounded-xl px-4 py-2 font-medium " +
                      (t.button?.primary ||
                        "bg-emerald-500 text-slate-950 hover:bg-emerald-400")
                    }
                  >
                    {cta.primaryCta.label}
                  </button>
                )}
                {cta.secondaryCta?.label && (
                  <button
                    type="button"
                    className={
                      "rounded-xl px-4 py-2 font-medium " +
                      (t.button?.secondary ||
                        "bg-white/10 text-slate-50 hover:bg-white/15")
                    }
                  >
                    {cta.secondaryCta.label}
                  </button>
                )}
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}

"""

TOKENS_CODE = """
// src/theme/tokens.js
// Central theme tokens used by all layouts

const THEME_TOKENS = {
  "minimal-light": {
    // Page background + base text
    page: "bg-slate-100/90 text-slate-900",

    // Surfaces
    surface: "bg-white border border-slate-200 shadow-sm",
    card: "bg-white/90 border border-slate-200 shadow-md",

    // Text
    text: {
      primary: "text-slate-900",
      secondary: "text-slate-800",
      muted: "text-slate-700",
      label: "text-slate-800",
      bullet: "text-slate-800",
    },

    // Buttons
    button: {
      primary: "bg-emerald-500 text-slate-950 hover:bg-emerald-600",
      secondary: "bg-slate-900 text-slate-50 hover:bg-slate-800",
      ghost:
        "border border-slate-300 text-slate-800 hover:bg-slate-100",
    },

    // Navigation (tabs, sidebars)
    nav: {
      active: "bg-emerald-100 text-slate-900",
      inactive: "text-slate-800 hover:bg-slate-100",
    },

    // Borders (if you need them separately)
    border: {
      subtle: "border-slate-200",
      strong: "border-slate-400",
    },
  },

  "soft-pastel": {
    // Page background + base text
    page: "bg-slate-50 text-slate-900",

    // Surfaces
    surface:
      "bg-white/80 border border-slate-200 shadow-sm backdrop-blur-xl",
    card:
      "bg-white/90 border border-slate-200 shadow-md backdrop-blur-xl",

    // Text
    text: {
      primary: "text-slate-900",
      secondary: "text-slate-800",
      // still need enough contrast on near‑white surfaces
      muted: "text-slate-600",
      label: "text-slate-700",
      bullet: "text-slate-800",
    },

    // Buttons
    button: {
      // soft indigo/emerald accent; dark text for legibility
      primary:
        "bg-indigo-400 text-slate-950 hover:bg-indigo-300",
      secondary:
        "bg-emerald-300 text-slate-900 hover:bg-emerald-200",
      ghost:
        "border border-slate-300 text-slate-800 hover:bg-slate-100/80",
    },

    // Navigation
    nav: {
      active: "bg-indigo-100 text-slate-900",
      inactive: "text-slate-700 hover:bg-slate-100/80",
    },

    border: {
      subtle: "border-slate-200",
      strong: "border-slate-400",
    },
  },

  "premium-dark": {
    page: "bg-slate-950 text-slate-50",
    surface: "bg-slate-950 border border-white/10 shadow-lg shadow-slate-950/60",
    card: "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/60",

    text: {
      primary: "text-slate-50",
      secondary: "text-slate-100",
      muted: "text-slate-400",
      label: "text-slate-300",
      bullet: "text-slate-200",
    },

    button: {
      primary: "bg-emerald-500 text-slate-950 hover:bg-emerald-400",
      secondary: "bg-white/10 text-slate-50 hover:bg-white/15",
      ghost:
        "border border-white/20 text-slate-200 hover:bg-white/10",
    },

    nav: {
      active: "bg-emerald-500/15 text-slate-50",
      inactive: "text-slate-300 hover:bg-white/5",
    },

    border: {
      subtle: "border-white/10",
      strong: "border-white/30",
    },
  },

  "high-contrast": {
  // Very dark page; strong global contrast
  page: "bg-black text-white",

  // Surfaces stay dark so white text tokens always work
  surface:
    "bg-neutral-950 border border-white shadow-[0_0_0_1px_rgba(255,255,255,0.6)]",
  card:
    "bg-neutral-900 border border-white shadow-[0_0_0_1px_rgba(255,255,255,0.8)]",

  text: {
    // All text is light-on-dark; no white cards
    primary: "text-white",
    secondary: "text-neutral-100",
    muted: "text-neutral-300",
    label: "text-neutral-200",
    bullet: "text-neutral-100",
  },

  button: {
    // Primary: inverted for emphasis
    primary:
      "bg-white text-black hover:bg-neutral-100",
    // Secondary: strong outline
    secondary:
      "bg-neutral-950 text-white border border-white hover:bg-neutral-900",
    // Ghost: minimalist but visible
    ghost:
      "border border-white text-white hover:bg-white/10",
  },

  nav: {
    // Active tab is clearly boxed and inverted
    active: "bg-white text-black",
    // Inactive keeps high contrast but slightly dimmer
    inactive: "text-neutral-200 hover:bg-white/10",
  },

  border: {
    subtle: "border-white/70",
    strong: "border-white",
  },
},


  "frosted-glass": {
    page:
      "bg-slate-900/90 text-slate-50 bg-[radial-gradient(circle_at_top,_rgba(148,163,184,0.35),_transparent_60%)]",
    surface:
      "bg-white/10 border border-white/30 backdrop-blur-2xl shadow-2xl shadow-slate-950/60",
    card:
      "bg-white/12 border border-white/35 backdrop-blur-2xl shadow-xl shadow-slate-950/60",

    text: {
      primary: "text-slate-50",
      secondary: "text-slate-100",
      muted: "text-slate-400",
      label: "text-slate-300",
      bullet: "text-slate-100",
    },

    button: {
      primary: "bg-emerald-400 text-slate-950 hover:bg-emerald-300",
      secondary: "bg-white/15 text-slate-50 hover:bg-white/25",
      ghost:
        "border border-white/30 text-slate-50 hover:bg-white/10",
    },

    nav: {
      active: "bg-emerald-400/25 text-slate-50",
      inactive: "text-slate-200 hover:bg-white/5",
    },

    border: {
      subtle: "border-white/25",
      strong: "border-white/50",
    },
  },
};

export function getThemeTokens(name) {
  return THEME_TOKENS[name] ?? THEME_TOKENS["premium-dark"];
}

"""
