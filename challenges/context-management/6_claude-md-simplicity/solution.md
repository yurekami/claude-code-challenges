# Solution: CLAUDE.md Simplicity

## Step-by-Step Solution

### Step 1: Understand CLAUDE.md Purpose

**What CLAUDE.md IS:**
- Quick reference for current project state
- Essential context loaded in every conversation
- High-level overview and key constraints
- Navigation guide to detailed docs

**What CLAUDE.md IS NOT:**
- Complete project documentation
- Detailed implementation guide
- Historical record of decisions
- Comprehensive API reference
- Full coding standards guide

### Step 2: The Minimalist Template

Here's an optimal CLAUDE.md structure (~500-800 tokens):

```markdown
# [Project Name]

[One sentence description of what this project does]

## Stack
[Tech stack in table or bullet points - 50-100 tokens]

## Quick Start
```bash
npm install
npm run dev
```

## Structure
```
src/
├── app/      # [brief description]
├── lib/      # [brief description]
└── components/ # [brief description]
```

## Key Constraints
- [Critical constraint 1]
- [Critical constraint 2]
- [Critical constraint 3]

## Current Focus
[What's currently being worked on - updated regularly]

## Docs
- Architecture: `docs/architecture.md`
- API Reference: `docs/api.md`
- Contributing: `CONTRIBUTING.md`
```

**This gives:**
- Project identity
- Tech stack
- How to start
- Code organization
- Critical rules
- Current state
- Where to find more info

### Step 3: Real-World Optimization

**BEFORE (8,000 tokens) - Too much detail:**

