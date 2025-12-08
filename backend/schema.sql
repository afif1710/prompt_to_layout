-- AI UI Builder Database Schema
CREATE DATABASE IF NOT EXISTS ai_ui_builder CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ai_ui_builder;

CREATE TABLE IF NOT EXISTS ui_builder_project (
  id INT AUTO_INCREMENT PRIMARY KEY,
  project_name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  files JSON NOT NULL,
  created_at DATETIME(6) NOT NULL,
  INDEX idx_created_at (created_at),
  INDEX idx_project_name (project_name(100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
