# DocuMind

> AI-powered Document Intelligence Platform built with FastAPI, PostgreSQL, Docker and Alembic.

DocuMind is a backend-focused document intelligence platform designed to upload, process, search and interact with documents using AI and RAG.

The project is being developed step-by-step using a production-style architecture with authentication, document processing, vector search, background jobs and local AI models.

---

## 🚀 Current Progress

### Completed

- [x] FastAPI application setup
- [x] Docker & Docker Compose setup
- [x] PostgreSQL database
- [x] SQLAlchemy ORM
- [x] User model
- [x] Document model
- [x] User creation API
- [x] Get users API
- [x] Pydantic schemas
- [x] Database relationships
- [x] Alembic migrations
- [x] PostgreSQL + pgvector ready environment

### Upcoming

- [ ] User authentication
- [ ] Password hashing
- [ ] JWT authentication
- [ ] Protected APIs
- [ ] Document upload
- [ ] PDF text extraction
- [ ] Document chunking
- [ ] Embeddings
- [ ] Vector search with pgvector
- [ ] RAG pipeline
- [ ] Local LLM integration using Ollama
- [ ] Redis + Celery background processing
- [ ] Document citations
- [ ] MinIO object storage
- [ ] Automated tests
- [ ] Frontend
- [ ] CI/CD

---

## 🏗️ Architecture

```text
                    ┌──────────────┐
                    │    Client    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   FastAPI    │
                    └──────┬───────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       ┌──────────────┐         ┌──────────────┐
       │ PostgreSQL   │         │   Services   │
       │  + pgvector  │         │              │
       └──────────────┘         └──────┬───────┘
                                       │
                                       ▼
                              Document Processing
                                       │
                                       ▼
                                    Chunks
                                       │
                                       ▼
                                  Embeddings
                                       │
                                       ▼
                                  Vector Search
                                       │
                                       ▼
                                  RAG Pipeline
                                       │
                                       ▼
                              Local LLM (Ollama)
