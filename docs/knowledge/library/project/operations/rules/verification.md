# Verification & Testing Rules

## RULE #4: Verification Until Maximum Confidence

Do NOT proceed to the next phase/step until:

1. ✅ All tests pass (run tests EVERY TIME)
2. ✅ Manual verification confirms expected behavior
3. ✅ You have ABSOLUTE confidence it works as intended
4. ✅ Edge cases have been considered and tested

**Why**: Agents CAN make mistakes. Verify everything.

## RULE #6: No False Completion Claims

Before saying "done", "complete", or "finished":

1. **Provide EVIDENCE** (file path, test output, screenshot)
2. **Explain HOW** you verified it works
3. **List** any known limitations or edge cases

**Why**: Direction ≠ Decision. Intention ≠ Completion.

## Testing Requirements

### Minimum Test Coverage: 80%

Test Types (ALL required):

1. **Unit Tests** - Individual functions, utilities, components
2. **Integration Tests** - API endpoints, database operations
3. **E2E Tests** - Critical user flows (Playwright)

### Test-Driven Development Workflow

**MANDATORY** for all new features:

1. **RED**: Write test first - it should FAIL
2. **GREEN**: Write minimal implementation - test should PASS
3. **REFACTOR**: Improve code quality, tests still pass
4. **VERIFY**: Run full test suite, check coverage

### Running Tests

```bash
# Unit + Integration tests
npm test

# Watch mode during development
npm test -- --watch

# E2E tests
npm run test:e2e

# Coverage report
npm test -- --coverage
```

**Requirement**: Coverage must be ≥80% before marking work complete.

## Definition of Done

A task is ONLY complete when:

### 1. Code Quality

- [ ] All tests pass locally
- [ ] Test coverage ≥ 80%
- [ ] No console.log statements in production code
- [ ] No hardcoded credentials or secrets
- [ ] Code follows project style guide
- [ ] No linting errors (`npm run lint`)
- [ ] No TypeScript errors (`npm run type-check`)

### 2. Documentation

- [ ] README updated if user-facing changes
- [ ] API docs updated if endpoints changed
- [ ] Inline comments for complex logic
- [ ] Relevant files referenced in AGENTS.md

### 3. Evidence

- [ ] Screenshot of working feature (if UI)
- [ ] Test output showing all tests pass
- [ ] Manual testing steps documented
- [ ] Edge cases tested and results recorded

### 4. Git

- [ ] All changes committed with clear messages
- [ ] Branch pushed to remote
- [ ] Plan file updated with completion status
- [ ] Session log written (if significant work)

## Verification Protocol

### For Features

1. **Functional Testing**
   - Does the feature work as specified?
   - Test happy path + error cases
   - Test with realistic data

2. **Visual Testing** (UI features)
   - Screenshot before/after
   - Test in different screen sizes
   - Check accessibility (keyboard nav, color contrast)

3. **Performance Testing**
   - Page load time < 3s
   - API response time < 200ms (p95)
   - No memory leaks

### For Bug Fixes

1. **Reproduction**
   - Confirm you can reproduce the bug
   - Document exact steps to reproduce

2. **Fix Verification**
   - Bug no longer reproducible
   - No regression (old features still work)
   - Test edge cases around the fix

3. **Root Cause**
   - Document WHY the bug occurred
   - Add tests to prevent regression

### For Refactoring

1. **Behavior Preservation**
   - All existing tests still pass
   - No change in functionality
   - Screenshots match (if UI)

2. **Code Quality**
   - Complexity reduced (measurable)
   - Duplication eliminated
   - Improved readability

## Evidence Storage

Store verification evidence in `.agents/artifacts/`:

```
.agents/artifacts/
├── screenshots/
│   └── 2026-01-30-feature-name/
│       ├── before.png
│       ├── after.png
│       └── edge-case.png
├── test-results/
│   └── 2026-01-30-feature-name.txt
└── reports/
    └── 2026-01-30-performance-analysis.md
```

## Common Verification Mistakes

### ❌ Don't Do This

- "I believe it works" (without testing)
- "Tests are optional for this task"
- "I'll add tests later"
- "Manual testing is sufficient"
- "Coverage dropped but feature works"

### ✅ Do This

- Run tests before claiming done
- Write tests alongside code (TDD)
- Provide evidence in commit message
- Screenshot + test output + coverage report
- Fix failing tests immediately

## Edge Cases Checklist

Always consider:

- [ ] Empty state (no data)
- [ ] Maximum state (pagination, limits)
- [ ] Invalid input (malformed data)
- [ ] Network failure (offline, timeout)
- [ ] Concurrent access (race conditions)
- [ ] Browser compatibility (Chrome, Firefox, Safari)
- [ ] Mobile responsiveness
- [ ] Accessibility (screen readers, keyboard)

## Security Verification

Before marking complete:

- [ ] No secrets in code/logs
- [ ] All inputs validated
- [ ] SQL injection prevented (parameterized queries)
- [ ] XSS prevented (sanitized HTML)
- [ ] Authentication verified
- [ ] Authorization checked (role-based)
- [ ] Rate limiting tested

## Final Checklist

```bash
# Run this before claiming task complete:
npm run lint          # No linting errors
npm run type-check    # No TypeScript errors
npm test              # All tests pass
npm test -- --coverage # Coverage ≥ 80%
npm run build         # Build succeeds

# If all pass: ✅ Task complete
# If any fail: ❌ Fix before proceeding
```
