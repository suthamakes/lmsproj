"use client"

import { useState } from "react"

export default function LoginPage() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [isLoading, setIsLoading] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault()
        setIsLoading(true)
        setTimeout(() => {
            setIsLoading(false)
        }, 1000)
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
            <div className=" bg-white rounded-xl shadow-2xl flex justify-center">
                {/* Left side - Login form */}
                <div className="w-1/2 p-12 flex flex-col justify-center">
                    <div className="mb-8">
                        <div className="flex items-start gap-3 mb-2">
                            <div className="w-12 h-12 rounded-full bg-gradient-to-br from-red-500 via-yellow-400 to-blue-500 flex items-center justify-center text-white font-bold text-sm flex-shrink-0">
                                KU
                            </div>
                            <div>
                                <h2 className="text-3xl font-bold text-gray-900">Kathmandu University</h2>
                                <p className="text-sm text-gray-600">Learning Management System</p>
                            </div>
                        </div>
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-4">
                        <input
                            type="text"
                            placeholder="Username or email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full px-4 py-3 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                            required
                        />
                        <input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full px-4 py-3 border border-gray-300 rounded focus:border-blue-500 focus:outline-none"
                            required
                        />
                        <button
                            type="submit"
                            disabled={isLoading}
                            className="w-full py-3 bg-gray-900 text-white font-semibold rounded hover:bg-gray-800"
                        >
                            {isLoading ? "Logging in..." : "Log in"}
                        </button>
                    </form>

                    <div className="mt-6 text-center">
                        <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                            Lost password?
                        </a>
                    </div>
                </div>

                {/* Right side - Sign in section */}
                <div className="w-1/2 p-12 bg-gray-50 flex flex-col justify-start pt-20">
                    <h2 className="text-xl font-bold text-gray-900 mb-6">Sign in with</h2>

                    <button className="w-full py-3 px-4 bg-gray-900 text-white rounded hover:bg-gray-800 flex items-center justify-center gap-2 font-medium mb-6">
                        <svg className="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
                        </svg>
                        Login with KU Email
                    </button>

                    <p className="text-sm text-gray-700 leading-relaxed">
                        Kathmandu University students can log in using their official KU email (e.g., username@student.ku.edu.np).
                    </p>
                    <p className="text-sm text-gray-700 leading-relaxed mt-3">
                        Click <span className="font-semibold">"Login with KU Email"</span> to enter the e-Learning Forum.
                    </p>
                </div>
            </div>
        </div>
    )
}
