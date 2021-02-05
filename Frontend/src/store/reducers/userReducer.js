const userReducer = (state = {}, action ) => {
	switch (action.type) {
		case "USER_LOADED":
			debugger
			return {
				...state,
				user:{...action.payload}
			}
		default:
			return state
	}
 }

 export default userReducer