import { BrowserRouter, Route, Routes } from "react-router-dom"
import { ToastContainer } from "react-toastify"
import Home from "./Home"
import Login from "./Login"
import Register from "./Register"
export default function App() {

  return (
    <div className="App">
    <ToastContainer theme='colored' position='top-right'></ToastContainer>
    <BrowserRouter>
    {/* <Appheaderclear></Appheaderclear> */}
    <Routes>
      <Route path='/' element={<Home/>}></Route>
      <Route path='/login' element={<Login/>}></Route>
      <Route path='/register' element={<Register/>}></Route>
    </Routes>
    
    </BrowserRouter>
    
  </div>
  )
}