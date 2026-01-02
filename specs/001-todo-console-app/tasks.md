---
description: "Task list for Todo In-Memory Python Console App implementation"
---

# Tasks: Todo In-Memory Python Console App

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as specified in the functional requirements and success criteria.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/todo_app/
- [x] T002 Initialize Python 3.13+ project with dependencies in requirements.txt
- [x] T003 [P] Configure pytest testing framework in pyproject.toml
- [x] T004 Create initial project files (README.md, CLAUDE.md, .gitignore)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Task model in src/todo_app/models/task.py
- [x] T006 Create TodoList collection in src/todo_app/services/todo_service.py
- [x] T007 [P] Create CLI argument parser in src/todo_app/cli/cli_app.py
- [x] T008 Create main application entry point in src/todo_app/main.py
- [x] T009 Configure error handling and logging infrastructure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with title and description

**Independent Test**: Can be fully tested by running the console app, entering an "add task" command, providing title and description, and verifying the task appears in the list.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Unit test for Task creation in tests/unit/test_task.py
- [x] T011 [P] [US1] Unit test for add_task functionality in tests/unit/test_todo_service.py
- [x] T012 [P] [US1] Integration test for adding tasks via CLI in tests/integration/test_cli_integration.py

### Implementation for User Story 1

- [x] T013 [P] [US1] Implement Task model with validation in src/todo_app/models/task.py
- [x] T014 [US1] Implement add_task method in src/todo_app/services/todo_service.py
- [x] T015 [US1] Implement add command in CLI interface in src/todo_app/cli/cli_app.py
- [x] T016 [US1] Add input validation for title and description
- [x] T017 [US1] Add unique ID generation for tasks

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Enable users to view their complete todo list with status indicators

**Independent Test**: Can be fully tested by running the console app, viewing the list of tasks, and verifying that all tasks display with proper status indicators (completed/incomplete).

### Tests for User Story 2 ⚠️

- [x] T018 [P] [US2] Unit test for get_all_tasks functionality in tests/unit/test_todo_service.py
- [x] T019 [P] [US2] Integration test for viewing tasks via CLI in tests/integration/test_cli_integration.py

### Implementation for User Story 2

- [x] T020 [US2] Implement get_all_tasks method in src/todo_app/services/todo_service.py
- [x] T021 [US2] Implement get_completed_tasks method in src/todo_app/services/todo_service.py
- [x] T022 [US2] Implement get_pending_tasks method in src/todo_app/services/todo_service.py
- [x] T023 [US2] Implement list command in CLI interface in src/todo_app/cli/cli_app.py
- [x] T024 [US2] Format task display with status indicators

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark tasks as complete or incomplete to track progress

**Independent Test**: Can be fully tested by selecting a task ID and marking it complete/incomplete, then verifying the status change in the task list.

### Tests for User Story 3 ⚠️

- [x] T025 [P] [US3] Unit test for mark_complete/mark_incomplete in tests/unit/test_todo_service.py
- [x] T026 [P] [US3] Integration test for marking tasks via CLI in tests/integration/test_cli_integration.py

### Implementation for User Story 3

- [x] T027 [US3] Implement mark_complete method in src/todo_app/services/todo_service.py
- [x] T028 [US3] Implement mark_incomplete method in src/todo_app/services/todo_service.py
- [x] T029 [US3] Implement complete command in CLI interface in src/todo_app/cli/cli_app.py
- [x] T030 [US3] Implement incomplete command in CLI interface in src/todo_app/cli/cli_app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Enable users to update task details like title and description

**Independent Test**: Can be fully tested by selecting a task ID, updating its details, and verifying the changes persist in the task list.

### Tests for User Story 4 ⚠️

- [x] T031 [P] [US4] Unit test for update_task functionality in tests/unit/test_todo_service.py
- [x] T032 [P] [US4] Integration test for updating tasks via CLI in tests/integration/test_cli_integration.py

### Implementation for User Story 4

- [x] T033 [US4] Implement update_task method in src/todo_app/services/todo_service.py
- [x] T034 [US4] Implement update command in CLI interface in src/todo_app/cli/cli_app.py
- [x] T035 [US4] Add validation for updated title and description

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Enable users to delete tasks they no longer need

**Independent Test**: Can be fully tested by selecting a task ID for deletion and verifying it's removed from the task list.

### Tests for User Story 5 ⚠️

- [x] T036 [P] [US5] Unit test for delete_task functionality in tests/unit/test_todo_service.py
- [x] T037 [P] [US5] Integration test for deleting tasks via CLI in tests/integration/test_cli_integration.py

### Implementation for User Story 5

- [x] T038 [US5] Implement delete_task method in src/todo_app/services/todo_service.py
- [x] T039 [US5] Implement delete command in CLI interface in src/todo_app/cli/cli_app.py
- [x] T040 [US5] Add error handling for non-existent task IDs

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T041 [P] Add comprehensive error handling for all operations
- [x] T042 [P] Add input validation across all commands
- [x] T043 Add documentation in README.md for all commands
- [x] T044 Run quickstart validation with all features
- [x] T045 Add help text and usage examples to CLI
- [x] T046 Handle edge cases like empty lists, invalid IDs, etc.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with other stories but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Task creation in tests/unit/test_task.py"
Task: "Unit test for add_task functionality in tests/unit/test_todo_service.py"
Task: "Integration test for adding tasks via CLI in tests/integration/test_cli_integration.py"

# Launch implementation tasks for User Story 1:
Task: "Implement Task model with validation in src/todo_app/models/task.py"
Task: "Implement add_task method in src/todo_app/services/todo_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence