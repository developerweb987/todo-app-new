export interface User {
  id: string;
  email: string;
  username?: string;
  created_at: Date;
  updated_at: Date;
  is_active: boolean;
}

export interface TodoTask {
  id: string;
  title: string;
  description?: string;
  is_completed: boolean;
  user_id: string;
  created_at: Date;
  updated_at: Date;
}

export interface TodoTaskUpdate {
  title?: string;
  description?: string;
  is_completed?: boolean;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
    details?: any;
  };
}