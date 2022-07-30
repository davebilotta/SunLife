function StatusCardText(props) {
	return (
		<div>
			<span className="status-card-text-label">{props.label}:</span>
			<span className="status-card-text-value">{props.text}</span>
		</div>
	);
}

export default StatusCardText;
