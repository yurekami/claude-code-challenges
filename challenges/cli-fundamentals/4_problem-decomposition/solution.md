# Solution: Problem Decomposition Mastery

## Framework Application: Blog System

Let's apply the decomposition framework to our practice problem.

### Step 1: Identify the Goal

**Goal**: A functional blog platform where users can register, authenticate, create posts, comment, and admins can manage content.

### Step 2: List Major Components

1. **Foundation**: Database, project structure, dependencies
2. **Authentication**: User registration, login, session management
3. **Core Blog**: Post CRUD operations
4. **Social Features**: Comments, likes, shares
5. **User Experience**: Profiles, search, notifications
6. **Media**: Image uploads and management
7. **Admin**: Dashboard and moderation tools

### Step 3: Break Down Each Component

#### Foundation
- Set up project structure (Next.js/Express/etc.)
- Configure database (PostgreSQL/MongoDB)
- Set up ORM (Prisma/TypeORM)
- Create initial database schema
- Configure environment variables

#### Authentication
- Implement user registration endpoint
- Implement login endpoint with JWT
- Add password hashing with bcrypt
- Create auth middleware
- Add refresh token mechanism
- Implement logout functionality

#### Core Blog
- Create posts table schema
- Implement create post endpoint
- Implement read post endpoint (single + list)
- Implement update post endpoint
- Implement delete post endpoint
- Add post ownership validation

#### Social Features
- Create comments table schema
- Implement comment CRUD endpoints
- Add comment ownership validation
- Create likes system
- Add comment threading (optional)

#### User Experience
- Create user profile schema
- Implement profile view endpoint
- Implement profile update endpoint
- Add search functionality for posts
- Create email notification service
- Implement notification triggers

#### Media
- Configure file storage (S3/local)
- Implement image upload endpoint
- Add image validation and resizing
- Link images to posts
- Handle image deletion

#### Admin
- Create admin role system
- Build admin dashboard UI
- Implement user management
- Add content moderation tools
- Create analytics/stats view

### Step 4: Identify Dependencies

```
Foundation
    ↓
Authentication (needs database)
    ↓
Core Blog (needs auth)
    ↓
├─→ Social Features (needs posts & auth)
├─→ User Experience (needs posts & auth)
├─→ Media (needs posts)
└─→ Admin (needs all of above)
```

### Step 5: Sequence Tasks

**Phase 1: Foundation (Days 1-2)**
1. Initialize project with Next.js + TypeScript
2. Set up PostgreSQL database
3. Configure Prisma ORM
4. Create initial schema (users, posts, comments)
5. Run migrations and verify database

**Phase 2: Authentication (Days 3-4)**
6. Implement user registration with validation
7. Add password hashing and storage
8. Create login endpoint with JWT generation
9. Build auth middleware for protected routes
10. Add refresh token mechanism
11. Test authentication flow end-to-end

**Phase 3: Core Blog (Days 5-7)**
12. Create post creation endpoint
13. Implement post listing with pagination
14. Add single post view endpoint
15. Build post update endpoint with ownership check
16. Implement post deletion with ownership check
17. Add draft/published status system

**Phase 4: Social Features (Days 8-9)**
18. Create comments table and endpoints
19. Add comment ownership validation
20. Implement likes system
21. Add comment threading (1 level deep)

**Phase 5: Polish (Days 10-12)**
22. Implement user profiles
23. Add post search functionality
24. Create email notification service
25. Add image upload for posts
26. Build basic admin dashboard

### Step 6: Size Check

Each task should take 15-30 minutes:
- ✓ Task 1: "Initialize project with Next.js + TypeScript" (~20 min)
- ✓ Task 6: "Implement user registration with validation" (~25 min)
- ✓ Task 12: "Create post creation endpoint" (~30 min)

## TodoWrite Implementation

Here's how to structure this in Claude Code:

