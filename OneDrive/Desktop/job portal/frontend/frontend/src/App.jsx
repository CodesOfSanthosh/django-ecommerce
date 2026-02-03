import { useState } from 'react'
import './App.css'
import RegisterPage from './components/RegisterPage'
import LoginPage from './components/LoginPage'
import JobListPage from './components/JobListPage'
import ApplyJobPage from './components/ApplyJobPage'
import { BrowserRouter , Routes, Route} from 'react-router-dom'
function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/login' element={<LoginPage />} />
        <Route path='/register' element={<RegisterPage />} />
        <Route path='/jobs' element={<JobListPage />} />
        <Route path='/apply/:jobId' element={<ApplyJobPage />} />

        </Routes>
    </BrowserRouter>
  )
}

export default App
