/* Main App for UI - will show three cards for Amazon, Google and a combined one containing both */

import './App.css';
import Header from './components/Header';
import StatusCard from './components/StatusCard';

function App() {
	return (
		<div className="App">
			<Header text="Status Dashboard" />
			<StatusCard name="Amazon" endpoint="amazon" />
			<StatusCard name="Google" endpoint="google" />
			<StatusCard name="Amazon & Google" endpoint="all" />
		</div>
	);
}

export default App;
