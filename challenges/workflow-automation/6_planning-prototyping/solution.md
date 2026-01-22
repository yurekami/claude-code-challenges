# Balance Planning with Prototyping - Solution

## Decision Framework

### When to Prototype First

**Use rapid prototyping when:**

1. **High Uncertainty**
   - New technology/framework
   - Unclear requirements
   - Unknown API behavior
   - Performance concerns

2. **Low Cost of Failure**
   - Throwaway code expected
   - Easy to revert
   - Small isolated feature
   - Personal project

3. **Quick Validation Needed**
   - Client demo/POC
   - Technical feasibility check
   - Competitive pressure
   - Hypothesis testing

**Example Scenarios:**
```
✓ "Can we integrate this payment API?"
✓ "Will this caching strategy improve performance?"
✓ "Does this UI library meet our needs?"
✓ "Is real-time sync feasible?"
```

### When to Plan First

**Use detailed planning when:**

1. **High Cost of Mistakes**
   - Database schema changes
   - Authentication systems
   - Data migration
   - Breaking API changes

2. **Multiple Team Dependencies**
   - Cross-team collaboration
   - Shared infrastructure
   - API contracts
   - Coordinated releases

3. **Complex Systems**
   - Microservices architecture
   - State management
   - Distributed systems
   - Security-critical features

**Example Scenarios:**
```
✓ "Redesigning user authentication"
✓ "Migrating from PostgreSQL to MongoDB"
✓ "Implementing multi-region deployment"
✓ "Refactoring payment processing"
```

### Decision Matrix

| Factor | Prototype First | Plan First |
|--------|----------------|------------|
| **Uncertainty** | High | Low |
| **Risk** | Low | High |
| **Reversibility** | Easy | Hard |
| **Time Pressure** | Immediate | Can wait |
| **Team Size** | Solo/Small | Large |
| **Scope** | Small/Isolated | Large/Integrated |
| **Knowledge** | Learning | Known domain |

## Prototype-First Approach

### Example: Real-Time Notification System

**Initial Requirement:**
"Add real-time notifications to the app"

**Quick Prototype (15 minutes with Claude Code):**

**Step 1: Ask Claude Code**
```
Create a quick prototype for real-time notifications using WebSockets.
Keep it simple - just prove the concept works.
```

**Generated Code:**

```javascript
// server.js - Quick prototype
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('Client connected');

  // Send test notification
  ws.send(JSON.stringify({
    type: 'notification',
    message: 'Welcome!',
    timestamp: Date.now()
  }));

  // Simulate periodic notifications
  const interval = setInterval(() => {
    ws.send(JSON.stringify({
      type: 'notification',
      message: 'Test notification',
      timestamp: Date.now()
    }));
  }, 5000);

  ws.on('close', () => {
    clearInterval(interval);
    console.log('Client disconnected');
  });
});

console.log('WebSocket server running on port 8080');
```

```html
<!-- client.html - Quick test -->
<!DOCTYPE html>
<html>
<head>
  <title>Notification Test</title>
</head>
<body>
  <h1>Real-Time Notifications</h1>
  <div id="notifications"></div>

  <script>
    const ws = new WebSocket('ws://localhost:8080');
    const notifDiv = document.getElementById('notifications');

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      const p = document.createElement('p');
      p.textContent = `[${new Date(data.timestamp).toLocaleTimeString()}] ${data.message}`;
      notifDiv.appendChild(p);
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  </script>
</body>
</html>
```

**Test Results (10 minutes):**
- ✓ WebSockets work in our environment
- ✓ Real-time updates are smooth
- ✓ Connection handling is straightforward
- ✗ Need to handle reconnection
- ✗ Need authentication
- ? How to scale to multiple servers?

**Key Learnings:**
1. WebSockets are viable for our use case
2. Need reconnection logic for production
3. Must integrate with existing auth system
4. Scaling requires additional infrastructure (Redis pub/sub?)

**Decision:** Proceed with implementation, now informed by prototype

### Example: GraphQL vs REST API

**Prototype Both (30 minutes total):**

**REST Prototype (15 min):**
```javascript
// rest-prototype.js
app.get('/api/users/:id', async (req, res) => {
  const user = await db.users.findById(req.params.id);
  const posts = await db.posts.findByUserId(user.id);
  const comments = await db.comments.findByUserId(user.id);

  res.json({ user, posts, comments });
});

// Result: 3 database queries, over-fetching data
```

**GraphQL Prototype (15 min):**
```javascript
// graphql-prototype.js
const typeDefs = `
  type User {
    id: ID!
    name: String!
    posts: [Post]
    comments: [Comment]
  }

  type Query {
    user(id: ID!): User
  }
`;

const resolvers = {
  Query: {
    user: (_, { id }) => db.users.findById(id),
  },
  User: {
    posts: (user) => db.posts.findByUserId(user.id),
    comments: (user) => db.comments.findByUserId(user.id),
  },
};

// Result: More flexible, but adds complexity
```

