const userReducer = (state = {userProfile:{}, loading: false }, action ) => {
	switch (action.type) {
		case "LOADING_USER":
			return {
				...state,
				loading: true
			}
		case "USER_LOADED":
			return {
				...state,
				userProfile: {
				},
				loading: false
			}
		case "CREATE_USER":
			return {
				...state,
				userProfile: {
				},
				loading: false
			}
		default:
			return state
	}
 }

 export default userReducer