const coursesReducer = (state = {}, action ) => {
	switch (action.type) {
		case "COURSES_LOADED":
			return {
				...state,
				courses:[...action.payload]
			}
		default:
			return state
	}
 }

 export default coursesReducer