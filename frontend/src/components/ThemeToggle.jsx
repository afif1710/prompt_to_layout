import React from "react";
import { classNames } from "../utils/classNames";

const THEMES = [
  { id: "minimal-light", label: "Minimal Light", dotClass: "bg-slate-100" },
  { id: "premium-dark", label: "Premium Dark", dotClass: "bg-slate-900" },
  { id: "frosted-glass", label: "Frosted Glass", dotClass: "bg-cyan-300" }
];

export function ThemeToggle({ value, onChange }) {
  return (
    <div className="space-y-2">
      <p className="text-xs font-medium uppercase tracking-[0.2em] text-slate-400">
        Theme
      </p>
      <div className="flex gap-2">
        {THEMES.map((t) => (
          <button
            key={t.id}
            type="button"
            onClick={() => onChange(t.id)}
            className={classNames(
              "group flex flex-1 items-center gap-2 rounded-2xl border px-3 py-2 text-xs transition-all",
              value === t.id
                ? "border-brand-violet/60 bg-white/10 shadow-md shadow-black/50"
                : "border-white/10 bg-white/5 hover:border-white/40"
            )}
          >
            <span
              className={classNames(
                "h-2.5 w-2.5 rounded-full shadow-[0_0_0_3px_rgba(148,163,184,0.45)]",
                t.dotClass
              )}
            />
            <span className="text-slate-200">{t.label}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
