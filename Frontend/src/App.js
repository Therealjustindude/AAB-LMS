// imports for redux
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './store/reducers/indexReducer'


import './App.css';
import Container from "react-bootstrap/Container";
import Routes from "./Routes"
import NavigationBar from "./Components/NavigationBar"

// create redux store
const store = createStore(rootReducer, applyMiddleware(thunk))

function App() {
  return (
    <Provider store={store}>
      <Container fluid className="App">
        <NavigationBar/>
        <Routes/>
      </Container>
    </Provider>
  );
}

export default App;
