module.exports = function indexFile() {
    return `
		<h1>Welcome</h1>
		<p>This page is used for practicing <a href="https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model">click here</a></p>
        <p>Open a web preview in another tab for this to work.</p>
		<div>
			<p>We will be learning</p>
			<ul>
				<li class="odd">Adding To The DOM</li>
				<li>Querying The DOM</li>
				<li class="odd">Changing The DOM</li>
				<li>Event Listeners</li>
			</ul>
		</div>
		<div id="question">
			<p>The Answer to the Ultimate Question of Life, The Universe, and Everything:</p>
		</div>
		<form id="page-form">
			<input type="text" />
			<input type="submit" value="Click Me" />
		</form>
    `
}
