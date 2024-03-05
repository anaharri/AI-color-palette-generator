const form = document.querySelector("#form");

form.addEventListener("submit", e => {
	e.preventDefault();
	getColors();
});

function getColors() {
	query = form.elements.query.value;

	fetch("/palette", {
		method: "POST",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded",
		},
		body: new URLSearchParams({
			query,
		}),
	})
		.then(response => response.json())
		.then(colors => {
			const container = document.querySelector(".container");

			createColorBlocks(colors, container);
		})
		.catch(e => console.error(e));

	form.elements.query.value = "";
}

function createColorBlocks(colors, container) {
	container.innerHtml = "";

	for (const color of colors) {
		const div = document.createElement("div");

		div.classList.add("color");
		div.style.backgroundColor = color;
		div.style.width = `calc(100%/${colors.length})`;

		div.addEventListener("click", () => {
			navigator.clipboard.writeText(color);
		});

		const span = document.createElement("span");
		span.innerText = color;
		div.appendChild(span);

		container.appendChild(div);
	}
}
