import React from "react";
import styled from 'styled-components'
import Container from "react-bootstrap/Container";
import {useSelector} from 'react-redux'

function User() {
    const currentUser = useSelector(state => state.userReducer.user)
    return (
        <Container>
           <EditDebtFormWrapper>
				<StyledForm >
					<StyledH1>{currentUser.first_name + ' ' + currentUser.last_name}</StyledH1>
                    <br />
                    <h5>Email</h5>
					<span>{currentUser.email}</span>	
                </StyledForm>
			</EditDebtFormWrapper>
        </Container>
    )
}

export default User;

const EditDebtFormWrapper = styled.div`
	display: flex;
	justify-content: center;
	align-items:center;
	height: auto;
	width: auto;
	padding: 0 20px;
	boxing-size: border-box;
`

const StyledForm = styled.form`
	width: 100%;
	max-width: 700px;
	padding: 40px;
	background-color: white;
	border-radius: 10px;
	box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
	text-align: center;
	position: fixed;
    width: 80%;
    height: auto;
    top:50%;
    left:50%;
    transform: translate(-50%,-50%);
`

const StyledH1 = styled.h1`
  font-size: 1.5em;
  text-align: center;
  margin: 10px;
`;
