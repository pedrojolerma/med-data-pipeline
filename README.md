# Medical Imaging Data Pipeline (MVP)

### End-to-End Data Engineering Portfolio Project



## Project Overview

This project demonstrates a containerized ETL (Extract, Transform, Load) pipeline designed to manage medical imaging metadata (MRI, CT, X-RAY). It automates the ingestion of clinical records from raw CSV formats into a structured PostgreSQL Data Warehouse.



## Tech Stack

\* \*\*Language:\*\* Python 3.x

\* \*\*Database:\*\* PostgreSQL 15 (Containerized via Docker)

\* \*\*Orchestration:\*\* Docker Compose

\* \*\*Libraries:\*\* Pandas, SQLAlchemy, python-dotenv

\* \*\*Version Control:\*\* Git



## Architecture

1\. \*\*Infrastructure:\*\* PostgreSQL running in a Docker container for environment isolation.

2\. \*\*Security:\*\* Sensitive credentials managed via `.env` (excluded from Git).

3\. \*\*Ingestion:\*\* Python/Pandas script to validate and load clinical metadata.

4\. \*\*Schema:\*\* Relational design optimized for medical modality queries.



## How to Run

1\. Ensure Docker Desktop is running.

2\. Clone the repository and `cd` into the project folder.

3\. Create a `.env` file based on the project requirements.

4\. Run `docker-compose up -d` to launch the database.

5\. Run `pip install -r requirements.txt`.

6\. Run `python scripts/initialize\_db.py` to create the tables.

7\. Run `python scripts/ingest\_data.py` to load the data.

