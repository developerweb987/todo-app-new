---
id: 4
title: "tasks-full-stack-web-todo-application"
stage: "tasks"
date_iso: "2026-01-14"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "web-todo"
branch: "002-web-todo"
user: "Archive1"
command: "/sp.tasks"
labels: ["tasks", "todo", "authentication", "full-stack"]
links:
  spec: "specs/002-web-todo/spec.md"
  plan: "specs/002-web-todo/plan.md"
  tasks: "specs/002-web-todo/tasks.md"
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - specs/002-web-todo/tasks.md
  - history/prompts/web-todo/4-tasks-full-stack-web-todo-application.tasks.prompt.md
tests_yaml: |
  - specs/002-web-todo/tasks.md
prompt_text: |
  # sp.tasks — Phase II: Full-Stack Web Todo

  ## Backend Tasks

  1. **DB: Task Model**
     - Create SQLModel `Task` with fields: id, user_id, title, description, completed, created_at, updated_at
     - Link `user_id` to `users` table

  2. **DB Connection**
     - Connect to Neon PostgreSQL using environment variable `DATABASE_URL`
     - Configure session lifecycle

  3. **Auth Middleware**
     - Verify JWT from `Authorization` header
     - Extract `user_id` and attach to request context
     - Reject invalid/missing tokens with 401

  4. **REST API: GET /tasks**
     - Return tasks for authenticated user
     - Support optional query params: status, sort

  5. **REST API: POST /tasks**
     - Create a new task for authenticated user
     - Validate title (required), description (optional)

  6. **REST API: GET /tasks/{id}**
     - Return task details
     - Ensure task belongs to user

  7. **REST API: PUT /tasks/{id}**
     - Update title/description of task
     - Enforce ownership

  8. **REST API: DELETE /tasks/{id}**
     - Delete task
     - Enforce ownership

  9. **REST API: PATCH /tasks/{id}/complete**
     - Toggle task completion
     - Enforce ownership

  ---

  ## Frontend Tasks

  10. **Better Auth Setup**
      - Configure signup and login pages
      - Retrieve JWT token after login

  11. **API Client**
      - Create centralized client
      - Attach JWT to all requests
      - Handle 401 / 403 responses

  12. **UI Components**
      - TaskList: display all user tasks
      - TaskItem: show title, description, completed status
      - TaskForm: create/update tasks
      - CompletionToggle: mark task complete

  13. **Pages**
      - `/login` — login page
      - `/register` — signup page
      - `/dashboard` — display task list, create/update/delete actions

  14. **UX & States**
      - Loading states for API calls
      - Empty states when no tasks
      - Error states for auth/API failures

  ---

  ## Integration Tasks

  15. **Connect Frontend & Backend**
      - Map frontend actions to backend endpoints
      - Ensure JWT flows end-to-end

  16. **Validation**
      - Confirm user data isolation
      - Test all CRUD operations
      - Ensure unauthorized requests return 401
response_text: |
  Created comprehensive task list for the Full-Stack Web Todo application with 50 specific, actionable tasks organized by user story. The tasks are divided into 7 phases:
  - Phase 1: Setup (5 tasks)
  - Phase 2: Foundational (7 tasks)
  - Phase 3: User Story 1 - Authentication (7 tasks)
  - Phase 4: User Story 2 - Task Management (8 tasks)
  - Phase 5: User Story 3 - Data Isolation (6 tasks)
  - Phase 6: Integration & Validation (11 tasks)
  - Phase 7: Polish & Cross-Cutting (11 tasks)

  Each task follows the required format with checkboxes, IDs, and file paths. Tasks are organized by user story to enable independent implementation and testing. Parallel execution opportunities are marked with [P] tags.
outcome: |
  Successfully generated complete task breakdown for the Full-Stack Web Todo application. All 50 tasks follow the required format and are organized by user story for independent implementation. The tasks cover all required functionality including authentication, task management, data isolation, and integration.
evaluation: |
  The task list comprehensively covers all aspects of the implementation: backend models, authentication middleware, API endpoints, frontend components, and integration. All tasks follow the required format with proper IDs, story labels, and file paths. The organization by user story enables independent development and testing.
---
# PHR: tasks-full-stack-web-todo-application

## Overview
- **ID**: 4
- **Stage**: tasks
- **Date**: 2026-01-14
- **Feature**: web-todo
- **Branch**: 002-web-todo

## Description
Created comprehensive task list for the Full-Stack Web Todo application with 50 specific, actionable tasks organized by user story.

## Files Created
- specs/002-web-todo/tasks.md

## Summary
The tasks are divided into 7 phases covering setup, foundational work, user stories, integration, and polish. Each task follows the required format with checkboxes, IDs, and file paths. Tasks are organized by user story to enable independent implementation and testing.

## Status
Successfully generated complete task breakdown for the Full-Stack Web Todo application. All tasks follow the required format and are organized by user story for independent implementation.