**Comparison:**
| Aspect | REST | GraphQL |
|--------|------|---------|
| Setup time | 10 min | 20 min |
| Flexibility | Low | High |
| Learning curve | None | Steep |
| Over-fetching | Yes | No |
| Tooling | Mature | Growing |

**Decision:** Stick with REST for now, revisit GraphQL when team is larger

## Plan-First Approach

### Example: User Authentication System

**Detailed Planning (45 minutes):**

**Step 1: Requirements Analysis (10 min)**
```markdown
## Authentication Requirements

### Must Have:
- Email/password login
- JWT token-based auth
- Password reset flow
- Session management
- Role-based access control (RBAC)

### Security:
- Bcrypt password hashing
- HTTPS only
- CSRF protection
- Rate limiting
- Secure session storage

### User Experience:
- "Remember me" functionality
- OAuth integration (Google, GitHub)
- Multi-factor authentication (MFA)
```

**Step 2: Architecture Design (15 min)**
```markdown
## Architecture

### Components:
1. Auth Service - Handles authentication logic
2. User Service - User CRUD operations
3. Token Service - JWT generation/validation
4. Session Store - Redis for session management

### Data Flow:
1. User submits credentials
2. Auth Service validates against User Service
3. Token Service generates JWT
4. JWT returned to client
5. Client includes JWT in subsequent requests
6. Middleware validates JWT on each request

### Database Schema:
```sql
-- users table
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(50) DEFAULT 'user',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- sessions table
CREATE TABLE sessions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  token_hash VARCHAR(255),
  expires_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- password_resets table
CREATE TABLE password_resets (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  token_hash VARCHAR(255),
  expires_at TIMESTAMP,
  used BOOLEAN DEFAULT FALSE
);
```
```

**Step 3: API Contracts (10 min)**
```typescript
// POST /auth/register
interface RegisterRequest {
  email: string;
  password: string;
  name: string;
}

interface RegisterResponse {
  user: {
    id: string;
    email: string;
    name: string;
  };
  token: string;
}

// POST /auth/login
interface LoginRequest {
  email: string;
  password: string;
  rememberMe?: boolean;
}

interface LoginResponse {
  user: UserProfile;
  token: string;
  refreshToken?: string;
}

// POST /auth/reset-password
interface ResetPasswordRequest {
  email: string;
}

// POST /auth/confirm-reset
interface ConfirmResetRequest {
  token: string;
  newPassword: string;
}
```

**Step 4: Security Checklist (10 min)**
```markdown
## Security Measures

- [ ] Password minimum 8 characters
- [ ] Bcrypt with cost factor 12
- [ ] Rate limiting: 5 attempts per 15 min
- [ ] HTTPS enforced
- [ ] CSRF tokens on state-changing requests
- [ ] JWT secret rotated monthly
- [ ] XSS protection headers
- [ ] SQL injection prevention (parameterized queries)
- [ ] Session timeout after 24 hours
- [ ] Password reset tokens expire after 1 hour
- [ ] Audit logging for all auth events
```

**Result:** Ready to implement with confidence, minimal surprises

## Hybrid Approach

### Example: E-Commerce Checkout Flow

**Complex Feature Requiring Both:**

**Phase 1: Prototype Payment Integration (20 min)**

Use Claude Code to test payment API:
```
Quick prototype to test Stripe payment integration.
Just need to verify:
1. Can we create payment intents?
2. How do we handle webhooks?
3. What's the error handling like?
```

**Prototype Code:**
```javascript
// stripe-test.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

async function testPayment() {
  try {
    // Test creating payment intent
    const paymentIntent = await stripe.paymentIntents.create({
      amount: 2000,
      currency: 'usd',
      payment_method_types: ['card'],
    });

    console.log('✓ Payment intent created:', paymentIntent.id);

    // Test webhook verification
    const event = stripe.webhooks.constructEvent(
      webhookPayload,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET
    );

    console.log('✓ Webhook verification works');

  } catch (error) {
    console.error('✗ Error:', error.message);
  }
}

testPayment();
```

**Learnings:**
- ✓ Stripe API is straightforward
- ✓ Webhook signatures work as expected
- ✗ Need to handle async payment confirmation
- ? How to handle failed payments and retries?

**Phase 2: Plan Full Checkout Flow (30 min)**

Now plan the complete system based on prototype learnings:

```markdown
## Checkout Flow Design

### States:
1. Cart → Review
2. Review → Payment Processing
3. Payment Processing → Confirmation or Failure
4. Failure → Retry or Cancel

### Database Schema:
```sql
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  status VARCHAR(50), -- pending, processing, completed, failed
  total_amount INTEGER,
  stripe_payment_intent_id VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

CREATE TABLE order_items (
  id UUID PRIMARY KEY,
  order_id UUID REFERENCES orders(id),
  product_id UUID REFERENCES products(id),
  quantity INTEGER,
  price_at_time INTEGER
);

CREATE TABLE payment_events (
  id UUID PRIMARY KEY,
  order_id UUID REFERENCES orders(id),
  event_type VARCHAR(50),
  stripe_event_id VARCHAR(255),
  data JSONB,
  created_at TIMESTAMP
);
```

### Error Handling:
1. Network failures → Retry with exponential backoff
2. Card declined → Show user-friendly message, allow retry
3. Webhook missed → Poll API as backup
4. Duplicate webhooks → Idempotency using stripe_event_id

### Test Strategy:
1. Unit tests for payment logic
2. Integration tests with Stripe test mode
3. Webhook testing with Stripe CLI
4. Load testing for concurrent payments
```

**Phase 3: Implementation (2 hours)**

With prototype validation + detailed plan, implement confidently.

## Using Claude Code Effectively

### For Rapid Prototyping

**Good Prompts:**
```
✓ "Quick prototype for testing WebSocket performance"
✓ "Simple example of Redis pub/sub in Node.js"
✓ "Minimal OAuth flow with Passport.js"
✓ "Test script to validate API rate limiting"
```

**Bad Prompts:**
```
✗ "Build complete authentication system"
✗ "Production-ready payment processing"
✗ "Full-featured admin dashboard"
```

### For Planning

**Good Prompts:**
```
✓ "Design database schema for multi-tenant SaaS"
✓ "Architecture for real-time collaborative editing"
✓ "API design for mobile app with offline support"
✓ "Security checklist for financial application"
```

**Workflow:**
```bash
# 1. Prototype to validate assumptions
claude "Quick prototype: Can we use WebRTC for video chat?"

# 2. Review prototype results
# (Test, measure, learn)

# 3. Plan based on learnings
claude "Design production architecture for video chat based on WebRTC, handling 1000 concurrent users"

# 4. Implement with confidence
```

## Decision Trees

### Feature Complexity Assessment

```
Is the feature complex?
├─ No → Prototype first (< 30 min), then implement
└─ Yes → Is the approach uncertain?
    ├─ No → Plan first (30-60 min), then implement
    └─ Yes → Hybrid approach:
        ├─ Prototype risky parts (30 min)
        ├─ Plan overall architecture (45 min)
        └─ Implement (2-4 hours)
```

### Risk Assessment

```
What's the cost of getting it wrong?
├─ Low (easy to revert) → Prototype quickly
├─ Medium (some refactoring needed) → Light planning + prototype
└─ High (data migration/breaking changes) → Detailed planning required
```

## Common Mistakes to Avoid

### 1. **Over-Engineering Prototypes**
❌ Writing tests for throwaway code
❌ Optimizing prototype performance
❌ Adding error handling to experiments

✅ Keep prototypes minimal
✅ Focus on validation only
✅ Expect to discard the code

### 2. **Planning Without Validation**
❌ Planning for 2 hours without testing assumptions
❌ Designing for requirements that might change
❌ Architecting for scale before proving concept

✅ Prototype first to validate unknowns
✅ Plan based on real data
✅ Start simple, scale later

### 3. **Not Documenting Learnings**
❌ Building prototype, forgetting what you learned
❌ Not sharing insights with team
❌ Repeating same experiments

✅ Document key findings
✅ Share with team
✅ Update plan based on learnings

### 4. **Perfectionism in Either Phase**
❌ Spending 4 hours on "perfect" plan
❌ Polishing prototype endlessly
❌ Analysis paralysis

✅ Time-box both activities
✅ "Good enough" planning
✅ Iterate quickly

## Verification Checklist

- [ ] Created decision framework (when to plan vs prototype)
- [ ] Built working prototype in under 20 minutes
- [ ] Created detailed plan for same/different feature
- [ ] Used Claude Code for rapid prototyping
- [ ] Identified scenarios where planning saves time
- [ ] Successfully used hybrid approach
- [ ] Documented learnings from both approaches
- [ ] Can explain trade-offs to team members

## Time Savings Examples

### Scenario 1: Payment Integration

**Prototype-First Approach:**
- Prototype: 30 min (discovered issues early)
- Planning: 30 min (informed by prototype)
- Implementation: 2 hours (no surprises)
- **Total: 3 hours**

**Plan-First Approach:**
- Planning: 1 hour (missed API quirks)
- Implementation: 3 hours (hit unexpected issues)
- Debugging: 1 hour (should have prototyped)
- **Total: 5 hours**

**Savings: 40%**

### Scenario 2: Database Migration

**Plan-First Approach:**
- Planning: 2 hours (caught edge cases)
- Implementation: 4 hours (smooth)
- Testing: 1 hour
- **Total: 7 hours**

**Prototype-First Approach:**
- Prototype: 1 hour
- Hit production data issue: 2 hours debugging
- Replan: 1 hour
- Reimplement: 3 hours
- **Total: 7 hours** (but higher risk)

**Conclusion: Planning was better for high-risk migration**

## Further Reading

- Lean Startup methodology (Build-Measure-Learn)
- Agile spike stories
- Proof of Concept (POC) best practices
- Architecture Decision Records (ADRs)
- Rapid prototyping techniques
