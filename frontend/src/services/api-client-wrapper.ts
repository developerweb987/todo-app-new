import { MockApiClient } from './mock-api-client';

class ApiClientWrapper {
  // Authentication endpoints
  async login(email: string, password: string) {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().login(email, password);
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.login(email, password);
    }
  }

  async register(email: string, password: string) {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().register(email, password);
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.register(email, password);
    }
  }

  async logout() {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().logout();
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.logout();
    }
  }

  // Todo endpoints
  async getTodos() {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().getTodos();
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.getTodos();
    }
  }

  async createTodo(title: string, description?: string) {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().createTodo(title, description);
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.createTodo(title, description);
    }
  }

  async updateTodo(id: string, updates: { title?: string; description?: string }) {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().updateTodo(id, updates);
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.updateTodo(id, updates);
    }
  }

  async toggleTodoComplete(id: string, isCompleted: boolean) {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().toggleTodoComplete(id, isCompleted);
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.toggleTodoComplete(id, isCompleted);
    }
  }

  async deleteTodo(id: string) {
    const useMock = process.env.NEXT_PUBLIC_USE_MOCK_API === 'true' ||
                   !process.env.NEXT_PUBLIC_API_BASE_URL;

    if (useMock) {
      return new MockApiClient().deleteTodo(id);
    } else {
      const realClient = (await import('./api-client')).default;
      return realClient.deleteTodo(id);
    }
  }
}

export default new ApiClientWrapper();