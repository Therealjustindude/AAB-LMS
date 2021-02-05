import { combineReducers } from 'redux'
import userReducer from './userReducer'
import coursesReducer from './coursesReducer'


const rootReducer = combineReducers({
	userReducer,
	coursesReducer
})

export default rootReducer;