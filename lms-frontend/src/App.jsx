import './App.css'

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import LoginPage from './pages/Auth/LoginPage'
import SignupPage from './pages/Auth/Signup'

function App() {
  
  return (
    <div className='w-screen'>
      <Router>
        <Routes>
          <Route path='/' element={<LoginPage />} />
          <Route path='/signup' element={<SignupPage />} />
        </Routes>
      </Router>
    </div>
  )
}

export default App
