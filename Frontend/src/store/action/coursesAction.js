const BASE_URL = "http://127.0.0.1:5000/backend"

export const getCourses = () => {
    return ((dispatch) => {
        fetch(`${BASE_URL}/courses`,{
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        })
            .then(res => res.json())
            .then(res => { 
                dispatch({type: "COURSES_LOADED", payload: res.courses})
            })
            .catch(error => {
                console.log("Error fetching from database:", error)
            })
    })
}