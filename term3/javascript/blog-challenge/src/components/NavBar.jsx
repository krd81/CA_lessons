import React, { useState } from 'react'
import { Link } from 'react-router-dom';

const NavBar = () => {

    const [isActive, setIsActive] = useState(false);

  return (
    <>
    <nav className="navbar is-link" role="navigation" aria-label="main navigation">
        <div className="navbar-brand">
            {/* <a className="navbar-item" href="https://bulma.io"> */}
                {/* <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28" /> */}
            {/* </a> */}

            <a role="button" className={`navbar-burger burger ${isActive ? "is-active" : ""}`} onClick={() => {setIsActive(!isActive)}} aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" className={`navbar-menu ${isActive ? "is-active" : ""}`}>
            <div className="navbar-start">
                <Link to="/" className="navbar-item">
                    Home
                </Link>

                <Link to="/articles" className="navbar-item">
                    Articles
                </Link>

                <div className="navbar-item has-dropdown is-hoverable">
                    <Link to="/" className="navbar-link">
                        More
                    </Link>

                    <div className="navbar-dropdown">
                        <Link to="/" className="navbar-item">
                            About
                        </Link>
                        <Link to="/" className="navbar-item">
                            Jobs
                        </Link>
                        <Link to="/" className="navbar-item">
                            Contact
                        </Link>
                        <hr className="navbar-divider" />
                        <Link to="/" className="navbar-item">
                            Report an issue
                        </Link>
                    </div>
                </div>
            </div>

            <div className="navbar-end">
                <div className="navbar-item">
                    <div className="buttons">
                        <a className="button is-primary">
                            <strong>Sign up</strong>
                        </a>
                        <a className="button is-light">
                            Log in
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    </>
  )
}

export default NavBar