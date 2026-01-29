import React from 'react';

interface CompletionToggleProps {
  isCompleted: boolean;
  onToggle: () => void;
  disabled?: boolean;
}

const CompletionToggle: React.FC<CompletionToggleProps> = ({ isCompleted, onToggle, disabled = false }) => {
  return (
    <button
      onClick={onToggle}
      disabled={disabled}
      className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 ${
        isCompleted ? 'bg-green-500' : 'bg-gray-300'
      } ${disabled ? 'opacity-50 cursor-not-allowed' : 'hover:opacity-80'}`}
      aria-checked={isCompleted}
      role="switch"
    >
      <span
        className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
          isCompleted ? 'translate-x-6' : 'translate-x-1'
        }`}
      />
    </button>
  );
};

export default CompletionToggle;