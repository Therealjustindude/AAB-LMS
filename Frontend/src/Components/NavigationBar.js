import React from "react";
import{Navbar, Nav} from "react-bootstrap";
import {LinkContainer} from "react-router-bootstrap";


function NavigationBar(){
    return (
        <Navbar bg="dark" variant="dark" sticky="top">
            <LinkContainer to="/">
                <Navbar.Brand>AAB-LMS</Navbar.Brand>
            </LinkContainer>
            <Nav>
                <LinkContainer to="/Courses">
                    <Nav.Link>Courses</Nav.Link>
                </LinkContainer>
                <LinkContainer to="/Profile">
                    <Nav.Link>Profile</Nav.Link>
                </LinkContainer>
            </Nav>
        </Navbar>
    )
}

export default NavigationBar;

//Reference: https://medium.com/how-to-react/use-react-router-link-with-bootstrap-315a8b88e129