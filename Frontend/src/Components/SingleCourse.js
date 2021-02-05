import React from "react";

import {Container, Card} from "react-bootstrap";

const mockProps = {
    id:1,
    name: "JavaScript",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque blandit porttitor arcu vitae suscipit. Aliquam at suscipit justo."
}

//Make a GET call to backend with course id: /Courses/:id

function SingleCourse(){
    return(
        <Container className="single-course">
            <Card>
                <Card.Body>
                    <Card.Img src="http://www.abcteach.com/free/b/book01_rgb2.jpg"></Card.Img>
                    <Card.Title>{mockProps.name||"Name"}</Card.Title>
                    <Card.Text>{mockProps.description||"Description"}</Card.Text>
                </Card.Body>
            </Card>
        </Container>
    )
}

export default SingleCourse;