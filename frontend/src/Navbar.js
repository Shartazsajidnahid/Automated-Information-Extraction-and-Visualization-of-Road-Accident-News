import { Link } from "react-router-dom";
import axios from "axios";
import React, { useState, useEffect } from "react";
import ExcelJS from "exceljs";


function Navbar() {
  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
  // const [newsData, setNewsData] = useState([]);

  async function exportNewsDataToExcel(newsData) {
    // Create a new Excel file
    const workbook = new ExcelJS.Workbook();
  
    // Add a new worksheet to the Excel file
    const worksheet = workbook.addWorksheet("News Data");
  
    // Set the column headers for the worksheet
    worksheet.columns = [

      { header: "Title" },
      { header: "Content" },
      { header: "Link" },
      { header: "Location" },
      { header: "Time" },
      { header: "Vehicles" },
      { header: "Dead" },
      { header: "Injured" },
      { header: "Source" },
    ];
  
    // Iterate over the news data array and add each object to the worksheet
    newsData.forEach((newsItem) => {
      const row = worksheet.addRow();
      // Set the cell values for each column in the worksheet
      row.getCell(1).value = newsItem.title;
      row.getCell(2).value = newsItem.content;
      row.getCell(3).value = newsItem.link;
      row.getCell(4).value = newsItem.parameters.location;
      row.getCell(5).value = newsItem.parameters.time;
      row.getCell(6).value = newsItem.parameters.vehicles;
      row.getCell(7).value = newsItem.parameters.dead;
      row.getCell(8).value = newsItem.parameters.injured;
      row.getCell(9).value = newsItem.source;
    });
  
    // Save the Excel file to the user's browser
    const buffer = await workbook.xlsx.writeBuffer();
    const blob = new Blob([buffer], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
    const url = URL.createObjectURL(blob);
  
    const downloadLink = document.createElement("a");
    downloadLink.href = url;
    downloadLink.download = "news-data.xlsx";
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  }
  function handleDownloadExcel() {
    try {
        
      axios.get(`${apiBaseUrl}/news/news-article/`).then((response) => {
        if(response.data){
          // console.log(response.data);
          exportNewsDataToExcel(response.data);

        }
      });
      
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
                className="nav-link"
                aria-current="page"
              >
                All news
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/selectChartType">Visualize</Link>
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
