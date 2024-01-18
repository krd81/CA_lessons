module.exports = function() {
    return `
		<div id="container">
			<div class="column">
				<form>
					<div>
						<label for="name">Name:</label>
						<input id="name"/>
					</div>
					<div>
						<label for="language">Language:</label>
						<input id="language"/>
					</div>
					<div>
						<label for="cohort">Cohort:</label>
						<input id="cohort"/>
					</div>
					<button id="challenge-one">Submit Form</button>
				</form>
				<p id="output"></p>
			</div>
			<div class="column" id="challenge-two">
				<button id="change-theme">Dark Mode</button>
			</div>
            <div id="last" class="column">
				<div class="drag" id="from">
					<div id="dragger" draggable="true"></div>
	 			</div>
				<div class="drag"></div>
				<div class="drag"></div>
				<div class="drag"></div>
				<div class="drag"></div>
				<div class="drag"></div>
				<div class="drag"></div>
				<div class="drag"></div>
				<div class="drag"></div>
				<div class="drag" id="to"></div>
			</div>
		</div>
    `
}
