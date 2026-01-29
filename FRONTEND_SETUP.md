# Frontend Environment Configuration

This file contains the necessary environment configuration for the frontend to connect to the backend API.

## Required Environment Variables

- `NEXT_PUBLIC_API_BASE_URL`: Points to the backend API server (set to http://localhost:8000)
- `BETTER_AUTH_SECRET`: Secret key for authentication
- `BETTER_AUTH_URL`: URL for authentication service

## Troubleshooting Common Issues

1. **"An error occurred while making the request"**:
   - Make sure the backend server is running on port 8000
   - Verify the NEXT_PUBLIC_API_BASE_URL is correctly set
   - Check that the backend API routes match what the frontend expects

2. **To start the backend server**:
   ```bash
   cd backend
   python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

3. **To start the frontend server**:
   ```bash
   cd frontend
   npm run dev
   ```

4. **If you get port conflicts**, try a different port:
   - Backend: Change port in uvicorn command
   - Frontend: Update NEXT_PUBLIC_API_BASE_URL to match new backend port