# Multi-Agent Research and Analysis Assistant

An intelligent, modular workflow orchestrator built with Python, LangGraph, LangChain, and FastAPI. It uses a state-based multi-agent architecture to handle complex research tasks, information extraction, and synthesis.

## Features
- **LangGraph Orchestration:** Manages agent states and controlled workflow transitions (Research -> Extraction -> Analysis).
- **FastAPI Interface:** Exposes the multi-agent workflow via REST API returning structured JSON responses.
- **Modular Agents:** Specialized nodes handle targeted sub-tasks to improve reasoning quality and reduce hallucination.

## Setup & Run Locally
1. Clone the repository.
2. Build and run using Docker:
   ```bash
   docker-compose up -d --build
   ```
3. Access Swagger UI at `http://localhost:8002/docs`.

## Endpoints
- `POST /research`: Trigger a research workflow on a specific topic.


## Community
Contributions are always welcome. See CONTRIBUTING.md for details.
