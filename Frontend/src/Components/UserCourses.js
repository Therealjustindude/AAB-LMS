import React from "react";
import {Container, Row, Col, Card, Button} from "react-bootstrap";

import {Link} from "react-router-dom";


const mockUserCourses = [
    {id:1,
    name: "JavaScript",
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque blandit porttitor arcu vitae suscipit. Aliquam at suscipit justo."
    },
    {id:3,
    name: "HTML",
    description: "Nullam dictum erat leo, ac feugiat augue varius vitae. In mattis vulputate nisl at imperdiet. Nulla aliquam gravida velit eu auctor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam tristique sed turpis non rhoncus. Aenean congue nibh nec magna tincidunt, ut tristique libero tincidunt."
    },
    {id: 5,
    name: "Java",
    description: "Curabitur sollicitudin bibendum libero, nec aliquet velit tempor a. Curabitur mauris risus, maximus id sollicitudin et, eleifend id nibh. Maecenas rutrum semper nisi, vitae posuere orci vulputate eu. "
    },
    
]
//Make GET call for baseURL/users/id/courses

function UserCourses(){
    return(
        <Container>
            <h3>Will Display User Courses</h3>
            <Row>
            {mockUserCourses.map((course)=>{
                return (
                    <Col key={course.id} sm={12} md={6} lg={4} xl={4}>
                    <Card>
                        <Card.Header><Link to={`/Courses/${course.name}`}>{course.name}</Link></Card.Header>
                        <Card.Body>
                            <Card.Img variant="top" src="http://www.abcteach.com/free/b/book01_rgb2.jpg"/>
                            <Card.Text className="description-truncate">{course.description}</Card.Text>
                            <Button variant="danger">Leave Course</Button>
                        </Card.Body>
                    </Card>
                    </Col>
                )
            })}</Row>
        </Container>
    )
}

export default UserCourses;