Data Platform Kinshasa — e-Gov Simulation Engine








👨‍💻 Author

JEAN-LUC LUZEMBA

🧭 Project Overview

This project is a realistic government-scale data engineering simulation system designed to model a civil registry (e-Government system) for Kinshasa, Democratic Republic of Congo.

It simulates:

👤 Citizens registration (synthetic + real CSV data)
🏘 Population distribution across communes (weighted model)
📄 Administrative requests (civil status services)
📊 KPI-ready datasets for analytics & dashboards

🎯 Goal: simulate a real-world e-Government data infrastructure for analytics, portfolio demonstration, and scalability testing.

🏗 System Architecture
⚙️ Tech Stack
🐍 Python 3.x
🐘 PostgreSQL (Neon Cloud DB)
🎲 Faker (synthetic data generation)
📊 CSV ingestion pipeline
🔗 psycopg2 (DB connector)
🧠 ETL architecture (Extract → Transform → Load)
🚀 Core Features
👤 1. Citizen Generation Engine
Real CSV-based name ingestion
Synthetic enrichment (Faker)
Unique identifiers (CI numbers)
Secure random emails
Gender & birth data generation
🏘 2. Realistic Population Distribution

Population is not uniform across communes.

Weighted simulation:

High density: Kimbanseke, Masina, Ndjili
Medium density: Lemba, Limete
Lower density: others

👉 This mimics real urban population dynamics of Kinshasa

📄 3. Administrative Requests Simulation

Each citizen generates:

🪪 Acte de naissance
💍 Acte de mariage
🏠 Acte de résidence

With:

status tracking (pending / approved / rejected)
timestamps
relational integrity
📊 4. Analytics Ready Output

This system enables:

Population per commune
Administrative load per region
Citizen-to-request ratio
Urban pressure simulation
Government KPI dashboards
🔁 Data Pipeline Flow
CSV Dataset
   ↓
Normalization Layer (accent-safe parsing)
   ↓
Citizen Generator (Faker enrichment)
   ↓
Weighted Commune Distribution
   ↓
PostgreSQL (Neon Cloud)
   ↓
Request Generator (1–3 per citizen)
   ↓
Analytics-ready relational database
🗄 Database Schema
👤 Citoyens
id
communeId
nom
postnom
prenom
dateNaissance
sexe
lieuNaissance
numeroUnique
password
email
createdAt
updatedAt
📄 Requests
id
citizenId
type
status
createdAt
updatedAt
📊 Example Output
🚀 PIPELINE START
📌 Headers détectés: ['Nom', 'Post-nom', 'Prénom']
📊 CSV loaded: 24746 persons
🏘 communes loaded: 24
🎯 Simulation size: 5000 citizens

👤 citizen created: 1024
👤 citizen created: 1025
...

✅ PIPELINE DONE
✔ created: 4876
⚠️ skipped: 124
🧠 Engineering Concepts Demonstrated
✔ ETL Pipeline Design
Extract (CSV)
Transform (cleaning + normalization)
Load (PostgreSQL)
✔ Data Quality Engineering
Accent normalization
Missing data handling
Schema validation
✔ Synthetic Data Generation
Faker integration
Controlled randomness
Unique identity generation
✔ Weighted Sampling Model
Realistic population distribution
Urban simulation logic
📈 Business / Real-World Value

This project simulates:

🏛 Government civil registry systems
📊 National data infrastructure
📡 Administrative workload analysis
🌍 Urban population modeling
🚀 Roadmap
⚡ Batch inserts optimization (10x performance)
📊 Power BI / Metabase dashboard
🧠 Predictive analytics (request forecasting)
🌍 Geo-mapping of communes
📡 FastAPI service layer
📈 100k+ citizens simulation scale
🧪 How to Run
pip install -r requirements.txt
python3 run.pipeline.py
🏁 Final Statement

This project demonstrates a production-style data engineering pipeline capable of simulating a real-world e-Government system, combining:

structured data engineering
synthetic data generation
relational database modeling
analytical readiness
👨‍💻 Author

JEAN-LUC LUZEMBA