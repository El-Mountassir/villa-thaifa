# Tech Stack Decisions & Rationale

**Version**: 1.0
**Last Updated**: 2026-02-13
**Context**: Villa Thaifa PMS — 2-user property management app

---

## Decision Summary

**Framework**: Next.js 15 (App Router)
**Database**: Vercel Postgres (Neon)
**Deployment**: Vercel (free tier)
**Auth**: NextAuth.js + magic links
**UI**: shadcn/ui + Tailwind CSS
**i18n**: next-intl
**OTA Integration**: HotelRunner API (custom REST wrapper)

**Why not Vite+React+FastAPI?** This is a standalone client project, not Omar's platform. Full-stack Next.js is the simplest path for 2-user app on Vercel. No double-backend risk because there IS no other backend.

---

## Stack Comparison: Next.js vs. Vite+React+FastAPI

| Criterion | Next.js (Chosen) | Vite+React+FastAPI | Reasoning |
|-----------|-----------------|-------------------|-----------|
| **Deployment** | Single Vercel deploy | Frontend (Vercel) + Backend (Hetzner/Railway) | Next.js: Zero infra management, single URL |
| **API Routes** | Built-in (App Router) | Separate FastAPI server | Next.js: No CORS, no separate deploy |
| **Database** | Vercel Postgres (serverless) | PostgreSQL on Hetzner | Next.js: Free tier, auto-scaling |
| **SSR/SEO** | Native | Client-side only (unless SSR added) | Not critical for 2-user admin app |
| **Dev Complexity** | Single codebase | Two codebases (frontend + backend) | Next.js: Simpler for small team |
| **Cost** | $0 (free tier) | $0 frontend + $5-20 backend | Next.js: Cheaper |
| **Omar's Platform** | NOT part of platform | Aligns with Vite+FastAPI stack | This is a CLIENT project, not platform |
| **Scalability** | 2-10 users max (Vercel free tier) | 100+ users (dedicated backend) | Villa Thaifa = 2 users (Omar + Said) |

**Decision**: Next.js wins for THIS project. If Omar builds a multi-client property management PLATFORM later, revisit Vite+FastAPI.

---

## Layer-by-Layer Decisions

### 1. Framework: Next.js 15 (App Router)

**Alternatives Considered**: Vite+React, Remix, Nuxt.js, SvelteKit

