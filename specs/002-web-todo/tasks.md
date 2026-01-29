---
description: "Task list for Full-Stack Web Todo Application implementation"
---

# Tasks: Full-Stack Web Todo Application

**Input**: Design documents from `/specs/002-web-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- **Shared**: `shared/types/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend project structure with FastAPI dependencies in backend/
- [ ] T002 Create frontend project structure with Next.js dependencies in frontend/
- [ ] T003 [P] Initialize backend requirements.txt with FastAPI, SQLModel, psycopg2 dependencies
- [ ] T004 [P] Initialize frontend package.json with Next.js, TypeScript, Tailwind CSS dependencies
- [ ] T005 [P] Configure project root with shared directory for types

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Set up Neon PostgreSQL connection in backend/src/database/database.py
- [ ] T007 [P] Create User and TodoTask models in backend/src/models/
- [ ] T008 [P] Implement JWT authentication middleware in backend/src/middleware/auth_middleware.py that verifies tokens are issued by Better Auth
- [ ] T009 Configure environment variables and settings in backend/src/config/
- [ ] T010 [P] Set up Better Auth in frontend/src/lib/auth.ts
- [ ] T011 Create API client service in frontend/src/services/api-client.ts
- [ ] T012 Set up basic Next.js routing and layout in frontend/src/app/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create Account and Login (Priority: P1) 🎯 MVP

**Goal**: Enable new users to create an account and securely log in to the todo application

**Independent Test**: A new user can register for an account, receive confirmation, and log in successfully. The system validates credentials and establishes a secure session.

### Implementation for User Story 1

- [ ] T013 [P] [US1] Create authentication endpoints in backend/src/api/auth_router.py
- [ ] T014 [P] [US1] Implement user registration service in backend/src/services/auth_service.py
- [ ] T015 [US1] Implement JWT token generation and verification in backend/src/services/auth_service.py with proper issuer validation for Better Auth
- [ ] T016 [P] [US1] Create login page component in frontend/src/app/login/page.tsx
- [ ] T017 [P] [US1] Create register page component in frontend/src/app/register/page.tsx
- [ ] T018 [US1] Implement authentication state management in frontend/src/lib/auth-service.ts
- [ ] T019 [US1] Add authentication form validation in frontend/src/components/auth/

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Manage Personal Todo Tasks (Priority: P1)

**Goal**: Allow authenticated users to add, view, update, and delete their personal todo tasks

**Independent Test**: A logged-in user can create a new task, see it in their list, update its details, mark it as complete, and delete it when no longer needed.

### Implementation for User Story 2

- [ ] T020 [P] [US2] Create Todo API endpoints in backend/src/api/todo_router.py
- [ ] T021 [US2] Implement Todo service with CRUD operations in backend/src/services/todo_service.py
- [ ] T022 [P] [US2] Create Todo management components in frontend/src/components/todo/
- [ ] T023 [P] [US2] Create TaskList component in frontend/src/components/todo/task-list.tsx
- [ ] T024 [P] [US2] Create TaskItem component in frontend/src/components/todo/task-item.tsx
- [ ] T025 [P] [US2] Create TaskForm component in frontend/src/components/todo/task-form.tsx
- [ ] T026 [US2] Create dashboard page to display tasks in frontend/src/app/dashboard/page.tsx
- [ ] T027 [US2] Implement task completion toggle in frontend/src/components/todo/completion-toggle.tsx

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Secure Data Isolation (Priority: P1)

**Goal**: Ensure that users can only access and modify their own tasks, maintaining data privacy and security

**Independent Test**: When logged in as one user, I can only see and modify my own tasks, not those belonging to other users.

### Implementation for User Story 3

- [ ] T028 [US3] Enhance JWT middleware to verify user ownership of resources in backend/src/middleware/auth_middleware.py
- [ ] T029 [US3] Update Todo service to enforce user-based authorization in backend/src/services/todo_service.py
- [ ] T030 [US3] Add user ID validation to all Todo API endpoints in backend/src/api/todo_router.py
- [ ] T031 [US3] Implement user-based filtering in GET /api/todos endpoint in backend/src/api/todo_router.py
- [ ] T032 [US3] Add error handling for unauthorized access attempts in backend/src/api/todo_router.py
- [ ] T033 [US3] Implement client-side validation to ensure proper error handling in frontend/src/services/api-client.ts

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Integration & Validation

**Goal**: Connect frontend and backend components and validate end-to-end functionality

- [ ] T034 [P] Connect frontend API client with backend endpoints in frontend/src/services/api-client.ts
- [ ] T035 [P] Implement JWT token attachment to all authenticated requests in frontend/src/services/api-client.ts
- [ ] T036 Handle 401/403 responses in frontend application in frontend/src/services/api-client.ts
- [ ] T037 Test end-to-end authentication flow from registration to dashboard access
- [ ] T038 Validate user data isolation by testing cross-user access attempts
- [ ] T039 [P] Add loading states for API calls in frontend/src/components/ui/loading-states.tsx
- [ ] T040 Add error states for auth/API failures in frontend/src/components/ui/error-states.tsx
- [ ] T041 Implement empty states when no tasks exist in frontend/src/components/todo/empty-state.tsx

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T042 [P] Add comprehensive error handling and logging across all backend endpoints
- [ ] T043 [P] Add input validation and sanitization to all API endpoints
- [ ] T044 [P] Implement proper database transaction handling
- [ ] T045a [P] Handle expired JWT tokens during API requests in backend/src/middleware/auth_middleware.py
- [ ] T045b [P] Handle user attempts to access application without authentication in frontend/src/services/auth-service.ts
- [ ] T045c [P] Handle user attempts to delete non-existent tasks in backend/src/api/todo_router.py
- [ ] T045d [P] Handle database connectivity loss gracefully in backend/src/database/database.py
- [ ] T045e [P] Handle user attempts to create tasks with empty descriptions in backend/src/services/todo_service.py
- [ ] T046 [P] Add comprehensive TypeScript types in shared/types/index.ts
- [ ] T047 [P] Add responsive design to all frontend components using Tailwind CSS
- [ ] T048 [P] Add accessibility features to all frontend components
- [ ] T049 [P] Add proper meta tags and SEO features to Next.js app
- [ ] T050 Run quickstart.md validation to ensure all setup instructions work
- [ ] T051 [P] Add comprehensive documentation in README.md files

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Integration & Validation (Phase 6)**: Depends on all user stories being complete
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on User Story 1 for authentication
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Depends on User Story 2 for task operations

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 2

```bash
# Launch all components for User Story 2 together:
Task: "Create Todo API endpoints in backend/src/api/todo_router.py"
Task: "Create Todo management components in frontend/src/components/todo/"
Task: "Create TaskList component in frontend/src/components/todo/task-list.tsx"
Task: "Create TaskItem component in frontend/src/components/todo/task-item.tsx"
Task: "Create TaskForm component in frontend/src/components/todo/task-form.tsx"
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Authentication)
4. Complete Phase 4: User Story 2 (Basic Task Management)
5. **STOP and VALIDATE**: Test authentication and basic task management independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add Integration & Validation → Test end-to-end → Deploy/Demo
6. Add Polish → Final touches → Production Ready

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Authentication)
   - Developer B: User Story 2 (Task Management)
   - Developer C: User Story 3 (Security/Authorization)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- User Story 3 depends on authentication from User Story 1 and task operations from User Story 2