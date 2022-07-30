import './App.css';
import StatusCard from './components/StatusCard';

function App() {
	return (
		<div className="App">
			<StatusCard name="Amazon" endpoint="amazon" />
			<StatusCard name="Google" endpoint="google" />
			<StatusCard name="Amazon & Google" endpoint="all" />
		</div>
	);
}

export default App;
