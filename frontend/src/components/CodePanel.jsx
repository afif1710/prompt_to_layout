import React from "react";

export function CodePanel({ files, onCopy }) {
  const entries = Object.entries(files || {});
  const [active, setActive] = React.useState(entries[0]?.[0] ?? "");

  React.useEffect(() => {
    if (!active && entries[0]) setActive(entries[0][0]);
  }, [entries, active]);

  if (!entries.length) {
    return (
      <div className="flex h-full items-center justify-center text-xs text-slate-500">
        Code will be generated here.
      </div>
    );
  }

  const code = files[active] || "";

  return (
    <div className="flex h-full flex-col rounded-2xl border border-white/10 bg-slate-950/80">
      <div className="flex items-center justify-between border-b border-white/10 px-3 py-2">
        <div className="flex gap-2 text-[11px] overflow-x-auto">
          {entries.map(([name]) => (
            <button
              key={name}
              type="button"
              onClick={() => setActive(name)}
              className={`whitespace-nowrap rounded-full px-3 py-1 ${
                active === name
                  ? "bg-white/10 text-slate-100 shadow-sm shadow-black/40"
                  : "text-slate-500 hover:bg-white/5"
              }`}
            >
              {name}
            </button>
          ))}
        </div>
        <button
          type="button"
          onClick={onCopy}
          className="rounded-full bg-emerald-500/90 px-3 py-1 text-[11px] font-medium text-emerald-950 shadow-sm shadow-emerald-500/40 hover:bg-emerald-400"
        >
          Copy all
        </button>
      </div>
      <pre className="flex-1 overflow-auto p-3 text-[11px] leading-relaxed">
        <code className="text-emerald-100">{code}</code>
      </pre>
    </div>
  );
}