```markdown
# E-commerce Platform

This is a comprehensive e-commerce platform built using modern web
technologies. The platform supports multiple vendors, product
catalogs, shopping cart functionality, payment processing, and
order management.

## Technology Stack

### Frontend
We are using Next.js 14 with the App Router for the frontend. Next.js
was chosen because it provides excellent performance characteristics
through server-side rendering and static generation. The App Router
is the new routing paradigm that was introduced in Next.js 13 and
significantly improved in version 14.

Key features of our Next.js setup:
- Server Components by default for optimal performance
- Client Components only when interactivity is needed
- Streaming for progressive page loading
- Automatic code splitting
- Image optimization with next/image

[... 7,500 more tokens of similar verbose content ...]

## API Endpoints

### Products

#### GET /api/products
Retrieves a list of products with optional filtering and pagination.

**Query Parameters:**
- `page` (number, optional): Page number for pagination. Default: 1
- `limit` (number, optional): Number of items per page. Default: 20. Max: 100
- `category` (string, optional): Filter by category ID
- `search` (string, optional): Search products by name or description
- `sort` (string, optional): Sort field. Options: 'name', 'price', 'created_at'
- `order` (string, optional): Sort order. Options: 'asc', 'desc'

**Response:**
```json
{
  "products": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

[... continues with 20 more endpoints in similar detail ...]

## Database Schema

### Products Table
```sql
CREATE TABLE products (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
  stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
  category_id UUID REFERENCES categories(id),
  vendor_id UUID REFERENCES vendors(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_vendor ON products(vendor_id);
CREATE INDEX idx_products_name ON products(name);
```

[... 15 more tables with full schemas ...]

## Coding Standards

[... 2,000 tokens of coding standards that could be in separate file ...]

## Deployment Process

[... 1,500 tokens of deployment docs ...]
```

**AFTER (800 tokens) - Essential only:**

```markdown
# E-commerce Platform

Multi-vendor marketplace with products, cart, payments, orders.

## Stack
| Layer | Tech |
|-------|------|
| Frontend | Next.js 14 (App Router), React 18, Tailwind |
| Backend | Next.js API routes, tRPC |
| Database | PostgreSQL 16, Prisma ORM |
| Auth | NextAuth.js (JWT) |
| Payments | Stripe |
| Hosting | Vercel |

## Quick Start
```bash
npm install
cp .env.example .env  # Add STRIPE_KEY, DATABASE_URL
npm run db:migrate
npm run dev           # localhost:3000
```

## Structure
```
src/
├── app/             # Next.js App Router (pages, layouts)
│   ├── (shop)/      # Public shopping routes
│   ├── (vendor)/    # Vendor dashboard
│   └── api/         # API routes
├── lib/
│   ├── db/          # Prisma client, queries
│   ├── stripe/      # Payment utilities
│   └── auth/        # Auth helpers
└── components/      # Shared React components
```

## Key Constraints
- **Auth:** JWT tokens (15m access, 7d refresh)
- **Payments:** All via Stripe, no custom payment handling
- **Images:** Max 5MB, processed via next/image
- **Rate limits:** 100 req/hr per user, 1000/hr per vendor
- **Database:** All queries via Prisma, no raw SQL
- **Server components default:** Client only for interactivity

## Current Focus
**Sprint:** Payment flow improvements
- Webhook handling for async payment confirmation
- Refund workflow
- See: `docs/sprints/2025-w03.md`

## Architecture Decisions
- **Monorepo vs separate:** Monorepo (simpler at current scale)
- **SSR vs SPA:** SSR for SEO, product pages
- **Auth strategy:** JWT for API, sessions for web
- See: `docs/decisions/` for full ADRs

## Documentation
- **API Reference:** `docs/api.md` (OpenAPI spec)
- **Database:** `docs/database.md` (ER diagram, migrations)
- **Architecture:** `docs/architecture.md` (C4 diagrams)
- **Deployment:** `docs/deployment.md`
- **Contributing:** `CONTRIBUTING.md`

## Common Commands
```bash
npm run dev              # Development
npm run build            # Production build
npm run test             # Run tests
npm run db:studio        # Prisma Studio (DB GUI)
npm run db:migrate       # Run migrations
npm run stripe:listen    # Stripe webhook testing
```

## Environment Variables
See `.env.example` for required vars. Key ones:
- `DATABASE_URL` - PostgreSQL connection
- `NEXTAUTH_SECRET` - Auth signing key
- `STRIPE_SECRET_KEY` - Stripe API key
- `STRIPE_WEBHOOK_SECRET` - Webhook validation
```

**Result: 8,000 → 800 tokens (90% reduction)**

### Step 4: Content Migration Strategy

**Create a docs/ structure for detailed content:**

```
project/
├── .claude/
│   └── CLAUDE.md            # 800 tokens - essentials only
├── docs/
│   ├── api.md               # Detailed API reference
│   ├── database.md          # Schema, ER diagrams
│   ├── architecture.md      # System design, C4 diagrams
│   ├── deployment.md        # Deploy process
│   ├── decisions/           # ADRs (Architecture Decision Records)
│   │   ├── 001-jwt-auth.md
│   │   ├── 002-stripe-payments.md
│   │   └── 003-monorepo.md
│   └── sprints/             # Sprint planning
│       ├── 2025-w03.md
│       └── 2025-w04.md
├── CONTRIBUTING.md          # How to contribute
└── README.md                # Public-facing readme
```

**Migration checklist:**

```markdown
## Content to Move Out of CLAUDE.md

### To docs/api.md
- [ ] Endpoint specifications
- [ ] Request/response examples
- [ ] Error codes
- [ ] Rate limiting details

### To docs/database.md
- [ ] Full schema definitions
- [ ] ER diagrams
- [ ] Migration history
- [ ] Indexing strategy

### To docs/architecture.md
- [ ] System diagrams
- [ ] Component interactions
- [ ] Data flow diagrams
- [ ] Scaling strategy

### To docs/deployment.md
- [ ] CI/CD pipeline
- [ ] Environment setup
- [ ] Release process
- [ ] Rollback procedures

### To docs/decisions/
- [ ] Why JWT over sessions
- [ ] Why Stripe over PayPal
- [ ] Why monorepo
- [ ] Technology choices

### Keep in CLAUDE.md
- [x] One-line project description
- [x] Tech stack table
- [x] Quick start commands
- [x] Directory structure overview
- [x] Key constraints (3-5 critical ones)
- [x] Current focus/sprint
- [x] Links to detailed docs
```

### Step 5: Optimization Techniques

#### Technique 1: Use Tables

**Instead of:**
```markdown
The frontend uses Next.js 14 with the App Router. For the backend,
we're using Next.js API routes with tRPC. The database is PostgreSQL
16 with Prisma as the ORM. For authentication, we use NextAuth.js
with JWT tokens. Payments are handled by Stripe. The application is
hosted on Vercel.
```

**Use:**
```markdown
| Layer | Tech |
|-------|------|
| Frontend | Next.js 14 (App Router) |
| Backend | Next.js API + tRPC |
| Database | PostgreSQL 16 + Prisma |
| Auth | NextAuth.js (JWT) |
| Payments | Stripe |
| Hosting | Vercel |
```

**Savings: ~150 → 80 tokens, better scannability**

#### Technique 2: Directory Tree Comments

**Instead of:**
```markdown
The app directory contains all the Next.js App Router files including
pages and layouts. Within app, there are three main sections: shop for
public shopping routes, vendor for the vendor dashboard, and api for
API routes. The lib directory contains all our utility functions and
helpers, organized into subdirectories for database operations, Stripe
integration, and authentication. The components directory has all our
shared React components.
```

**Use:**
```markdown
```
src/
├── app/             # App Router (pages, layouts)
│   ├── (shop)/      # Public routes
│   ├── (vendor)/    # Vendor dashboard
│   └── api/         # API routes
├── lib/             # Utilities
│   ├── db/          # Prisma client
│   ├── stripe/      # Payments
│   └── auth/        # Auth helpers
└── components/      # Shared components
```
```

**Savings: ~180 → 60 tokens**

#### Technique 3: Reference, Don't Repeat

**Instead of:**
```markdown
## Authentication

We use JWT tokens for authentication. Access tokens expire after
15 minutes and refresh tokens expire after 7 days. The tokens are
signed using the NEXTAUTH_SECRET environment variable...

[500+ tokens of auth details]
```

**Use:**
```markdown
## Key Constraints
- **Auth:** JWT (15m access, 7d refresh) - See `docs/auth.md`
```

**Savings: 500+ → 15 tokens**

#### Technique 4: Current Focus Section

Instead of historical context, maintain a living "Current Focus" section:

```markdown
## Current Focus
**Sprint:** Payment improvements (W03 2025)
- Webhook handling for async confirmation
- Refund workflow
- See: `docs/sprints/2025-w03.md`
```

Update this every sprint/phase. It's more useful than project history.

### Step 6: CLAUDE.md Maintenance

**Update triggers:**

1. **Major architectural change**
   ```markdown
   # Before
   ## Stack
   | Backend | Express + REST |

   # After migration
   ## Stack
   | Backend | Next.js + tRPC |
   ```

2. **New critical constraint**
   ```markdown
   ## Key Constraints
   - Auth: JWT tokens
   - Payments: Stripe only
   + Images: Max 5MB, next/image processing  # NEW
   ```

3. **Sprint/phase change**
   ```markdown
   ## Current Focus
   - **Sprint:** Payment improvements  # Update every sprint
   ```

4. **Major directory restructure**
   ```markdown
   # Update structure section when org changes
   ```

**Don't update for:**
- Individual file changes
- Bug fixes
- Minor refactors
- Day-to-day development

**Maintenance schedule:**
- Review weekly
- Update on major changes
- Archive old "Current Focus" to docs/sprints/

### Step 7: Common Patterns by Project Type

#### Pattern A: Full-Stack Web App

```markdown
# [Project Name]
[One-line description]

## Stack
[Table: Frontend, Backend, Database, Auth, Hosting]

## Quick Start
```bash
[3-4 commands to get running]
```

## Structure
```
[Directory tree with comments]
```

## Key Constraints
- [3-5 critical rules]

## Current Focus
[Active sprint/phase]

## Docs
- API: `docs/api.md`
- Architecture: `docs/architecture.md`
```

**Target: 600-800 tokens**

#### Pattern B: Library/Package

```markdown
# [Package Name]
[One-line description]

## Installation
```bash
npm install [package]
```

## Structure
```
[Source directory tree]
```

## Key Constraints
- Zero dependencies
- <5KB gzipped
- Browser + Node support

## Development
```bash
npm test
npm run build
```

## Docs
- API Reference: `docs/api.md`
- Examples: `examples/`
```

**Target: 400-600 tokens**

#### Pattern C: API/Backend Service

```markdown
# [Service Name]
[One-line description]

## Stack
[Table: Runtime, Framework, Database, Deployment]

## Quick Start
```bash
[Setup commands]
```

## Endpoints
High-level routes:
- `GET /api/v1/users` - User operations
- `GET /api/v1/products` - Product catalog
- `POST /api/v1/orders` - Order processing

Full spec: `docs/api.md` (OpenAPI)

## Key Constraints
- [Auth, rate limits, etc.]

## Docs
- API Reference: `docs/api.md`
- Database: `docs/database.md`
```

**Target: 500-700 tokens**

## Common Mistakes to Avoid

### Mistake 1: Kitchen Sink Approach

❌ **Wrong:**
```markdown
# Including everything in CLAUDE.md:
- Complete API documentation (2000 tokens)
- Full database schema (1500 tokens)
- Detailed deployment guide (1000 tokens)
- Git workflow (500 tokens)
- Code style guide (800 tokens)
```

✅ **Correct:**
```markdown
# High-level overview in CLAUDE.md (800 tokens):
- Tech stack table
- Quick start
- Directory structure
- Key constraints
- Links to detailed docs
```

### Mistake 2: Static Historical Document

❌ **Wrong:**
```markdown
## Project History
In January 2024, we decided to build this platform...
We considered MongoDB but chose PostgreSQL because...
The original architect was John Doe...
```

✅ **Correct:**
```markdown
## Current Focus
**Sprint W03 2025:** Payment improvements
- Webhook handling
- Refund workflow

See `docs/decisions/` for historical ADRs.
```

### Mistake 3: Duplicating External Docs

❌ **Wrong:**
```markdown
# Repeating what's in package.json
## Dependencies
- next: ^14.0.0
- react: ^18.2.0
- typescript: ^5.3.0
[... 50 more dependencies ...]
```

✅ **Correct:**
```markdown
# Just reference
See `package.json` for dependencies.
```

### Mistake 4: Over-Explaining Obvious Things

❌ **Wrong:**
```markdown
To start the development server, you need to run the npm run dev
command in your terminal. This will start the Next.js development
server on port 3000. You can then open your web browser and navigate
to http://localhost:3000 to view the application.
```

✅ **Correct:**
```markdown
```bash
npm run dev  # localhost:3000
```
```

## Testing Your CLAUDE.md

Start a new conversation and ask Claude:

```
Q1: "What tech stack does this project use?"
→ Should answer from CLAUDE.md immediately

Q2: "How do I start the dev server?"
→ Should answer from CLAUDE.md immediately

Q3: "What's the database schema for products?"
→ Should reference docs/database.md (not directly answer)

Q4: "What are the API endpoints?"
→ Should reference docs/api.md (not list all)

Q5: "What's currently being worked on?"
→ Should answer from "Current Focus" section
```

If Claude can answer Q1, Q2, Q5 immediately and properly reference docs for Q3, Q4, your CLAUDE.md is effective.

## Measuring Success

A successful CLAUDE.md has:
- ✅ 500-1500 tokens (depending on project complexity)
- ✅ Scannable in <30 seconds
- ✅ Answers: "What?", "How to start?", "Where's more info?"
- ✅ Updated with current project state
- ✅ No duplicated information
- ✅ Clear navigation to detailed docs
- ✅ Claude can start work without clarification questions

## Best Practices Summary

1. **Minimal by default** - Only essentials in CLAUDE.md
2. **Reference, don't repeat** - Link to detailed docs
3. **Update regularly** - Keep "Current Focus" current
4. **Use tables** - More scannable, fewer tokens
5. **Directory trees** - Visual structure with inline comments
6. **3-5 key constraints** - Not exhaustive list
7. **Quick start** - 3-4 commands to get running
8. **Current over historical** - Present focus, not project history
9. **Test regularly** - Ensure it provides needed context
10. **Token budget** - Stay under 1500 tokens

## Template: Minimal CLAUDE.md

```markdown
# [Project Name]

[One sentence: what this project does and its primary purpose]

## Stack
| Layer | Tech | Version |
|-------|------|---------|
| [Frontend/Runtime] | [Tech] | [Optional] |
| [Backend/Framework] | [Tech] | [Optional] |
| [Database] | [Tech] | [Optional] |

## Quick Start
```bash
[command 1: install]
[command 2: setup]
[command 3: run]
```

## Structure
```
[key-directory]/
├── [subdirectory]/  # [brief description]
├── [subdirectory]/  # [brief description]
└── [subdirectory]/  # [brief description]
```

## Key Constraints
- [Critical constraint 1]
- [Critical constraint 2]
- [Critical constraint 3]

## Current Focus
**[Phase/Sprint]:** [What's actively being worked on]
- [Key task/goal 1]
- [Key task/goal 2]

## Docs
- [Doc type]: `[path/to/doc]`
- [Doc type]: `[path/to/doc]`
```

**Token target: 500-800**
