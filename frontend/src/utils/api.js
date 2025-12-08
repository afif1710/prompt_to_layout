import axios from "axios";

const api = axios.create({
  baseURL: "/api",
  headers: {
    "Content-Type": "application/json"
  }
});

export async function generateUI(payload) {
  const { data } = await api.post("/generate-ui", payload);
  return data;
}

export async function uploadSketch(formData) {
  const { data } = await api.post("/upload-sketch", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });
  return data;
}

export async function fetchProjects() {
  const { data } = await api.get("/projects");
  return data;
}

export async function saveProject(payload) {
  const { data } = await api.post("/save-project", payload);
  return data;
}

export async function downloadZip(files) {
  const { data } = await api.post("/download-zip", { files }, { 
    responseType: "blob" 
  });
  return data;
}
