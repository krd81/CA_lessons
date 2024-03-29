import React, { useRef } from 'react'
import { Link } from "react-router-dom"


const Navbar = () => {
    const navBarRef = useRef();

    function toggeleHamburger(event) {
        event.target.classList.toggle('is-active')
        navBarRef.current.classList.toggle('is-active')
    }

    return (

        <nav className="navbar is-primary" role="navigation" aria-label="main navigation">
        <div className="navbar-brand">
        <Link to="/" className="navbar-item">
            <h1>Journal</h1>
        </Link>
            <a role="button" onClick={toggeleHamburger} className="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" onClick={toggeleHamburger} ref={navBarRef} className="navbar-menu">
            <div className="navbar-start">
            <Link to="/" className="navbar-item">
                Home
            </Link>

            <Link to="/category" className="navbar-item">
                Create New Entry
            </Link>

            </div>

        </div>
        </nav>
  )
}

export default Navbar