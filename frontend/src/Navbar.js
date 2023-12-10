import { Link } from "react-router-dom";
import axios from "axios";
import React from "react";
import ExcelJS from "exceljs";


function Navbar() {
  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

  async function exportNewsDataToExcel(newsData) {
    
    const workbook = new ExcelJS.Workbook();
  
    const worksheet = workbook.addWorksheet("News Data");
  
    worksheet.columns = [

      { header: "Content" },
      { header: "Accident Location" },
      { header: "Accident Time" },
      { header: "No of Dead from News" },
      { header: "No of Injured from News" }

    ];
  
    newsData.forEach((newsItem) => {
      const row = worksheet.addRow();
      // Set the cell values for each column in the worksheet
      row.getCell(1).value = newsItem.content;
      row.getCell(2).value = newsItem.parameters.location;
      row.getCell(3).value = newsItem.parameters.time;
      row.getCell(4).value = newsItem.parameters.dead;
      row.getCell(5).value = newsItem.parameters.injured;
    });
  
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
              <Link className="nav-link" to="/visualizeDashboard">Visualize</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/heatmap">Heatmap</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/heat">Heatchart</Link>
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

          {/* <form className="d-flex">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            ></input>
            <button className="btn btn-outline-success" type="submit">
              Search
            </button>
          </form> */}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
