import { Link } from "react-router-dom";
import axios from "axios";
import React, { useState, useEffect } from "react";

function Navbar() {
  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
  const [newsData, setNewsData] = useState([]);
  function handleDownloadExcel() {
    try {
        
      axios.get(`${apiBaseUrl}/news/news-article/`).then((response) => {
        setNewsData(response.data);
      });

      console.log("hehah");
      console.log(newsData);
      // Create a new Excel workbook
      const xlsx = require("xlsx");
      const wb = xlsx.utils.book_new();
      const ws = xlsx.utils.json_to_sheet([]);

      // Add column headers
      const columnHeaders = [
        "title",
        "content",
        "source",
        "link",
        "location",
        "time",
        "vehicles",
        "dead",
        "injured",
      ];
      xlsx.utils.sheet_add_aoa(ws, [columnHeaders], { origin: -1 }); // -1 means at the beginning

      // Loop through the data and add rows
      newsData.forEach((newsItem) => {
        const rowData = [
          newsItem.title,
          newsItem.content,
          newsItem.source,
          newsItem.link,
          newsItem.parameters.location,
          newsItem.parameters.time,
          newsItem.parameters.vehicles,
          newsItem.parameters.dead,
          newsItem.parameters.injured,
        ];
        xlsx.utils.sheet_add_aoa(ws, [rowData], { origin: -1 }); // -1 means at the beginning
      });

      // Add the worksheet to the workbook
      xlsx.utils.book_append_sheet(wb, ws, "News Data");

      // Generate a Blob containing the Excel data
      const blob = xlsx.write(wb, { bookType: "xlsx", type: "blob" });

      // Create a URL for the Blob and trigger the download
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "news_data.xlsx";
      a.click();

      // Clean up the URL object
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error("Error downloading Excel file:", error);
    }
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark ">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/allnews">
          Road Accident Info
        </Link>
        {/* <Button classNameName="navbar-brand">Navbar</Button> */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link
                to="/allnews"
                className="nav-link active"
                aria-current="page"
              >
                All news
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link"></Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link disabled"></Link>
            </li>
          </ul>
          <button
            className="btn btn-md btn-success me-2"
            aria-current="page"
            onClick={handleDownloadExcel}
          >
            Export to Excel
          </button>

          <form className="d-flex">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            ></input>
            <button className="btn btn-outline-success" type="submit">
              Search
            </button>
          </form>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
