import { useState } from 'react'
import {Route,BrowserRouter,Routes}from 'react-router-dom'
import{Sender} from './components/Sender'
import{Receiver} from './components/Receiver'
import './App.css'
//localhost/sender
//localhost/receiver
//react-router-dom
function App() {
  const [count, setCount] = useState(0)

  return (
    <>{/** create sender route and receive router */}
    <BrowserRouter>
    <Routes>
      <Route path='/sender' element={<Sender/>}/>
      <Route path='/receiver' element={<Receiver/>}/>
    </Routes>
    </BrowserRouter>
      
    </>
  )
}

export default App