```markdown
# Blog System Implementation

## Phase 1: Foundation
- [ ] Initialize Next.js project with TypeScript and ESLint
- [ ] Install and configure Prisma ORM
- [ ] Set up PostgreSQL database locally
- [ ] Create Prisma schema for users, posts, comments tables
- [ ] Run initial migration and verify database connection

## Phase 2: Authentication
- [ ] Create user registration API route with Zod validation
- [ ] Implement password hashing using bcrypt
- [ ] Build login endpoint that generates JWT tokens
- [ ] Create auth middleware to verify JWT tokens
- [ ] Add refresh token mechanism for long-lived sessions
- [ ] Test authentication flow with Postman/curl

## Phase 3: Core Blog
- [ ] Create POST /api/posts endpoint with auth middleware
- [ ] Implement GET /api/posts with pagination
- [ ] Build GET /api/posts/:id for single post view
- [ ] Add PUT /api/posts/:id with ownership validation
- [ ] Implement DELETE /api/posts/:id with ownership check
- [ ] Add draft/published status field and filtering

## Phase 4: Social Features
- [ ] Create comments schema and migration
- [ ] Implement POST /api/posts/:id/comments endpoint
- [ ] Add GET /api/posts/:id/comments with pagination
- [ ] Build likes system (schema + endpoints)
- [ ] Add comment threading support (1 level)

## Phase 5: Polish
- [ ] Create user profile schema and endpoints
- [ ] Implement full-text search for posts
- [ ] Set up email service (SendGrid/Mailgun)
- [ ] Add image upload with multer/S3
- [ ] Build basic admin dashboard UI
```

## Execution Strategy

### Session 1: Foundation
```bash
claude

# Message to Claude:
"I'm building a blog system. Let's start with the foundation.

Task 1: Initialize a Next.js 14 project with:
- TypeScript
- ESLint with strict rules
- Tailwind CSS for styling
- App router (not pages)

Please create the project structure and show me the package.json."
```

### Session 2: Database Setup
```bash
# Continue or new session if needed

"Task 2: Set up Prisma ORM with PostgreSQL.

Create a schema with three models:
1. User (id, email, password, name, createdAt)
2. Post (id, title, content, authorId, published, createdAt)
3. Comment (id, content, authorId, postId, createdAt)

Include proper relations. Show me the schema file."
```

### Session 3: First Feature
```bash
"Task 3: Implement user registration.

Create /api/auth/register that:
- Accepts email, password, name
- Validates with Zod (email format, password min 8 chars)
- Hashes password with bcrypt
- Creates user in database
- Returns user object (without password)

Show me the implementation."
```

## Real-World Example: E-commerce Site

Let's decompose another complex problem.

**Problem**: Build an e-commerce site

### Quick Decomposition

**Major Components**:
1. Product catalog
2. Shopping cart
3. Checkout & payment
4. Order management
5. User accounts
6. Admin panel

**Sequenced Tasks** (15 core tasks):
1. Set up project and database
2. Create product schema and seed data
3. Build product listing page
4. Add product detail page
5. Implement shopping cart (client state)
6. Create cart persistence (database)
7. Build checkout form
8. Integrate payment gateway (Stripe)
9. Create order schema and endpoints
10. Implement order confirmation
11. Add user registration/login
12. Build user order history
13. Create admin product management
14. Add admin order management
15. Implement inventory tracking

**Dependency Chain**:
```
Setup (1) → Products (2,3,4) → Cart (5,6) → Checkout (7,8,9,10) → Users (11,12) → Admin (13,14,15)
```

## Advanced Decomposition Techniques

### Technique 1: Vertical Slicing

Instead of building all backend, then all frontend:

❌ **Horizontal**:
1. All database schemas
2. All API endpoints
3. All UI components
4. All integration

✓ **Vertical**:
1. User registration: DB → API → UI → Test
2. User login: DB → API → UI → Test
3. Post creation: DB → API → UI → Test

**Benefits**:
- Each slice is a complete, testable feature
- Early feedback on full stack
- Visible progress for stakeholders

### Technique 2: Complexity-Based Ordering

Order tasks by complexity:

**Easy → Medium → Hard**:
1. Read operations (easiest)
2. Create operations
3. Update operations
4. Delete operations
5. Complex business logic (hardest)

**Why**: Build confidence, establish patterns, tackle hard parts when you're warmed up

### Technique 3: Risk-First Decomposition

Identify high-risk/uncertain parts and tackle them first:

**Example**:
1. ⚠️ Stripe payment integration (unknown)
2. ⚠️ Image upload to S3 (never done)
3. ✓ User CRUD (familiar)
4. ✓ Basic UI (familiar)

**Why**: Fail fast, adjust plan based on real constraints

### Technique 4: Dependency Mapping

Create a visual dependency graph:

