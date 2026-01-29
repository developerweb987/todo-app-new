import axios, { AxiosInstance } from 'axios';

class ApiClient {
  private client: AxiosInstance;
  private baseURL: string;

  constructor(baseURL: string = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000') {
    this.baseURL = baseURL;
    this.client = axios.create({
      baseURL: this.baseURL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Add request interceptor to include JWT token
    this.client.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Add response interceptor to handle 401/403 responses
    this.client.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response?.status === 401 || error.response?.status === 403) {
          // Clear token and redirect to login
          localStorage.removeItem('access_token');
          window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }

  // Authentication endpoints
  async login(email: string, password: string) {
    try {
      const response = await this.client.post('/api/auth/login', { email, password });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async register(email: string, password: string) {
    try {
      const response = await this.client.post('/api/auth/register', { email, password });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async logout() {
    try {
      // Clear the stored token
      localStorage.removeItem('access_token');
      return { success: true };
    } catch (error) {
      throw this.handleError(error);
    }
  }

  // Todo endpoints
  async getTodos() {
    try {
      // Get user ID from token
      const token = localStorage.getItem('access_token');
      let userId = '';

      if (token) {
        try {
          const tokenPayload = JSON.parse(atob(token.split('.')[1]));
          userId = tokenPayload.sub || '';
        } catch (error) {
          console.error('Error parsing token:', error);
          throw this.handleError({ response: { status: 401, data: { detail: 'Invalid token' } } });
        }
      } else {
        throw this.handleError({ response: { status: 401, data: { detail: 'No token found' } } });
      }

      const response = await this.client.get(`/api/${userId}/tasks`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async createTodo(title: string, description?: string) {
    try {
      // Get user ID from token
      const token = localStorage.getItem('access_token');
      let userId = '';

      if (token) {
        try {
          const tokenPayload = JSON.parse(atob(token.split('.')[1]));
          userId = tokenPayload.sub || '';
        } catch (error) {
          console.error('Error parsing token:', error);
          throw this.handleError({ response: { status: 401, data: { detail: 'Invalid token' } } });
        }
      } else {
        throw this.handleError({ response: { status: 401, data: { detail: 'No token found' } } });
      }

      const response = await this.client.post(`/api/${userId}/tasks`, { title, description });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async updateTodo(id: string, updates: { title?: string; description?: string }) {
    try {
      // Get user ID from token
      const token = localStorage.getItem('access_token');
      let userId = '';

      if (token) {
        try {
          const tokenPayload = JSON.parse(atob(token.split('.')[1]));
          userId = tokenPayload.sub || '';
        } catch (error) {
          console.error('Error parsing token:', error);
          throw this.handleError({ response: { status: 401, data: { detail: 'Invalid token' } } });
        }
      } else {
        throw this.handleError({ response: { status: 401, data: { detail: 'No token found' } } });
      }

      const response = await this.client.put(`/api/${userId}/tasks/${id}`, updates);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async toggleTodoComplete(id: string, isCompleted: boolean) {
    try {
      // Get user ID from token
      const token = localStorage.getItem('access_token');
      let userId = '';

      if (token) {
        try {
          const tokenPayload = JSON.parse(atob(token.split('.')[1]));
          userId = tokenPayload.sub || '';
        } catch (error) {
          console.error('Error parsing token:', error);
          throw this.handleError({ response: { status: 401, data: { detail: 'Invalid token' } } });
        }
      } else {
        throw this.handleError({ response: { status: 401, data: { detail: 'No token found' } } });
      }

      const response = await this.client.patch(`/api/${userId}/tasks/${id}/complete`, { is_completed: isCompleted });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async deleteTodo(id: string) {
    try {
      // Get user ID from token
      const token = localStorage.getItem('access_token');
      let userId = '';

      if (token) {
        try {
          const tokenPayload = JSON.parse(atob(token.split('.')[1]));
          userId = tokenPayload.sub || '';
        } catch (error) {
          console.error('Error parsing token:', error);
          throw this.handleError({ response: { status: 401, data: { detail: 'Invalid token' } } });
        }
      } else {
        throw this.handleError({ response: { status: 401, data: { detail: 'No token found' } } });
      }

      const response = await this.client.delete(`/api/${userId}/tasks/${id}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  private handleError(error: any) {
    if (error.response) {
      // Server responded with error status
      const responseData = error.response.data;
      let errorMessage = error.response.statusText;

      // Try to extract meaningful error message from response
      if (responseData && typeof responseData === 'object') {
        // Check for structured error response from backend (success: false, error: {...})
        if (responseData.success === false && responseData.error) {
          errorMessage = responseData.error.message || responseData.error.details || error.response.statusText;
        }
        // Check for standard FastAPI error format
        else if (responseData.detail) {
          errorMessage = responseData.detail;
        }
        // Check for simple message
        else if (responseData.message) {
          errorMessage = responseData.message;
        }
        else if (Array.isArray(responseData)) {
          errorMessage = responseData.join(', ');
        }
        else {
          // If response has other keys, try to extract meaningful info
          const keys = Object.keys(responseData);
          if (keys.length > 0) {
            errorMessage = responseData[keys[0]] || JSON.stringify(responseData);
          }
        }
      }

      return {
        success: false,
        error: {
          code: error.response.status,
          message: errorMessage,
          details: responseData
        }
      };
    } else if (error.request) {
      // Request was made but no response received
      return {
        success: false,
        error: {
          code: 'NETWORK_ERROR',
          message: error.message || 'Network error occurred',
          details: 'Unable to connect to the server. Please check your connection and ensure the backend is running.'
        }
      };
    } else {
      // Something else happened
      return {
        success: false,
        error: {
          code: 'REQUEST_ERROR',
          message: error.message || 'An error occurred while making the request',
          details: error
        }
      };
    }
  }
}

export default new ApiClient();