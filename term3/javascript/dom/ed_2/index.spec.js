/**
 * @jest-environment jsdom
 */

const indexFile = require("./tests/indexFile.js")
document.body.innerHTML = indexFile()
describe("Anchor should - ", () => {
    require("./script.js")
    test("have correct text", () => {
        let anchors = document.querySelectorAll("a")
        expect(anchors.length).toEqual(1)
        expect(anchors[0].innerHTML).toEqual("DOM Manipulation")
    })
})

describe("ul should - ", () => {
    let ul = document.querySelector("ul")
    let children = ul.children
    test(" only have 3 list items", () => {
        expect(children.length).toEqual(3)
    })
    test("remove the Event Listener li", () => {
        expect(children[children.length-1].innerHTML).toEqual("Changing The DOM")
    })
})

describe("form should - ", () => {
    let form = document.querySelector("form")
    let lbl = document.querySelector("label")
    test("have a label", () => {
        expect(lbl.parentElement).toEqual(form)
    })
    test("have label before text fields", () => {
        expect(form.children[0]).toEqual(lbl)
    })
    test("have label with correct text", () => {
        expect(lbl.innerHTML).toEqual("Name:")
    })
})

describe("Question div should - ", () => {
    let questionDiv = document.getElementById('question')
    test("have 2 paragraph tags", () => {
        expect(questionDiv.children.length).toEqual(2)
    })
    test("have the correct answer", () => {
        expect(questionDiv.lastChild.innerHTML).toEqual("42")
    })
})