```
        [Database Setup]
              ↓
        [User Auth] ← [Email Service]
         ↓       ↓
    [Posts]  [Profiles]
       ↓         ↓
  [Comments] [Settings]
       ↓         ↓
    [Likes]  [Notifications]
         ↓     ↓
       [Admin Panel]
```

**Why**: Prevents starting tasks that have unmet dependencies

## Common Mistakes and Solutions

### Mistake 1: Skipping the Decomposition
**Symptom**: "Help me build a blog system"

**Problem**: Too vague, Claude doesn't know where to start

**Solution**:
```
Instead: "I want to build a blog system. First, let's create
a task breakdown. The system needs authentication, post CRUD,
comments, and an admin panel. Can you help me decompose this
into 15-20 specific tasks with dependencies?"
```

### Mistake 2: Over-Decomposition
**Symptom**: "Task 47: Add a semicolon on line 92"

**Problem**: Tasks too small, overhead exceeds value

**Solution**: Combine micro-tasks into meaningful chunks
- ❌ 50 tiny tasks
- ✓ 15 substantial tasks

### Mistake 3: Under-Decomposition
**Symptom**: "Task 1: Build the entire frontend"

**Problem**: Task too large, will hit context limits

**Solution**: Break into feature-sized pieces
- ❌ "Build frontend"
- ✓ "Build login form component with validation"

### Mistake 4: Ignoring Dependencies
**Symptom**: "Let's start with the admin dashboard"

**Problem**: Admin needs auth, posts, users, etc.

**Solution**: Build foundation first, complex features last

### Mistake 5: No Verification Steps
**Symptom**: Building 10 features without testing any

**Problem**: Bugs compound, hard to debug

**Solution**: Test after each task or small group of tasks

## Decomposition Checklist

Before starting work:

- [ ] Goal is clearly defined
- [ ] Major components identified (3-7 components)
- [ ] Each component broken into tasks (3-5 tasks each)
- [ ] Each task is appropriately sized (15-30 min)
- [ ] Dependencies are mapped
- [ ] Tasks are sequenced logically
- [ ] High-risk tasks identified
- [ ] Verification steps included

## Practice Exercises

### Exercise 1: Social Media App
Decompose a Twitter-like app with:
- User profiles
- Posts (tweets)
- Follow system
- Feed algorithm
- Likes and retweets
- Direct messages
- Notifications

**Goal**: 20 tasks, properly sequenced

### Exercise 2: Project Management Tool
Decompose a Trello-like app with:
- Boards, lists, cards
- Drag and drop
- User assignments
- Comments and attachments
- Team workspaces
- Activity log

**Goal**: 25 tasks with dependency map

### Exercise 3: Your Real Project
Take something you're actually building:
- Write down the full vision
- Apply the decomposition framework
- Create TodoWrite list
- Execute first 5 tasks
- Reflect on the process

## Success Indicators

You've mastered problem decomposition when you:

- Instinctively break down complex problems before coding
- Can estimate task sizes accurately (within 20%)
- Identify dependencies without conscious effort
- Rarely encounter blocked tasks
- Complete tasks sequentially without backtracking
- Maintain context efficiency (<60% usage per phase)
- Deliver features incrementally
- Can explain your decomposition rationale

## Quick Reference: The Decomposition Process

```
1. STATE THE GOAL
   "Build a [system] that [does X, Y, Z]"

2. LIST COMPONENTS
   "This requires: [A], [B], [C], [D], [E]"

3. BREAK DOWN
   Component A:
     - Task A1
     - Task A2
     - Task A3
   (Repeat for each component)

4. MAP DEPENDENCIES
   "A1 must complete before B1"
   "C1, C2, C3 can be parallel"

5. SEQUENCE
   Phase 1: [Foundation tasks]
   Phase 2: [Core features]
   Phase 3: [Advanced features]
   Phase 4: [Polish]

6. VERIFY SIZING
   Each task = 15-30 minutes
   Too big? Split it.
   Too small? Combine.

7. EXECUTE
   One task at a time
   Test after each task
   Adjust plan as needed
```

## Final Tips

1. **Start Simple**: Get the simple version working first
2. **Iterate**: Decompose → Execute → Reflect → Adjust
3. **Document**: Keep your decomposition visible
4. **Be Flexible**: Adjust as you learn more
5. **Celebrate Progress**: Each completed task is a win
