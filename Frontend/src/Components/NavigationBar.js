import React from "react";
import{Navbar, Nav} from "react-bootstrap";
import {LinkContainer} from "react-router-bootstrap";


function NavigationBar(){
    return (
        <Navbar bg="dark" variant="dark" sticky="top">
            <LinkContainer to="/">
                <Navbar.Brand>SMPLE</Navbar.Brand>
            </LinkContainer>
            <Nav>
                <LinkContainer to="/user/:id/courses">
                    <Nav.Link>My Courses</Nav.Link>
                </LinkContainer>
                <LinkContainer to="/user/:id">
                    <Nav.Link>Settings</Nav.Link>
                </LinkContainer>
            </Nav>
        </Navbar>
    )
}

export default NavigationBar;

//Reference: https://medium.com/how-to-react/use-react-router-link-with-bootstrap-315a8b88e129