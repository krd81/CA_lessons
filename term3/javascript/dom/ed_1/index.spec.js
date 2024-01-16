/**
 * @jest-environment jsdom
 */

const {
	findAllAnchors,
	findFirstH3,
	findAllTextBlocks,
	findAllNestedParagraphs,
	findTheFooter,
} = require("./script.js")
const zenFile = require("./tests/zen.js")

describe("Testing CSS Zen Garden - ", () => {
    document.body.innerHTML = zenFile()
    test("findAllAnchors", () => {
		let anchors = findAllAnchors()
        expect(anchors.length).toEqual(32)
    })
    test("findFirstH3", () => {
		let h3 = findFirstH3()
        expect(h3.innerHTML).toBe("The Road to Enlightenment")
    })
    test("findAllTextBlocks", () => {
		let textBlocks = findAllTextBlocks()
        expect(textBlocks.length).toEqual(5)
    })
    test("findAllNestedParagraphs", () => {
		let nestedParagraphs = findAllNestedParagraphs()
        expect(nestedParagraphs.length).toEqual(5)
    })
    test("findTheFooter", () => {
		let footer = findTheFooter()
        expect(footer.children.length).toEqual(5)
    })
})
