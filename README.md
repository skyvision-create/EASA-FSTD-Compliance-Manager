# EASA FSTD Compliance Manager

A web application for Approved Training Organizations (ATOs) to implement and document compliance with the new EASA FSTD regulation (Regulation (EU) 2026/781, CS-FSTD Issue 1, ED Decision 2026/006/R).

## Features

- **Programme Management**: Create and manage type rating training programmes per aircraft type/variant
- **Appendix 9 Task Library**: Structured task database with FCS requirements (T/TP levels)
- **FSTD Register**: Device inventory with qualification certificates, ESLs, and FCS profiles
- **Task-to-Tool Engine**: Automated FCS compliance checking (FSTD FCS ≥ Task TP FCS)
- **ADDIE ISD Workspace**: Complete instructional systems design workflow
- **Compliance Matrix**: Live regulatory compliance tracking with evidence linkage
- **PDF Export**: Authority approval packs and internal reference documents

## Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.10+
- PostgreSQL 14+ (or SQLite for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd easa-fstd-compliance-manager
   ```

2. **Install backend dependencies**
   ```bash
   cd backend
   python -m pip install -r requirements.txt
   ```

3. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   ```

4. **Start backend**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Start frontend**
   ```bash
   cd frontend
   npm run dev
   ```

6. **Access the application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Deployment

### Railway

1. Connect your GitHub repository to Railway
2. Create two services:
   - Backend: Root directory `backend`, Dockerfile builder
   - Frontend: Root directory `frontend`, build `npm install && npm run build`, start `npx serve -s dist -l $PORT`
3. Add PostgreSQL database
4. Set environment variables:
   - Backend: `DATABASE_URL`, `SECRET_KEY`, `CORS_ORIGINS`
   - Frontend: `VITE_API_URL`

### Docker

```bash
docker-compose up -d
```

## Project Structure

```
easa-fstd-compliance-manager/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── core/
│       │   ├── config.py
│       │   └── database.py
│       ├── api/
│       ├── models/
│       └── services/
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── src/
│       ├── main.tsx
│       └── App.tsx
└── README.md
```

## License

Proprietary - All rights reserved.

## Disclaimer

This application is a compliance management and evidence-structuring aid. It does not constitute authority approval or substitute for the ATO's formal compliance determination.
