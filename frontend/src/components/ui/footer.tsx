import React from 'react';
import Link from 'next/link';

const Footer: React.FC = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-white border-t border-gray-200 mt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="md:flex md:items-center md:justify-between">
          <div className="flex items-center space-x-3 mb-6 md:mb-0">
            <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">E</span>
            </div>
            <span className="text-lg font-semibold text-gray-900">Evolution of Todo</span>
          </div>

          <div className="flex flex-col md:flex-row md:space-x-8 space-y-2 md:space-y-0">
            <Link
              href="/privacy"
              className="text-sm text-gray-600 hover:text-blue-600 transition-colors duration-200"
            >
              Privacy Policy
            </Link>
            <Link
              href="/terms"
              className="text-sm text-gray-600 hover:text-blue-600 transition-colors duration-200"
            >
              Terms of Service
            </Link>
            <Link
              href="/support"
              className="text-sm text-gray-600 hover:text-blue-600 transition-colors duration-200"
            >
              Support
            </Link>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-200">
          <p className="text-center text-sm text-gray-500">
            &copy; {currentYear} Evolution of Todo. All rights reserved. Empowering productivity, one task at a time.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;