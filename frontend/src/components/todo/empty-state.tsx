import React from 'react';

interface EmptyStateProps {
  message?: string;
  action?: () => void;
  actionText?: string;
}

const EmptyState: React.FC<EmptyStateProps> = ({
  message = "You don't have any tasks yet.",
  action,
  actionText = "Create your first task"
}) => {
  return (
    <div className="text-center py-12">
      <div className="mx-auto h-24 w-24 flex items-center justify-center rounded-full bg-gray-100">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-12 w-12 text-gray-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
          />
        </svg>
      </div>
      <h3 className="mt-2 text-lg font-medium text-gray-900">{message}</h3>
      <p className="mt-1 text-sm text-gray-500">
        Get started by creating your first task.
      </p>
      {action && (
        <div className="mt-6">
          <button
            type="button"
            onClick={action}
            className="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            {actionText}
          </button>
        </div>
      )}
    </div>
  );
};

export default EmptyState;