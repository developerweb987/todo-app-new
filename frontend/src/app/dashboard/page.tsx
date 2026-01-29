'use client';

import React, { useState, useEffect } from 'react';
import TaskList from '../../components/todo/task-list';
import TaskForm from '../../components/todo/task-form';
import { TodoTask } from '../../../../shared/types';
import apiClient from '../../services/api-client-wrapper';
import Header from '../../components/ui/header';

const DashboardPage = () => {
  const [tasks, setTasks] = useState<TodoTask[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [updatingTaskId, setUpdatingTaskId] = useState<string | null>(null);
  const [deletingTaskId, setDeletingTaskId] = useState<string | null>(null);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const response = await apiClient.getTodos();
      // Handle both real API response format and mock API response format
      const data = response.data || response;
      setTasks(Array.isArray(data) ? data : []);
    } catch (err: any) {
      console.error('Error fetching tasks:', err);
      // Extract error message from both real and mock API responses
      let errorMessage = 'Failed to fetch tasks';
      if (err.error?.message) {
        errorMessage = err.error.message;
      } else if (err.message) {
        errorMessage = err.message;
      } else if (typeof err === 'string') {
        errorMessage = err;
      }
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const handleAddTask = async (title: string, description?: string) => {
    try {
      const response = await apiClient.createTodo(title, description);
      // Handle both real API response format and mock API response format
      const newTask = response.data || response;
      setTasks([...tasks, newTask]);
    } catch (err: any) {
      console.error('Error adding task:', err);
      // Extract error message from both real and mock API responses
      let errorMessage = 'Failed to add task';
      if (err.error?.message) {
        errorMessage = err.error.message;
      } else if (err.message) {
        errorMessage = err.message;
      } else if (typeof err === 'string') {
        errorMessage = err;
      }
      setError(errorMessage);
    }
  };

  const handleUpdateTask = async (id: string, updates: { title?: string; description?: string }) => {
    setUpdatingTaskId(id);
    try {
      const response = await apiClient.updateTodo(id, updates);
      // Handle both real API response format and mock API response format
      const updatedTask = response.data || response;
      setTasks(tasks.map(task => task.id === id ? updatedTask : task));
    } catch (err: any) {
      console.error('Error updating task:', err);
      // Extract error message from both real and mock API responses
      let errorMessage = 'Failed to update task';
      if (err.error?.message) {
        errorMessage = err.error.message;
      } else if (err.message) {
        errorMessage = err.message;
      } else if (typeof err === 'string') {
        errorMessage = err;
      }
      setError(errorMessage);
    } finally {
      setUpdatingTaskId(null);
    }
  };

  const handleToggleComplete = async (id: string, isCompleted: boolean) => {
    try {
      const response = await apiClient.toggleTodoComplete(id, isCompleted);
      // Handle both real API response format and mock API response format
      const updatedTask = response.data || response;
      setTasks(tasks.map(task => task.id === id ? updatedTask : task));
    } catch (err: any) {
      console.error('Error toggling task completion:', err);
      // Extract error message from both real and mock API responses
      let errorMessage = 'Failed to update task status';
      if (err.error?.message) {
        errorMessage = err.error.message;
      } else if (err.message) {
        errorMessage = err.message;
      } else if (typeof err === 'string') {
        errorMessage = err;
      }
      setError(errorMessage);
    }
  };

  const handleDeleteTask = async (id: string) => {
    setDeletingTaskId(id);
    try {
      const response = await apiClient.deleteTodo(id);
      // Handle both real API response format and mock API response format
      // For delete, we typically just remove from UI regardless of response content
      setTasks(tasks.filter(task => task.id !== id));
    } catch (err: any) {
      console.error('Error deleting task:', err);
      // Extract error message from both real and mock API responses
      let errorMessage = 'Failed to delete task';
      if (err.error?.message) {
        errorMessage = err.error.message;
      } else if (err.message) {
        errorMessage = err.message;
      } else if (typeof err === 'string') {
        errorMessage = err;
      }
      setError(errorMessage);
    } finally {
      setDeletingTaskId(null);
    }
  };

  const focusOnNewTask = () => {
    const titleInput = document.getElementById('task-title-input');
    if (titleInput) {
      titleInput.focus();
    }
  };

  // Calculate task statistics
  const totalTasks = tasks.length;
  const completedTasks = tasks.filter(task => task.is_completed).length;
  const pendingTasks = totalTasks - completedTasks;

  if (loading) {
    return (
      <>
        <Header title="Evolution of Todo" showLogoutButton={true} />
        <div className="container mx-auto px-4 py-8">
          <div className="flex justify-center items-center h-64">
            <div className="text-center">
              <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mb-4"></div>
              <p className="text-gray-600">Loading your tasks...</p>
            </div>
          </div>
        </div>
      </>
    );
  }

  return (
    <>
      <Header title="Evolution of Todo" showLogoutButton={true} />

      <div className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div className="bg-gradient-to-r from-blue-500 to-blue-600 rounded-2xl shadow-lg p-6 text-white transform transition-transform duration-300 hover:scale-105">
              <div className="flex items-center">
                <div className="p-3 rounded-xl bg-blue-400 bg-opacity-30 backdrop-blur-sm">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                  </svg>
                </div>
                <div className="ml-4">
                  <h3 className="text-3xl font-bold">{totalTasks}</h3>
                  <p className="text-blue-100">Total Tasks</p>
                </div>
              </div>
            </div>

            <div className="bg-gradient-to-r from-green-500 to-green-600 rounded-2xl shadow-lg p-6 text-white transform transition-transform duration-300 hover:scale-105">
              <div className="flex items-center">
                <div className="p-3 rounded-xl bg-green-400 bg-opacity-30 backdrop-blur-sm">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div className="ml-4">
                  <h3 className="text-3xl font-bold">{completedTasks}</h3>
                  <p className="text-green-100">Completed</p>
                </div>
              </div>
            </div>

            <div className="bg-gradient-to-r from-amber-500 to-amber-600 rounded-2xl shadow-lg p-6 text-white transform transition-transform duration-300 hover:scale-105">
              <div className="flex items-center">
                <div className="p-3 rounded-xl bg-amber-400 bg-opacity-30 backdrop-blur-sm">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div className="ml-4">
                  <h3 className="text-3xl font-bold">{pendingTasks}</h3>
                  <p className="text-amber-100">Pending</p>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-2xl shadow-xl p-6 border border-gray-100 mb-8 transform transition-all duration-300 hover:shadow-2xl">
            <h2 className="text-xl font-semibold text-gray-900 mb-4 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              Add New Task
            </h2>
            <TaskForm onSubmit={handleAddTask} />
          </div>

          {error && (
            <div className="mb-6 p-4 bg-red-50 border-l-4 border-red-500 text-red-700 rounded-r-xl shadow-md transform transition-transform duration-300 hover:scale-[1.01]">
              <div className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                </svg>
                {error}
              </div>
            </div>
          )}

          <div className="bg-white rounded-2xl shadow-xl p-6 border border-gray-100 transform transition-all duration-300 hover:shadow-2xl">
            <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center mb-6 gap-4">
              <div>
                <h2 className="text-xl font-semibold text-gray-900">Your Tasks</h2>
                <p className="text-sm text-gray-500 mt-1">{tasks.length} {tasks.length === 1 ? 'task' : 'tasks'}</p>
              </div>
              <div className="flex space-x-2">
                <button
                  onClick={focusOnNewTask}
                  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-lg text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 shadow-md hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                  </svg>
                  Add Task
                </button>
              </div>
            </div>

            <TaskList
              tasks={tasks}
              onToggleComplete={handleToggleComplete}
              onDelete={handleDeleteTask}
              onUpdate={handleUpdateTask}
              onAddNewTask={focusOnNewTask}
              updatingTaskId={updatingTaskId}
              deletingTaskId={deletingTaskId}
            />
          </div>
        </div>
      </div>
    </>
  );
};

export default DashboardPage;