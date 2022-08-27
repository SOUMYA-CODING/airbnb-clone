import React from 'react'
import './AdminHome.scss'

const AdminHome = () => {
    return (
        <>
            <div>
                {/* Side Navbar */}
                <section className='side-navbar'>
                    <ul className="nav nav-pills">
                        <li><a href="index.html" className="nav-link"><i className="fa-solid fa-house"></i>
                            &nbsp; Dashboard</a></li>
                    </ul>
                    <ul className="nav nav-pills">
                        <li><a href="index.html" className="nav-link"><i className="fa-solid fa-users"></i> &nbsp;
                            Country</a></li>
                    </ul>
                    <ul className="nav nav-pills">
                        <li><a href="index.html" className="nav-link"><i className="fa-solid fa-bed"></i> &nbsp;
                            Hotels</a></li>
                    </ul>
                </section>
                {/* Main Container */}
                <section className='main-container'>
                    <header className='p-2'>
                        <nav>
                            <h4><strong>Dashboard</strong></h4>
                            <ul>
                                <li>Welcome</li>
                            </ul>
                        </nav>
                    </header>
                    {/* Body */}
                    
                </section>
            </div>
        </>
    )
}

export default AdminHome