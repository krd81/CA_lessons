module.exports = function() {
    return `
		<div id="container">
			<div class="column">
				<button id="five">+5</button>
				<button id="ten" >+10</button>
				<button id="fifteen">+15</button>
				<p id="counter-one">0</p>
			</div>
			<div class="column">
				<button value=1 class='challenge-two'>Increment</button>
				<button value=-1 class='challenge-two'>Decrement</button>
				<button id="stop">Stop</button>
				<p id="counter-two">0</p>
			</div>
		</div>
		<script src="./script.js"></script>
		<script>activity()</script>
	</body>
    `
}
