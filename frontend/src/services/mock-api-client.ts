import { AxiosInstance } from 'axios';

// Mock data for todos
let mockTodos = [
  {
    id: '1',
    title: 'Sample Todo',
    description: 'This is a sample todo item',
    is_completed: false,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString()
  },
  {
    id: '2',
    title: 'Learn Next.js',
    description: 'Complete the Next.js tutorial',
    is_completed: true,
    created_at: new Date(Date.now() - 86400000).toISOString(), // Yesterday
    updated_at: new Date(Date.now() - 86400000).toISOString()
  }
];

// Mock user data
const mockUser = {
  email: 'demo@example.com'
};

class MockApiClient {
  private baseURL: string;

  constructor(baseURL: string = 'http://localhost:8000') {
    this.baseURL = baseURL;
  }

  // Authentication endpoints
  async login(email: string, password: string) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));

    if (email && password) {
      // Store a mock token
      const mockToken = btoa(JSON.stringify({ sub: email, exp: Date.now() + 3600000 }));
      localStorage.setItem('access_token', mockToken);

      return {
        success: true,
        access_token: mockToken,
        user: mockUser
      };
    } else {
      // Consistent error format matching real API
      throw {
        success: false,
        error: {
          code: 'AUTH_ERROR',
          message: 'Invalid credentials',
          details: 'Please check your email and password'
        }
      };
    }
  }

  async register(email: string, password: string) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 500));

    if (email && password.length >= 6) {
      // Store a mock token
      const mockToken = btoa(JSON.stringify({ sub: email, exp: Date.now() + 3600000 }));
      localStorage.setItem('access_token', mockToken);

      return {
        success: true,
        access_token: mockToken,
        user: mockUser
      };
    } else {
      // Consistent error format matching real API
      throw {
        success: false,
        error: {
          code: 'REGISTRATION_ERROR',
          message: 'Invalid registration data',
          details: 'Email is required and password must be at least 6 characters'
        }
      };
    }
  }

  async logout() {
    // Clear the stored token
    localStorage.removeItem('access_token');
    return { success: true };
  }

  // Todo endpoints
  async getTodos() {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 200));

    // Return a copy of the todos to prevent direct mutation
    return {
      success: true,
      data: [...mockTodos]
    };
  }

  async createTodo(title: string, description?: string) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));

    if (!title.trim()) {
      // Consistent error format matching real API
      throw {
        success: false,
        error: {
          code: 'VALIDATION_ERROR',
          message: 'Title is required',
          details: 'The title field cannot be empty'
        }
      };
    }

    const newTodo = {
      id: (mockTodos.length + 1).toString(),
      title: title.trim(),
      description: description?.trim() || '',
      is_completed: false,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    };

    mockTodos = [...mockTodos, newTodo];

    return {
      success: true,
      data: newTodo
    };
  }

  async updateTodo(id: string, updates: { title?: string; description?: string }) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));

    const index = mockTodos.findIndex(todo => todo.id === id);
    if (index !== -1) {
      mockTodos[index] = {
        ...mockTodos[index],
        ...updates,
        updated_at: new Date().toISOString()
      };

      return {
        success: true,
        data: mockTodos[index]
      };
    } else {
      // Consistent error format matching real API
      throw {
        success: false,
        error: {
          code: 'NOT_FOUND',
          message: 'Todo not found',
          details: 'The requested todo item could not be found'
        }
      };
    }
  }

  async toggleTodoComplete(id: string, isCompleted: boolean) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 200));

    const index = mockTodos.findIndex(todo => todo.id === id);
    if (index !== -1) {
      mockTodos[index] = {
        ...mockTodos[index],
        is_completed: isCompleted,
        updated_at: new Date().toISOString()
      };

      return {
        success: true,
        data: mockTodos[index]
      };
    } else {
      // Consistent error format matching real API
      throw {
        success: false,
        error: {
          code: 'NOT_FOUND',
          message: 'Todo not found',
          details: 'The requested todo item could not be found'
        }
      };
    }
  }

  async deleteTodo(id: string) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 300));

    const initialLength = mockTodos.length;
    mockTodos = mockTodos.filter(todo => todo.id !== id);

    if (mockTodos.length === initialLength) {
      // Consistent error format matching real API
      throw {
        success: false,
        error: {
          code: 'NOT_FOUND',
          message: 'Todo not found',
          details: 'The requested todo item could not be found'
        }
      };
    }

    return {
      success: true,
      message: 'Todo deleted successfully'
    };
  }
}

// Check if we should use mock API (when backend is not available)
const shouldUseMock = (): boolean => {
  // Check if NEXT_PUBLIC_USE_MOCK_API is set to true, or if we detect network issues
  return process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
         !process.env.NEXT_PUBLIC_API_BASE_URL;
};

// Factory function to get the appropriate API client
const getApiClient = () => {
  if (shouldUseMock()) {
    return new MockApiClient();
  } else {
    // Dynamically import the real API client
    return new (require('./api-client').default.constructor)();
  }
};

// Export the MockApiClient class for use in the wrapper
export { MockApiClient };