import React, { useEffect } from 'react'
import {connect} from 'react-redux'
import './App.css';
import Container from "react-bootstrap/Container";
import Routes from "./Routes"
import NavigationBar from "./Components/NavigationBar"
import { getCourses } from './store/action/coursesAction';
import {getUser} from './store/action/userAction'

function App({getCourses, getUser}){
  useEffect(() => { getCourses(); getUser(); }, [getCourses, getUser])
  

  return (
      <Container fluid className="App">
        <NavigationBar/>
        <Routes/>
      </Container>
  );
}

export default connect(null, {getCourses, getUser})(App);