**Why Next.js**:
- ✅ Vercel-native (zero-config deployment)
- ✅ API routes built-in (no separate backend)
- ✅ Server-side rendering (fast initial load for Said's mobile)
- ✅ App Router = modern patterns (server components, streaming)
- ✅ next-intl for French/English SSR
- ✅ Huge ecosystem (shadcn/ui, Zod, NextAuth)

**Why NOT Vite+React**:
- ❌ Requires separate backend (FastAPI or Node.js)
- ❌ Two deploys (frontend + backend)
- ❌ CORS configuration needed
- ❌ More complex for 2-user app

**Trade-off**: Next.js locks us into Vercel ecosystem. If we outgrow Vercel, migration to self-hosted is harder than Vite+FastAPI. **Acceptable** because Villa Thaifa will stay small (2-10 users max).

---

### 2. Database: Vercel Postgres (Neon)

**Alternatives Considered**: Supabase Postgres, PlanetScale (MySQL), SQLite (existing), MongoDB

**Why Vercel Postgres**:
- ✅ Free tier: 256MB storage, 60 hours compute/month
- ✅ Serverless-compatible (Next.js API routes are serverless)
- ✅ Standard SQL (PostgreSQL 15+)
- ✅ Auto-backups, point-in-time recovery
- ✅ Vercel integration (env vars auto-injected)
- ✅ Scales if Villa Thaifa grows

**Why NOT SQLite** (existing in old project):
- ❌ Doesn't work on Vercel serverless (ephemeral filesystem)
- ❌ No concurrent writes (problematic for HotelRunner sync)
- ❌ No built-in backups

**Why NOT Supabase**:
- ❌ Another vendor (Vercel Postgres keeps everything in one ecosystem)
- ❌ Slightly more complex auth integration

**Trade-off**: Vendor lock-in to Vercel. If we migrate off Vercel, need to migrate database too. **Acceptable** for a 2-user app prioritizing speed over portability.

---

### 3. Auth: NextAuth.js + Magic Links

**Alternatives Considered**: Clerk, Supabase Auth, Auth0, Custom JWT

**Why NextAuth.js + Magic Links**:
- ✅ Said is 78 years old — no password friction
- ✅ Email → click → logged in (simplest UX)
- ✅ Free (no vendor cost)
- ✅ Next.js native integration
- ✅ Session management built-in
- ✅ Role-based access (Omar = admin, Said = owner)

**Why NOT Clerk**:
- ❌ $25/month after free tier (100 MAU)
- ❌ Overkill for 2 users

**Why NOT Custom JWT**:
- ❌ Security complexity (token rotation, refresh logic)
- ❌ Manual email sending (need SMTP config)

**Trade-off**: Magic links require reliable email delivery. Said's Hotmail (said_thaifa@hotmail.fr) may have delays. **Mitigation**: Test email delivery in Phase 2, add SMS backup if needed.

---

### 4. UI: shadcn/ui + Tailwind CSS

**Alternatives Considered**: Material UI, Chakra UI, Ant Design, Custom CSS

**Why shadcn/ui**:
- ✅ Copy-paste components (not npm dependency — owns the code)
- ✅ Accessible by default (WCAG AA compliant)
- ✅ Mobile-responsive (critical for Said's phone usage)
- ✅ Dark mode support (Omar's preference)
- ✅ Tailwind CSS (utility-first, fast development)
- ✅ TypeScript-first

**Why NOT Material UI**:
- ❌ Heavy bundle size (slower mobile load)
- ❌ Opinionated design (harder to customize)

**Why NOT Custom CSS**:
- ❌ Slower development (no pre-built components)
- ❌ Accessibility requires manual work

**Trade-off**: shadcn/ui = more code to maintain (copy-paste vs. npm). **Acceptable** because we control the code and can customize freely.

---

### 5. i18n: next-intl

**Alternatives Considered**: react-i18next, next-translate, custom solution

**Why next-intl**:
- ✅ Server-side rendering (fast initial load)
- ✅ Next.js App Router optimized
- ✅ Type-safe translations (TypeScript autocomplete)
- ✅ Namespace support (separate UI vs. content strings)
- ✅ French primary, English secondary (exactly our use case)

**Why NOT react-i18next**:
- ❌ Client-side only (slower initial render for Said's mobile)

**Trade-off**: None. next-intl is the clear winner for Next.js SSR + i18n.

---

### 6. Validation: Zod

**Alternatives Considered**: Yup, Joi, class-validator

**Why Zod**:
- ✅ Already used in existing project (migration continuity)
- ✅ TypeScript-first (type inference from schema)
- ✅ Works with React Hook Form (best form library for Next.js)
- ✅ Server-side + client-side validation
- ✅ Excellent error messages (French translations possible)

**Trade-off**: None. Zod is industry standard for TypeScript validation.

---

### 7. OTA Integration: HotelRunner API (Custom REST Wrapper)

**Alternatives Considered**: Direct OTA APIs, SiteMinder, Cloudbeds, browser automation (existing)

**Why HotelRunner API**:
- ✅ Said already uses HotelRunner actively (proven integration)
- ✅ 150+ OTA integrations (Booking.com, Expedia, Airbnb, Agoda, Trip.com)
- ✅ Dual API (REST + XML/SOAP)
- ✅ Real-time push webhooks (reservations don't count against rate limit)
- ✅ Preferred Connectivity Partner (Expedia, Booking.com, Airbnb)

**Why NOT direct OTA APIs**:
- ❌ 5 separate integrations (Booking.com, Expedia, Airbnb, Agoda, Trip.com)
- ❌ Each has different auth, rate limits, data formats
- ❌ Maintenance nightmare

**Why NOT browser automation** (existing approach):
- ❌ Broken auth persistence (requires daily manual login)
- ❌ Fragile (breaks when HotelRunner UI changes)
- ❌ No API-level error handling

**Trade-off**: HotelRunner rate limits (250 req/day, 5 req/min) are restrictive. **Mitigation**: Implement local caching + batch updates to stay under 100 req/day.

**HotelRunner Research**: See `~/omar/knowledge/research/business/hotelrunner-platform-research.md` for full analysis.

---

### 8. Exchange Rate: Auto-Fetch API

**Alternatives Considered**: Manual .env update, hardcoded rate, database-stored rate

**Why Auto-Fetch API**:
- ✅ EUR/MAD rate changes daily (manual = outdated pricing)
- ✅ Free tier APIs available (ExchangeRate-API.com, fixer.io)
- ✅ Caching (fetch 1x/day, store in Vercel KV or database)
- ✅ Fallback to last-known rate if API fails

**API Options** (TBD in Phase 1):

| API | Free Tier | Rate Limit | Reliability | Notes |
|-----|-----------|-----------|-------------|-------|
| ExchangeRate-API.com | 1,500 req/month | 1 req/day needed | High | Simple JSON API |
| fixer.io | 100 req/month | 1 req/day needed | Medium | Requires signup |
| Open Exchange Rates | 1,000 req/month | 1 req/day needed | High | More currencies |

**Decision**: ExchangeRate-API.com (simplest, most generous free tier). Finalize in Phase 1.

---

### 9. Deployment: Vercel (Free Tier)

**Alternatives Considered**: Hetzner VPS, Railway, Render, Netlify

**Why Vercel**:
- ✅ Free tier: Unlimited bandwidth, 100GB-hours compute/month
- ✅ Zero infra management (no server config, no SSH)
- ✅ Auto-deploy on git push (CI/CD built-in)
- ✅ Preview deployments (test before production)
- ✅ Next.js optimized (built by same company)
- ✅ Edge functions (fast for global users, though Villa Thaifa is Morocco-only)
- ✅ Said gets a URL (`villa-thaifa-pms.vercel.app`) — works on mobile

**Why NOT Hetzner VPS**:
- ❌ Requires server management (Omar's time)
- ❌ No auto-scaling (fixed resources)
- ❌ Manual SSL setup (Vercel = automatic HTTPS)

**Cost**: $0/month on free tier. Upgrade to Vercel Pro ($20/mo) only if:
- Analytics needed (free tier = basic only)
- Bandwidth exceeds free tier (unlikely for 2 users)
- Custom domain needed (villa-thaifa.com) — can add later

---

### 10. Monitoring: Vercel Analytics (Free Tier)

**Alternatives Considered**: Google Analytics, Plausible, Mixpanel, Custom logging

**Why Vercel Analytics**:
- ✅ Free tier: Basic page views, web vitals
- ✅ Zero config (auto-enabled on Vercel)
- ✅ Privacy-friendly (no cookies, GDPR compliant)
- ✅ Core Web Vitals tracking (mobile performance for Said)

**Why NOT Google Analytics**:
- ❌ Overkill for 2 users
- ❌ Cookie consent required (GDPR)
- ❌ More complex setup

**Upgrade Path**: If we need error tracking (Sentry) or user session replay (LogRocket), add in Phase 4.

---

### 11. Room Photos: Cloudinary or Vercel Image Optimization

**Alternatives Considered**: Store in git, S3, Vercel Blob Storage, HotelRunner only

**Why Cloudinary**:
- ✅ Free tier: 25GB storage, 25GB bandwidth/month
- ✅ Auto-resize, auto-format (WebP for modern browsers)
- ✅ CDN built-in (fast load for Said's mobile)
- ✅ Upload API (can integrate with HotelRunner photo sync)

**Why Vercel Image Optimization** (alternative):
- ✅ Built into Next.js (`<Image>` component)
- ✅ Auto-resize, lazy load, WebP
- ❌ Requires images stored in Vercel Blob Storage ($0.15/GB)

**Decision**: Cloudinary for Phase 2 (more generous free tier). Can switch to Vercel Blob if we exceed Cloudinary limits.

---

## Cost Breakdown (Monthly)

| Service | Tier | Cost | Notes |
|---------|------|------|-------|
| Vercel (hosting) | Free | $0 | Unlimited bandwidth, 100GB-hours compute |
| Vercel Postgres (Neon) | Free | $0 | 256MB storage, 60 hours compute |
| NextAuth.js | — | $0 | Open-source |
| Cloudinary | Free | $0 | 25GB storage, 25GB bandwidth |
| ExchangeRate-API.com | Free | $0 | 1,500 req/month |
| **Total** | — | **$0** | No recurring cost |

**Upgrade Path** (if needed):
- Vercel Pro: $20/month (analytics, custom domains, higher limits)
- Neon Pro: $19/month (more storage, more compute)
- Cloudinary Pro: $89/month (more bandwidth, video support)

**Trigger for Upgrade**: If Villa Thaifa grows to 5+ properties or 10+ users.

---

## Why NOT Vite + React + FastAPI? (Detailed Rationale)

Omar's platform stack (from `~/omar/specs/stack/tech-stack.md` v3.0.0) is:
- **Frontend**: Vite + React + Tailwind
- **Backend**: FastAPI + PostgreSQL + pgvector

**Why this doesn't apply to Villa Thaifa**:

1. **Villa Thaifa is a CLIENT project**, not Omar's platform
2. **2 users (Omar + Said)**, not multi-tenant SaaS
3. **Single deployment** is simpler than frontend + backend
4. **No AI/ML features** (pgvector not needed)
5. **No double-backend risk** because there IS no other backend

**When to use Vite+FastAPI**:
- Multi-client property management platform (10+ hotels)
- AI-powered features (pricing optimization, demand forecasting)
- Mobile app needed (React Native + FastAPI API)
- Shared backend for multiple frontends

**For Villa Thaifa**: Next.js is the pragmatic choice. Speed to production > architectural purity.

---

## Future-Proofing Considerations

### If Villa Thaifa Outgrows Next.js (Unlikely)

**Triggers**:
- 10+ properties (multi-tenant needed)
- 100+ users (Vercel free tier insufficient)
- Complex AI features (pricing optimization, demand forecasting)

**Migration Path**:
1. Keep Next.js frontend (Vite migration not needed)
2. Extract API routes to FastAPI backend (gradual migration)
3. Deploy FastAPI on Hetzner ($5-20/month)
4. Postgres stays on Neon or migrate to Hetzner
5. Keep Vercel for frontend (static deploy)

**Cost**: ~6-12 months dev time to migrate. Not worth it unless revenue justifies.

---

## Tech Stack Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Vercel vendor lock-in** | Hard to migrate off Vercel | Acceptable for 2-user app. If needed, Next.js can self-host. |
| **Hotmail delays (magic links)** | Said can't log in | Test in Phase 2. Add SMS backup if needed. |
| **HotelRunner rate limits** | Sync fails, stale data | Cache locally, batch updates, stay under 100 req/day. |
| **Exchange rate API downtime** | Wrong MAD pricing | Cache last-known rate, fallback to manual .env. |
| **Cloudinary free tier exceeded** | Photos stop loading | Monitor usage, upgrade to Pro ($89/mo) or switch to Vercel Blob. |
| **Next.js breaking changes** | App breaks on upgrade | Pin Next.js version, test upgrades in preview deploy. |

---

## Changelog

### 2026-02-13 — Initial Tech Decisions
- Chose Next.js over Vite+FastAPI (client project, not platform)
- Chose Vercel Postgres over Supabase (ecosystem consistency)
- Chose magic links over password auth (Said's age, UX)
- Chose Cloudinary over Vercel Blob (more generous free tier)
- Deferred exchange rate API decision to Phase 1 (3 options evaluated)

### 2026-02-10 — Tech Stack Research
- Evaluated 4 frameworks (Next.js, Vite+React, Remix, SvelteKit)
- Evaluated 3 databases (Vercel Postgres, Supabase, PlanetScale)
- Evaluated 2 auth solutions (NextAuth, Clerk)
- Decided on Next.js + Vercel ecosystem for simplicity

---

_These decisions are FROZEN for Phase 0-2. Re-evaluate in Phase 3 only if blockers emerge._
