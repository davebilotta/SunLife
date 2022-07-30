import { useState, useEffect } from 'react';
import StatusCardText from './StatusCardText';
import StatusCardErrorText from './StatusCardErrorText';
import StatusCardLabel from './StatusCardLabel';
import StatusCardLoadingText from './StatusCardLoadingText.js';

const axios = require('axios');

// TODO: The api interactions could be moved to a separate file. Not sure how to handle setting state
//       in that, though. Check on this
const endpoints = {
	amazon: 'http://localhost/v1/amazon-status',
	google: 'http://localhost/v1/google-status',
	all: 'http://localhost/v1/all-status'
};

function StatusCard(props) {
	const [ loading, setLoading ] = useState(false);
	const [ error, setError ] = useState(false);
	const [ statuses, setStatuses ] = useState([]);

	const name = props.name;
	const url = endpoints[props.endpoint];

	useEffect(() => {
		getSite(url);
	}, []);

	const getSite = (url) => {
		/* Gets response from a url and sets state of Statuses. Also sets Error and clears Loading statuses */
		setLoading(true);
		axios
			.get(url)
			.then((res) => {
				const d = res.data;
				if (d instanceof Array) {
					setStatuses(d);
				} else {
					setStatuses([ d ]);
				}

				setLoading(false);
			})
			.catch((err) => {
				setError(true);
				setLoading(false);
			});
	};

	// Return value for Component
	if (loading) {
		return (
			<div className="status-card">
				<StatusCardLabel label={name} />
				<StatusCardLoadingText text="Loading ..." />
			</div>
		);
	} else if (error) {
		return (
			<div className="status-card">
				<StatusCardLabel label={name} />
				<StatusCardErrorText text="Error" />
			</div>
		);
	}

	return (
		<div className="status-card">
			<StatusCardLabel label={name} />
			{statuses.map((status) => {
				return [
					<StatusCardText label="URL" text={status['url']} />,
					<StatusCardText label="Status Code" text={status['statusCode']} />,
					<StatusCardText label="Duration" text={status['duration']} />,
					<StatusCardText label="Timestamp" text={status['date']} />
				];
			})}
		</div>
	);
}

export default StatusCard;
