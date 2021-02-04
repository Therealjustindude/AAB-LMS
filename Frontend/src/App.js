
import './App.css';
import Container from "react-bootstrap/Container";
import Routes from "./Routes"
import NavigationBar from "./Components/NavigationBar"

function App() {
  return (
      <Container fluid className="App">
        <NavigationBar/>
        <Routes/>
      </Container>
  );
}

export default App;
