'use client';

import React, { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import apiClient from '../services/api-client-wrapper';

interface AuthContextType {
  isAuthenticated: boolean;
  user: { id: string; email: string } | null;
  login: (email: string, password: string) => Promise<any>;
  register: (email: string, password: string) => Promise<any>;
  logout: () => void;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [user, setUser] = useState<{ id: string; email: string } | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // Check if user is authenticated on initial load
    const token = localStorage.getItem('access_token');
    if (token) {
      // In a real app, you would verify the token with the backend
      // For now, we'll just check if it exists
      setIsAuthenticated(true);

      // Try to get user info if needed
      // For this demo, we'll extract email from token or set a placeholder
      try {
        const tokenPayload = JSON.parse(atob(token.split('.')[1]));
        setUser({
          id: tokenPayload.sub || '',
          email: tokenPayload.email || tokenPayload.sub || 'user@example.com'
        });
      } catch (error) {
        console.error('Error parsing token:', error);
        // If token is invalid, remove it
        localStorage.removeItem('access_token');
        setIsAuthenticated(false);
      }
    }
    setLoading(false);
  }, []);

  const login = async (email: string, password: string) => {
    try {
      setLoading(true);
      const response = await apiClient.login(email, password);

      if (response.success) {
        // Extract data from the response (the backend wraps it in 'data')
        const tokenData = response.data || response;
        const access_token = tokenData.access_token || response.access_token;

        localStorage.setItem('access_token', access_token);
        setIsAuthenticated(true);

        // Set user with ID and email from response if available
        const userData = tokenData.user || response.user;
        if (userData) {
          setUser(userData);
        } else {
          // Fallback: extract from token if response doesn't include user data
          const token = access_token;
          try {
            const tokenPayload = JSON.parse(atob(token.split('.')[1]));
            setUser({
              id: tokenPayload.sub || '',
              email: tokenPayload.email || email
            });
          } catch (parseError) {
            setUser({ id: '', email });
          }
        }
      }

      return response;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  const register = async (email: string, password: string) => {
    try {
      setLoading(true);
      const response = await apiClient.register(email, password);
      return response;
    } catch (error) {
      console.error('Registration error:', error);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    setIsAuthenticated(false);
    setUser(null);
  };

  const value = {
    isAuthenticated,
    user,
    login,
    register,
    logout,
    loading
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};