import React from 'react';
import TaskItem from './task-item';
import { TodoTask } from '../../../../shared/types';
import { PlusIcon } from '@heroicons/react/24/outline';

interface TaskListProps {
  tasks: TodoTask[];
  onToggleComplete: (id: string, isCompleted: boolean) => void;
  onDelete: (id: string) => void;
  onUpdate: (id: string, updates: { title?: string; description?: string }) => void;
  onAddNewTask?: () => void;
  updatingTaskId?: string | null;
  deletingTaskId?: string | null;
}

const TaskList: React.FC<TaskListProps> = ({ tasks, onToggleComplete, onDelete, onUpdate, onAddNewTask, updatingTaskId, deletingTaskId }) => {
  if (tasks.length === 0) {
    return (
      <div className="text-center py-16">
        <div className="mx-auto w-24 h-24 bg-gradient-to-r from-blue-100 to-indigo-100 rounded-full flex items-center justify-center mb-6 shadow-md">
          <PlusIcon className="h-12 w-12 text-blue-500" />
        </div>
        <h3 className="text-xl font-semibold text-gray-900 mb-2">No tasks yet</h3>
        <p className="text-gray-500 mb-8 max-w-md mx-auto">Get started by creating your first task. Click the button below or use the form above to add your first todo item.</p>
        {onAddNewTask && (
          <button
            onClick={onAddNewTask}
            className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-300"
          >
            <PlusIcon className="-ml-1 mr-2 h-5 w-5" />
            Add your first task
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          onToggleComplete={onToggleComplete}
          onDelete={onDelete}
          onUpdate={onUpdate}
          isUpdating={updatingTaskId === task.id}
          isDeleting={deletingTaskId === task.id}
        />
      ))}
    </div>
  );
};

export default TaskList;