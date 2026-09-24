# Astra Shopping OS

AI-powered multi-marketplace shopping comparison platform.

## V1 scope
- Multi-marketplace search abstraction
- Product normalization and SKU matching
- Real-price calculation
- Price-history storage model
- AI-ready comparison API
- Next.js frontend shell
- FastAPI backend
- Docker Compose
- MCP-ready service boundaries

## Architecture
Next.js -> FastAPI -> Marketplace Adapters -> Normalizer/Matcher -> Pricing -> PostgreSQL/Redis

V1 uses deterministic mock marketplace adapters so the complete product flow can be tested before connecting live marketplace integrations.

## Run

```bash
cp .env.example .env
docker compose up --build
```

Frontend: http://localhost:3000
Backend: http://localhost:8000
Docs: http://localhost:8000/docs

## Data policy
Live marketplace connectors must respect each marketplace's API availability, authentication requirements, rate limits and terms of service. The project does not implement anti-bot bypass or automated payment.
