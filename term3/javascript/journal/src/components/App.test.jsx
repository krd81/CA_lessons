import "@testing-library/jest-dom"
import { render, screen } from "@testing-library/react"
import { describe, expect, it, beforeEach } from "vitest"
import App from "./App"
import { userEvent } from "@testing-library/user-event"


describe('App Component', () => {
    let container

    beforeEach(() => {
        container = render(< App />).container
    })

    it('renders the Home component', () => {
        // const { container } = render(< App />)
        expect(container.querySelector('h3')).toHaveTextContent('Journal Entries')
    })

    it('renders CategorySelection when Create Entry menu item is clicked', async () => {
        // const { container } = render(< App />)

       await userEvent.click(screen.getByText('Create New Entry'))

       expect(container.querySelector('h3')).not.toBeNull()
       expect(container.querySelector('h3')).toHaveTextContent('Please select a category:')

    })
})





// describe('App Component', () => {
//     it('renders the Home component', () => {
//         render(
//             < App />
//         )
//         expect(screen.getByText('Journal Entries')).toBeDefined()

//     })
// })
