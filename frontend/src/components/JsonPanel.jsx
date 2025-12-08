import React from "react";

export function JsonPanel({ data }) {
  if (!data) {
    return (
      <div className="flex h-full items-center justify-center text-xs text-slate-500">
        Raw JSON will appear here.
      </div>
    );
  }
  return (
    <pre className="h-full overflow-auto rounded-2xl border border-white/10 bg-slate-950/80 p-3 text-[11px] text-slate-200">
      {JSON.stringify(data, null, 2)}
    </pre>
  );
}
