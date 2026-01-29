# Troubleshooting Guide

## Common Issues and Solutions

### 1. "An error occurred while making the request"
**Cause:** Frontend cannot connect to the backend API
**Solutions:**
- Ensure the backend server is running on port 8000
- Check that NEXT_PUBLIC_API_BASE_URL is set correctly in frontend/.env.local
- Verify the backend server process is active (check with `netstat -ano | findstr :8000`)
- Make sure firewall isn't blocking the connection

### 2. Port Binding Errors (Address already in use)
**Cause:** Another process is using the required port
**Solutions:**
- Find the process: `netstat -ano | findstr :8000`
- Kill the process: `taskkill /PID <PID> /F`
- Or use a different port for either frontend or backend

### 3. Database Connection Issues
**Cause:** Backend cannot connect to the database
**Solutions:**
- Check database connection string in backend configuration
- Ensure PostgreSQL/SQLite is running and accessible
- Verify database credentials

### 4. Environment Variable Issues
**Cause:** Missing or incorrect environment variables
**Solutions:**
- Ensure NEXT_PUBLIC_API_BASE_URL is set in frontend/.env.local
- Verify all required environment variables are present
- Restart the frontend after changing environment variables

### 5. Token/Authentication Issues
**Cause:** Invalid or expired JWT tokens
**Solutions:**
- Clear browser storage/localStorage
- Log out and log back in
- Check that the backend authentication endpoints are working

## Quick Checks

1. Is the backend running? Test: `curl http://localhost:8000/health`
2. Are environment variables set correctly?
3. Is the database accessible?
4. Are there any CORS issues?

## Restarting Services

To restart everything cleanly:
1. Kill any existing server processes
2. Run `start_both_servers.bat`
3. Check the console output for any errors