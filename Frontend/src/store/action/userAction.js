export const getUser = (data, browserHistory) => {
	return ((dispatch) => {
		dispatch({ type: "LOADING_USER" })
		return fetch('',{
			method: "GET",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			}
		})
			.then(res => res.json())
			.then(res => { 
				if (res.error) {
					browserHistory.push('/')
					alert("Something went wrong!")
				} else {
					dispatch({ type: "USER_LOADED", payload: res.user })
					browserHistory.push(`/users/${res.user.id}`)
				}
			})
	})
}