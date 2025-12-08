import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

function TreeNode({ node, depth = 0 }) {
  const [open, setOpen] = useState(true);
  const hasChildren = node.children && node.children.length > 0;

  return (
    <div className="rounded-2xl bg-white/2">
      <button
        type="button"
        onClick={() => hasChildren && setOpen((o) => !o)}
        className="flex w-full items-center gap-2 rounded-2xl px-3 py-2 text-xs text-slate-200 hover:bg-white/5"
      >
        <span
          className={`h-4 w-4 rounded-full border border-white/15 ${
            hasChildren ? "bg-brand-violet/40" : "bg-slate-700/60"
          }`}
        />
        <span className="font-medium text-slate-100">{node.type}</span>
        {node.props && node.props.layout && (
          <span className="rounded-full bg-slate-900/60 px-2 py-0.5 text-[10px] text-slate-400">
            {node.props.layout}
          </span>
        )}
        <span className="ml-auto text-[10px] uppercase tracking-[0.2em] text-slate-500">
          {hasChildren ? (open ? "−" : "+") : "•"}
        </span>
      </button>
      <AnimatePresence initial={false}>
        {hasChildren && open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            className="overflow-hidden pl-6"
          >
            <div className="border-l border-dashed border-slate-700/60 pl-3 space-y-1">
              {node.children.map((child, idx) => (
                <TreeNode key={idx} node={child} depth={depth + 1} />
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export function ComponentTree({ tree }) {
  if (!tree) {
    return (
      <div className="flex h-full items-center justify-center text-xs text-slate-500">
        Component tree will appear here after generation.
      </div>
    );
  }
  return (
    <div className="space-y-2 text-xs">
      <TreeNode node={tree} />
    </div>
  );
}
