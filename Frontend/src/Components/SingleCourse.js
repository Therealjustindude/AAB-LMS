import React from "react";

import {Container, Card, Row, Col} from "react-bootstrap";

const mockProps = {
    id:1,
    name: "Course Name",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque blandit porttitor arcu vitae suscipit. Aliquam at suscipit justo. Nullam dictum erat leo, ac feugiat augue varius vitae. In mattis vulputate nisl at imperdiet. Nulla aliquam gravida velit eu auctor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam tristique sed turpis non rhoncus. Aenean congue nibh nec magna tincidunt, ut tristique libero tincidunt."
}

const mockStudents = [
    {'id':1, 'first_name': 'Joely', 'last_name': 'Mcgill'},
    {'id':3,'first_name': 'Hadley', 'last_name': 'Bernard'},
    {'id':6,'first_name': 'Aisha', 'last_name': 'Shelton'},
    {'id':11,'first_name': 'Eloise', 'last_name': 'Ahmed'},
    {'id':8,'first_name': 'Rex', 'last_name': 'Sullivan'}
]


//Make a GET call to backend with course id: baseURL/courses/:course_id
//Also GET list of students in this class

function SingleCourse(){
    return(
        <Container className="single-course">
            <Container className="content">
                <Row>
                    <Col xs={12} sm={12} md={6} lg={4}>
                        <Card.Img src="http://www.abcteach.com/free/b/book01_rgb2.jpg"></Card.Img>
                    </Col>
                    <Col className="details">
                        <Card.Title>{mockProps.name||"Name"}</Card.Title>
                        <Card.Text>{mockProps.description||"Description"}</Card.Text>
                    </Col>
                </Row>
            </Container>
                <Row className="roster-row">
                    <Col xs={12} sm={12} md={7} >
                        <Card >
                            <h3>Class Roster</h3>
                            <div>{mockStudents.map(student=>{
                                return (
                                    <div key={student.id}>
                                        <div>{student.first_name} {student.last_name}</div>
                                    </div>
                                )
                            })}</div>
                        </Card>
                    </Col>
                </Row>
        </Container>
    )
}

export default SingleCourse;