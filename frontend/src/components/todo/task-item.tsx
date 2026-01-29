import React, { useState } from 'react';
import { TodoTask } from '../../../../shared/types';
import { PencilIcon, TrashIcon, CheckCircleIcon as CheckCircleOutlineIcon } from '@heroicons/react/24/outline';
import { CheckCircleIcon as CheckCircleSolidIcon } from '@heroicons/react/24/solid';

interface TaskItemProps {
  task: TodoTask;
  onToggleComplete: (id: string, isCompleted: boolean) => void;
  onDelete: (id: string) => void;
  onUpdate: (id: string, updates: { title?: string; description?: string }) => void;
  isUpdating?: boolean;
  isDeleting?: boolean;
}

const TaskItem: React.FC<TaskItemProps> = ({ task, onToggleComplete, onDelete, onUpdate, isUpdating = false, isDeleting = false }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description || '');

  const handleSave = () => {
    onUpdate(task.id, { title, description: description.trim() || undefined });
    setIsEditing(false);
  };

  const handleCancel = () => {
    setTitle(task.title);
    setDescription(task.description || '');
    setIsEditing(false);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Escape') {
      handleCancel();
    } else if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSave();
    }
  };

  return (
    <div className={`border rounded-xl p-5 shadow-sm transition-all duration-300 hover:shadow-md transform hover:-translate-y-0.5 ${
      task.is_completed
        ? 'bg-gradient-to-r from-green-50 to-emerald-50 border-green-200 opacity-90'
        : 'bg-white border-gray-200 hover:border-blue-300'
    }`}>
      {isEditing ? (
        <div className="space-y-4">
          <div>
            <label htmlFor={`task-title-${task.id}`} className="block text-sm font-medium text-gray-700 mb-1">
              Task Title
            </label>
            <input
              id={`task-title-${task.id}`}
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              onKeyDown={handleKeyPress}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200"
              autoFocus
            />
          </div>
          <div>
            <label htmlFor={`task-description-${task.id}`} className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <textarea
              id={`task-description-${task.id}`}
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              onKeyDown={handleKeyPress}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200 resize-none"
              rows={2}
            />
          </div>
          <div className="flex space-x-3">
            <button
              onClick={handleSave}
              disabled={isUpdating}
              className={`px-4 py-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-200 shadow-md hover:shadow-lg transform hover:-translate-y-0.5 ${
                isUpdating
                  ? 'opacity-70 cursor-not-allowed'
                  : 'hover:from-blue-700 hover:to-indigo-700'
              }`}
            >
              {isUpdating ? (
                <span className="flex items-center">
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Saving...
                </span>
              ) : 'Save'}
            </button>
            <button
              onClick={handleCancel}
              disabled={isUpdating}
              className={`px-4 py-2 bg-gradient-to-r from-gray-500 to-gray-600 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-500 transition-all duration-200 shadow-md hover:shadow-lg transform hover:-translate-y-0.5 ${
                isUpdating
                  ? 'opacity-70 cursor-not-allowed'
                  : 'hover:from-gray-600 hover:to-gray-700'
              }`}
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <div className="flex items-start justify-between">
          <div className="flex items-start space-x-4 flex-1">
            <button
              onClick={() => onToggleComplete(task.id, !task.is_completed)}
              className={`mt-1 flex-shrink-0 h-6 w-6 rounded-full border-2 flex items-center justify-center transition-all duration-200 ${
                task.is_completed
                  ? 'bg-gradient-to-r from-green-500 to-emerald-500 border-green-500 text-white shadow-inner'
                  : 'border-gray-300 hover:border-blue-500 hover:bg-blue-50'
              }`}
              aria-label={task.is_completed ? 'Mark as incomplete' : 'Mark as complete'}
            >
              {task.is_completed && (
                <CheckCircleSolidIcon className="h-4 w-4 text-white" />
              )}
            </button>
            <div className="flex-1 min-w-0">
              <h3 className={`font-semibold text-lg ${task.is_completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
                {task.title}
              </h3>
              {task.description && (
                <p className={`mt-2 text-base ${task.is_completed ? 'line-through text-gray-400' : 'text-gray-600'}`}>
                  {task.description}
                </p>
              )}
              <div className="mt-3 flex flex-wrap items-center gap-3 text-xs text-gray-500">
                <span className="inline-flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  Created: {new Date(task.created_at).toLocaleDateString()}
                </span>
                {task.is_completed && (
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                    <CheckCircleSolidIcon className="h-3 w-3 mr-1" />
                    Completed
                  </span>
                )}
              </div>
            </div>
          </div>
          <div className="flex space-x-2 ml-4">
            <button
              onClick={() => setIsEditing(true)}
              className="p-2 text-gray-500 hover:text-blue-600 hover:bg-blue-50 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors duration-200 shadow-sm hover:shadow-md"
              aria-label="Edit task"
            >
              <PencilIcon className="h-5 w-5" />
            </button>
            <button
              onClick={() => onDelete(task.id)}
              disabled={isDeleting}
              className={`p-2 rounded-lg focus:outline-none focus:ring-2 transition-colors duration-200 shadow-sm hover:shadow-md ${
                isDeleting
                  ? 'cursor-not-allowed opacity-50'
                  : 'text-gray-500 hover:text-red-600 hover:bg-red-50 focus:ring-red-500'
              }`}
              aria-label={isDeleting ? "Deleting task..." : "Delete task"}
            >
              {isDeleting ? (
                <svg className="animate-spin h-5 w-5 text-red-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
              ) : (
                <TrashIcon className="h-5 w-5" />
              )}
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskItem;