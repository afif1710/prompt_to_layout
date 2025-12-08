import React from "react";

export function LayoutShell({ children }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-slate-50">
      <div className="mx-auto flex min-h-screen max-w-6xl flex-col gap-4 px-4 pb-8 pt-6 md:pt-10">
        <header className="flex flex-col gap-4 rounded-3xl border border-white/10 bg-white/[0.03] px-4 py-3 shadow-glass-soft backdrop-blur-2xl md:flex-row md:items-center md:justify-between">
          <div>
            <p className="text-[10px] font-medium uppercase tracking-[0.3em] text-slate-400">
              AI WEB UI BUILDER
            </p>
            <h1 className="mt-1 text-xl font-semibold tracking-tight md:text-2xl">
              Describe your product, get a premium React UI.
            </h1>
            <p className="mt-1 text-xs text-slate-400">
              Natural language or sketch in, polished component tree, JSX, and preview out.
            </p>
          </div>
          <div className="flex items-center gap-3 text-[11px] text-slate-400">
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
