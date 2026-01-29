'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '../contexts/auth-context';
import Header from '../components/ui/header';
import Footer from '../components/ui/footer';

export default function HomePage() {
  const router = useRouter();
  const { user, loading } = useAuth();

  // Redirect based on auth status
  useEffect(() => {
    if (!loading) {
      if (user) {
        router.push('/dashboard');
      } else {
        router.push('/login');
      }
    }
  }, [user, loading, router]);

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-blue-50 to-indigo-100">
      <Header title="Evolution of Todo" showAuthButtons={!user} showLogoutButton={!!user} />

      <main className="flex-grow flex items-center justify-center p-4">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            Welcome to Evolution of Todo
          </h1>
          <p className="text-lg text-gray-600 mb-8">
            Loading your personalized experience...
          </p>
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto"></div>
        </div>
      </main>

      <Footer />
    </div>
  );
}