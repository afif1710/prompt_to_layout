import React, { useState } from "react";
import { LayoutShell } from "./components/LayoutShell";
import { InputPanel } from "./components/InputPanel";
import { OutputPanel } from "./components/OutputPanel";
import { Toast } from "./components/Toast";
import { generateUI, uploadSketch, saveProject } from "./utils/api";

export default function App() {
  const [description, setDescription] = useState(
    "Create a modern analytics dashboard with sidebar, stat cards, and a traffic chart."
  );
  const [theme, setTheme] = useState("premium-dark");
  const [sketchFile, setSketchFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [toast, setToast] = useState({ message: "", type: "success" });

  const showToast = (message, type = "success") => {
    setToast({ message, type });
    setTimeout(() => setToast({ message: "", type: "success" }), 2500);
  };

  const handleGenerate = async () => {
    if (!description && !sketchFile) {
      showToast("Provide a description or upload a sketch.", "error");
      return;
    }

    setLoading(true);
    try {
      let data;
      if (sketchFile) {
        const formData = new FormData();
        formData.append("file", sketchFile);
        formData.append("theme", theme);
        data = await uploadSketch(formData);
      } else {
        data = await generateUI({ description, theme });
      }

      setResult(data);
      showToast("UI generated successfully!");

      try {
        await saveProject({
          project_name: description.slice(0, 40) || "Untitled Project",
          description: description || "Sketch-based project",
          files: data.files,
        });
      } catch (saveError) {
        console.error("Error saving project:", saveError);
      }
    } catch (error) {
      console.error("Generation error:", error);
      showToast("Failed to generate UI. Check console for details.", "error");
    } finally {
      setLoading(false);
    }
  };

  const handleCopyCode = async () => {
    if (!result?.files) return;
    try {
      const combined = Object.entries(result.files)
        .map(([name, content]) => `// ${name}\n${content}`)
        .join("\n\n\n");
      await navigator.clipboard.writeText(combined);
      showToast("All code copied to clipboard!");
    } catch (error) {
      console.error("Copy failed:", error);
      showToast("Failed to copy code.", "error");
    }
  };

  return (
    <LayoutShell>
      <Toast message={toast.message} type={toast.type} />
      <main className="grid flex-1 gap-4 md:grid-cols-[minmax(260px,320px),1fr]">
        <InputPanel
          description={description}
          setDescription={setDescription}
          onGenerate={handleGenerate}
          theme={theme}
          setTheme={setTheme}
          setSketchFile={setSketchFile}
          loading={loading}
        />
        <OutputPanel
          result={result}
          loading={loading}
          onCopyCode={handleCopyCode}
        />
      </main>
    </LayoutShell>
  );
}
