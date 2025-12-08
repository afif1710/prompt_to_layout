"""
Utilities for creating ZIP archives of generated code
"""
import io
import zipfile

def create_zip_from_files(files_dict):
    """
    Create a ZIP archive from a dictionary of files.

    Args:
        files_dict: Dictionary mapping file paths to content

    Returns:
        bytes: ZIP file content

    Example:
        files = {
            "src/App.jsx": "import React...",
            "package.json": "{ ... }"
        }
        zip_bytes = create_zip_from_files(files)
    """
    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, content in files_dict.items():
            # Ensure content is string
            if isinstance(content, bytes):
                zf.writestr(path, content)
            else:
                zf.writestr(path, content.encode("utf-8"))

    buffer.seek(0)
    return buffer.read()

def add_package_json(files_dict):
    """
    Add a default package.json if not present.

    Args:
        files_dict: Existing files dictionary

    Returns:
        Dict: Updated files dictionary with package.json
    """
    if "package.json" not in files_dict and "src/package.json" not in files_dict:
        files_dict["package.json"] = """{
  "name": "generated-ui-project",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "framer-motion": "^11.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.1.0",
    "vite": "^5.2.0",
    "tailwindcss": "^3.4.4",
    "autoprefixer": "^10.4.17",
    "postcss": "^8.4.38"
  }
}"""

    return files_dict
