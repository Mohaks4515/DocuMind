# DocuMind

> AI-powered Document Intelligence Platform built with FastAPI, PostgreSQL, Docker, JWT Authentication and Alembic.

DocuMind is a backend-focused AI document intelligence platform designed to upload, process, search and interact with documents using AI and RAG.

The project is being developed step-by-step using a production-style architecture with authentication, document processing, vector search, background jobs and local AI models.

---

## 🚀 Current Progress

### Completed

- [x] FastAPI application setup
- [x] Docker & Docker Compose setup
- [x] PostgreSQL database
- [x] PostgreSQL + pgvector environment
- [x] SQLAlchemy ORM
- [x] User model
- [x] Document model
- [x] User creation API
- [x] Get users API
- [x] Pydantic schemas
- [x] Database relationships
- [x] Alembic migrations
- [x] Password hashing with bcrypt
- [x] User registration
- [x] JWT authentication
- [x] Login API
- [x] JWT token validation
- [x] Protected `/users/me` endpoint
- [x] Swagger OAuth2 authentication

### Upcoming

- [ ] Document upload
- [ ] PDF text extraction
- [ ] Document processing pipeline
- [ ] Text chunking
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

# 🏗️ Architecture

### Current Architecture

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
       ┌──────────────┐         ┌───────────────┐
       │ PostgreSQL   │         │Authentication │
       │  + pgvector  │         │ JWT + bcrypt  │
       └──────────────┘         └───────────────┘


### Planned Document intelligence
                         PDF
                          │
                          ▼
                    ┌───────────┐
                    │  FastAPI  │
                    └─────┬─────┘
                          │
                          ▼
                 Document Processing
                          │
                          ▼
                   Text Extraction
                          │
                          ▼
                      Chunking
                          │
                          ▼
                     Embeddings
                          │
                          ▼
                PostgreSQL + pgvector
                          │
                          ▼
                   Vector Search
                          │
                          ▼
                        RAG
                          │
                          ▼
                  Local LLM / Ollama
                          │
                          ▼
                 Answer + Citations