/* StatusCard Component - will return "Loading ..." text while request is being
made, and list of Name, Url, Status Code, Duration and timestamp if successful.
In the event of an error, will return Name and Error text "*/

import React, { useState, useEffect } from 'react';
import StatusCardText from './StatusCardText';
import StatusCardErrorText from './StatusCardErrorText';
import StatusCardLabel from './StatusCardLabel';
import StatusCardLoadingText from './StatusCardLoadingText.js';

const axios = require('axios');

// TODO: The api interactions could be moved to a separate file. Not sure how to handle setting state
//       in that, though. Check on this.
const endpoints = {
	amazon: 'http://localhost/v1/amazon-status',
	google: 'http://localhost/v1/google-status',
	all: 'http://localhost/v1/all-status'
};

class StatusCard extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			statuses: [],
			error: false,
			loading: true
		};

		this.name = props.name;
		this.url = endpoints[props.endpoint];
		this.refreshSeconds = 60;
	}

	componentDidMount() {
		this.getSiteStatus(this.url);
		this.timerID = setInterval(() => this.getSiteStatus(this.url), this.refreshSeconds * 1000);
	}

	componentWillUnmount() {
		clearInterval(this.timerID);
	}

	getSiteStatus(url) {
		/* Gets response from a url and sets state of Statuses. Also sets Error and clears Loading statuses */

		this.setState({ loading: true });
		axios
			.get(url)
			.then((res) => {
				const d = res.data;

				// Statuses state is an array of objects
				if (d instanceof Array) {
					this.setState({ statuses: d });
				} else {
					this.setState({ statuses: [ d ] });
				}

				this.setState({
					loading: false,
					error: false
				});
			})
			.catch((err) => {
				this.setState({
					error: true,
					loading: false
				});
			});
	}

	render() {
		// Return value for Component
		if (this.state.loading) {
			return (
				<div className="status-card status-card-loading">
					<StatusCardLabel label={this.name} />
					<StatusCardLoadingText text="Loading ..." />
				</div>
			);
		} else if (this.state.error) {
			return (
				<div className="status-card status-card-error">
					<StatusCardLabel label={this.name} />
					<StatusCardErrorText text="Error!!!" />
				</div>
			);
		}

		return (
			<div className="status-card">
				<StatusCardLabel label={this.name} />
				{this.state.statuses.map((status) => {
					return [
						<div key={status['url']} className="status-card-contents">
							<StatusCardText label="URL" text={status['url']} />
							<StatusCardText label="Status Code" text={status['statusCode']} />
							<StatusCardText label="Duration" text={status['duration']} />
							<StatusCardText label="Timestamp" text={status['date']} />
						</div>
					];
				})}
			</div>
		);
	}
}

export default StatusCard;
