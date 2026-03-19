-- Create a table for Medical Imaging Metadata
CREATE TABLE IF NOT EXISTS imaging_metadata (
    image_id SERIAL PRIMARY KEY,
    patient_id VARCHAR(50) NOT NULL,
    study_date DATE NOT NULL,
    modality VARCHAR(10), -- e.g., MRI, CT, X-RAY
    body_part VARCHAR(50),
    file_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);