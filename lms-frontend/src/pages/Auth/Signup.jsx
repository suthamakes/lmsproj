"use client"

import { useState } from "react"

export default function SignupPage() {
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [confirmPassword, setConfirmPassword] = useState("")
    const [isLoading, setIsLoading] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault()
        setIsLoading(true)
        setTimeout(() => {
            setIsLoading(false)
        }, 1000)
    }

    return (
        <div className="w-full h-screen flex items-center justify-center bg-gray-100 p-4">
            <div className="w-3/5 bg-white rounded-xl shadow-2xl flex justify-center">

                {/* Left side - Signup form */}
                <div className="w-1/2 p-12 flex flex-col justify-center">
                    <div className="mb-8">
                        <div className="flex items-start gap-3 mb-2">
                            <div className="w-12 h-12 rounded-full bg-linear-to-br from-red-500 via-yellow-400 to-blue-500 flex items-center justify-center text-white font-bold text-sm shrink-0">
                                KU
                            </div>
                            <div>
                                <h2 className="text-3xl font-bold text-gray-900">
                                    Kathmandu University
                                </h2>
                                <p className="text-sm text-gray-600">
                                    Learning Management System
                                </p>
                            </div>
                        </div>
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-5">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Full Name
                            </label>
                            <input
                                type="text"
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                className="w-full px-4 py-3 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                                required
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Email address
                            </label>
                            <input
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                className="w-full px-4 py-3 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                                required
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Password
                            </label>
                            <input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                className="w-full px-4 py-3 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                                required
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                Confirm password
                            </label>
                            <input
                                type="password"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                className="w-full px-4 py-3 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                                required
                            />
                        </div>

                        <button
                            type="submit"
                            disabled={isLoading}
                            className="w-full py-3 bg-gray-900 text-white font-semibold rounded hover:bg-gray-800"
                        >
                            {isLoading ? "Creating account..." : "Create account"}
                        </button>
                    </form>

                    <div className="mt-6 text-center">
                        <a
                            href="/"
                            className="text-blue-600 hover:text-blue-700 font-medium"
                        >
                            Already have an account? Log in
                        </a>
                    </div>
                </div>

                {/* Right side - Information section */}
                <div className="w-1/2 p-12 bg-gray-50 flex flex-col justify-start pt-20">
                    <h2 className="text-xl font-bold text-gray-900 mb-6">
                        Create your account
                    </h2>

                    <p className="text-sm text-gray-700 leading-relaxed">
                        Register to access Kathmandu University’s Learning Management System.
                        Manage courses, assignments, learning resources, and academic updates
                        from a single platform.
                    </p>

                    <p className="text-sm text-gray-700 leading-relaxed mt-4">
                        For best results, use your official KU email address during registration.
                    </p>
                </div>
            </div>
        </div>
    )
}
