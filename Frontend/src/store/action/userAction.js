const BASE_URL = "http://127.0.0.1:5000/backend"

export const getUser = () => {
    return (() => {
        fetch(`${BASE_URL}/users`,{
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        })
            .then(res => res.json())
            .then(res => { 
                console.log("Here's your results:", res)
            })
            .catch(error => {
                console.log("Error fetching from database:", error)
            })
    })
}