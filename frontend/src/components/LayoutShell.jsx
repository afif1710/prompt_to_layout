import React from "react";
import { getThemeTokens } from "../theme/tokens";

export function LayoutShell({ children }) {
  // Keep the editor shell stable regardless of preview theme
  const studioTheme = "premium-dark";
  const t = getThemeTokens(studioTheme);

  return (
    <div className={"min-h-screen " + (t.page || "bg-slate-950 text-slate-50")}>
      <div className="mx-auto flex min-h-screen max-w-6xl flex-col gap-4 px-4 pb-8 pt-6 md:pt-10">
        <header
          className={
            "flex flex-col gap-4 rounded-3xl px-4 py-3 md:flex-row md:items-center md:justify-between " +
            (t.surface || "bg-white/5 border border-white/10") +
            " shadow-glass-soft backdrop-blur-2xl"
          }
        >
          <div>
            <p
              className={
                "text-[10px] font-medium uppercase tracking-[0.3em] " +
                (t.text?.muted || "text-slate-400")
              }
            >
              AI WEB UI BUILDER
            </p>
            <h1 className="mt-1 text-xl font-semibold tracking-tight md:text-2xl">
              Describe your product, get a premium React UI.
            </h1>
            <p className={"mt-1 text-xs " + (t.text?.muted || "text-slate-400")}>
              Natural language or sketch in, polished component tree, JSX, and preview out.
            </p>
          </div>
          <div className={"flex items-center gap-3 text-[11px] " + (t.text?.muted || "text-slate-400")}>
            <span className="rounded-full border border-emerald-500/40 bg-emerald-500/10 px-2 py-1 text-[10px] font-medium uppercase tracking-[0.2em] text-emerald-300">
              Live MVP
            </span>
            <span>Powered by AI</span>
          </div>
        </header>
        {children}
      </div>
    </div>
  );
}
