import React from 'react'
import { Link } from "react-router-dom";
import axios from "axios";

function Navbar() {

    const handleExportToExcel = async () => {
        console.log("helloo")
        const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
        axios.get(`${apiBaseUrl}/exportsheet/save`).then((response) => {
        });
      };
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark ">
        <div className="container-fluid">
            <Link  className="navbar-brand" to="/allnews">Road Accident Info</Link>
            {/* <Button classNameName="navbar-brand">Navbar</Button> */}
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item">
                <Link to="/allnews" className="nav-link active" aria-current="page" >All news</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" ></Link>
                </li>
                <li className="nav-item">
                <Link className="nav-link disabled"></Link>
                </li>
            </ul>
            <button className="btn btn-md btn-success me-2" aria-current="page" onClick={handleExportToExcel}>Export to Excel</button>

            <form className="d-flex">
                <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
                <button className="btn btn-outline-success" type='submit'>Search</button>
            </form>
            
            </div>
        </div>
</nav>
  )
}

export default Navbar