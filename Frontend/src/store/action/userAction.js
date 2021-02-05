const BASE_URL = "http://127.0.0.1:5000/backend"

export const getUser = () => {
    return ((dispatch) => {
        fetch(`${BASE_URL}/users`,{
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        })
            .then(res => res.json())
            .then(res => { 
                // console.log("Here's your results:", res.users)
                //send first user to reducer for now
                dispatch({type: "USER_LOADED", payload: res.users[1]})
            })
            .catch(error => {
                console.log("Error fetching from database:", error)
            })
    })
}