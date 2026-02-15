# ADR-001: Technology Stack Definition

> **Status**: Accepted
> **Date**: 2026-01-29
> **Context**: Transformation from simple website to "AI-Powered Owner Business Platform".

## 1. Executive Summary

We are building a **Owner Business Platform** (Business Intelligence, AI Agents, Operations) rather than just a client-facing website. The stack must support:

- **Reactive UI** for the owner dashboard (`/admin`).
- **Relational Data** for complex room/reservation concepts.
- **AI Integration** (Agents reading/writing data).
- **Zero-Ops Deployment** (Vercel).

## 2. The Stack (2026 Standard)

### A. Core Framework: **Next.js 16 (App Router)**

- **Why**: Industry standard for React. Unified backend/frontend.
- **Role**: Handles UI, API Routes, and Server Actions.
- **Current State**: In use. verified.

### B. Database Strategy: **SQLite → PostgreSQL**

- **Phase 1 (Current)**: **SQLite** (`better-sqlite3`).
  - _Why_: file-based, zero latency, instant backups, perfect for "Embedded AI" workflows.
  - _Location_: `property.db`.
- **Phase 2 (Scale)**: **PostgreSQL** (via Supabase or Neon).
  - _Why_: Multi-tenancy, Row Level Security (RLS), Real-time subscriptions.
  - _Trigger_: When we onboard the second property.

### C. Language: **TypeScript** (Strict)

- **Why**: Non-negotiable for large-scale AI refactors and type safety.

### D. Styling: **CSS Modules + Design System**

- **Current**: CSS Modules (`*.module.css`).
- **Future**: Tailored Design System (Variables for "Moroccan Earth" palette).
- **Decision**: Avoid Tailwind complexity for now; stick to semantic CSS for "Premium" feel.

### E. Infrastructure: **Vercel**

- **CI/CD**: Automatic deployments from Git.
- **Storage**: Vercel Blob (for Images/Assets).
- **KV**: Vercel KV (for Agent State/Caching if needed).

## 3. Alignment with "Claude Code Plan"

This stack exactly mirrors the "Phase 3: Platform Architecture" proposal:

- [x] Framework: Next.js App Router.
- [x] Database: SQLite (Dev) -> Postgres (Prod).
- [x] Architecture: Modular `src/` structure.

## 4. Operational Directives

### 1. **Database First**

All business logic reads/writes from DB, not Markdown files.

### 2. **Server Actions**

Use Next.js Server Actions for data mutation (no manual API routes unless external consumers needed).

### 3. **Agent-Friendly**

DB Schema must be simple and documented (`schema.sql`) so AI agents can query it autonomously.
