function activity() {
    // 1. Anchor code here
    // let anchor = document.querySelector("a")
    // anchor.innerText = "DOM Manipulation"
    document.querySelector("a").textContent = "DOM Manipulation"

    // 2. List Item code here
    let ul = document.querySelector("ul")
    let lastListItem = ul.children[ul.children.length-1]
    ul.removeChild(lastListItem)

    // 3. Form code here
    let form = document.getElementById("page-form")
    let label = document.createElement("label")
    label.textContent = "Name:"
    form.prepend(label)

    // 4. Paragraph code here
    let div = document.getElementById("question")
    let p = document.createElement("p")
    p.textContent = "42"
    div.appendChild(p)
}

// Don't remove this
activity()
