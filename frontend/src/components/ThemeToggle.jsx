import React from "react";
import { classNames } from "../utils/classNames";

const THEMES = [
  { id: "minimal-light", label: "Minimal Light", dotClass: "bg-slate-100" },
  { id: "premium-dark", label: "Premium Dark", dotClass: "bg-slate-900" },
  { id: "frosted-glass", label: "Frosted Glass", dotClass: "bg-cyan-300" },
  { id: "soft-pastel", label: "Soft Pastel", dotClass: "bg-rose-100" },
  { id: "high-contrast", label: "High Contrast", dotClass: "bg-black" },
];

export function ThemeToggle({ value, onChange }) {
  const current = THEMES.find((t) => t.id === value) || THEMES[0];

  return (
    <div className="space-y-2">
      {/* Label, nudged right to align with select */}
      <p className="ml-1 text-xs pl-2 font-medium uppercase tracking-[0.2em] text-slate-400">
        Themes
      </p>

      {/* Wrapper also nudged right so control sits under label */}
      <div className="relative ml-1">
        <select
          value={current.id}
          onChange={(e) => onChange(e.target.value)}
          // compact width + extra right padding so arrow isn't on the edge
          className="inline-block max-w-[170px] min-w-[130px] rounded-2xl border border-white/15 bg-slate-950/70 pl-3 pr-7 py-2 text-xs text-slate-100 shadow-inner shadow-black/40 focus:border-brand-violet/70 focus:outline-none"
        >
          {THEMES.map((t) => (
            <option
              key={t.id}
              value={t.id}
              className="bg-slate-950 text-slate-100"
            >
              {t.label}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}
