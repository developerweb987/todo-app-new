export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/api/auth/login',
    REGISTER: '/api/auth/register',
    LOGOUT: '/api/auth/logout',
  },
  TODO: {
    BASE: '/api/todos',
    GET_ALL: '/api/todos',
    CREATE: '/api/todos',
    UPDATE: (id: string) => `/api/todos/${id}`,
    DELETE: (id: string) => `/api/todos/${id}`,
    TOGGLE_COMPLETE: (id: string) => `/api/todos/${id}/complete`,
  },
};

export const STORAGE_KEYS = {
  ACCESS_TOKEN: 'access_token',
  REFRESH_TOKEN: 'refresh_token',
  USER_DATA: 'user_data',
};

export const MESSAGES = {
  UNAUTHORIZED: 'Unauthorized access. Please log in.',
  FORBIDDEN: 'Access denied. You do not have permission to perform this action.',
  NETWORK_ERROR: 'Network error occurred. Please check your connection.',
  SERVER_ERROR: 'Server error occurred. Please try again later.',
  INVALID_CREDENTIALS: 'Invalid email or password.',
  SUCCESSFUL_LOGIN: 'Login successful.',
  SUCCESSFUL_REGISTER: 'Registration successful.',
  SUCCESSFUL_LOGOUT: 'Logout successful.',
};

export const VALIDATION = {
  EMAIL_PATTERN: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  PASSWORD_MIN_LENGTH: 6,
  TITLE_MIN_LENGTH: 1,
  TITLE_MAX_LENGTH: 255,
  DESCRIPTION_MAX_LENGTH: 1000,
};