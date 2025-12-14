# frontend/Dockerfile
FROM node:20-alpine

WORKDIR /app

# Install dependencies separately so Docker can cache node_modules
COPY package.json package-lock.json* /app/
RUN npm install

# Copy the rest of the frontend source
COPY . /app/

# Expose Vite dev server port
EXPOSE 5173

# Dev command with hot reload
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
