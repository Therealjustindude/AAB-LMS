import React, { useEffect } from 'react'
import {connect} from 'react-redux'
import './App.css';
import Container from "react-bootstrap/Container";
import Routes from "./Routes"
import NavigationBar from "./Components/NavigationBar"
import {getUser} from './store/action/userAction'

function App({getUser}){
  useEffect(()=>{getUser()},[getUser])
  return (
      <Container fluid className="App">
        <NavigationBar/>
        <Routes/>
      </Container>
  );
}

export default connect(null, {getUser})(App);