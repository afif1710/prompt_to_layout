import React, { useState } from "react";
import { DeviceFrame } from "./DeviceFrame";

import { CodePanel } from "./CodePanel";
import { JsonPanel } from "./JsonPanel";
import { motion } from "framer-motion";
import { downloadZip } from "../utils/api";
import { renderFromSpec } from "../layoutRenderer"; // keep this
// REMOVE this line:
// import { pricingSpec } from "../specExamples/pricingSpec";

const TABS = ["Preview", "Code", "JSON"];

export function OutputPanel({ result, loading, onCopyCode }) {
  const [tab, setTab] = useState("Preview");

  // NEW: spec coming from backend
  const spec = result?.component_tree;

  const handleDownloadZip = async () => {
    if (!result?.files) return;
    try {
      const blob = await downloadZip(result.files);
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "ui-project.zip";
      a.click();
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error("Download failed:", error);
    }
  };

  return (
    <div className="flex h-full flex-col gap-4 rounded-3xl border border-white/10 bg-slate-950/80 p-4 shadow-glass-soft backdrop-blur-2xl">
      <div className="flex items-center justify-between gap-4 border-b border-white/10 pb-2">
        <div className="flex gap-2 text-xs">
          {TABS.map((t) => (
            <button
              key={t}
              type="button"
              onClick={() => setTab(t)}
              className={`relative rounded-full px-3 py-1 ${
                tab === t
                  ? "bg-white/10 text-slate-50"
                  : "text-slate-500 hover:bg-white/5"
              }`}
            >
              {t}
              {tab === t && (
                <motion.span
                  layoutId="tab-underline"
                  className="absolute inset-x-2 -bottom-1 h-[2px] rounded-full bg-gradient-to-r from-brand-violet to-brand-blue"
                />
              )}
            </button>
          ))}
        </div>
        <div className="flex gap-2">
          <button
            type="button"
            onClick={handleDownloadZip}
            disabled={!result?.files}
            className="rounded-full border border-white/15 bg-white/5 px-3 py-1 text-[11px] text-slate-100 hover:bg-white/10 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            Download ZIP
          </button>
        </div>
      </div>

      <div className="relative flex-1 overflow-hidden">
        {loading && (
          <div className="absolute inset-0 z-10 flex items-center justify-center rounded-2xl bg-slate-950/80 backdrop-blur-sm">
            <div className="flex flex-col items-center gap-3">
              <div className="h-8 w-8 animate-spin rounded-full border-2 border-brand-violet border-t-transparent" />
              <p className="text-xs text-slate-400">Generating your UI...</p>
            </div>
          </div>
        )}
        <div className="h-full">
          {tab === "Preview" && (
            <DeviceFrame>
              <div className="h-[420px] overflow-auto bg-slate-950 p-4">
                {spec ? (
                  renderFromSpec(spec)
                ) : (
                  <div className="flex h-full items-center justify-center text-xs text-slate-500">
                    Generated UI preview will appear here.
                  </div>
                )}
              </div>
            </DeviceFrame>
          )}

          {tab === "Code" && (
            <div className="h-full">
              <CodePanel files={result?.files} onCopy={onCopyCode} />
            </div>
          )}

          {tab === "JSON" && (
            <div className="h-full">
              <JsonPanel data={result} />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
