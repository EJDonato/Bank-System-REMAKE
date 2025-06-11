
import './App.css'

import Landing from './pages/Landing/landing'
import Homepage from './pages/Homepage/homepage'
import Pending from './pages/Pending/pending'

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/pending_account" element={<Pending />}/>
          <Route path="/homepage/:userType/:userName" element={<Homepage />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
