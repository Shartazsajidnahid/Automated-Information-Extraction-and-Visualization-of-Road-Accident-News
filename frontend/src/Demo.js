import React, { useState, useEffect } from "react";
import axios from "axios";

function Demo() {
  const [news, setNews] = useState([]); // Changed the initial state to an empty array

  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    axios.get(`${apiBaseUrl}/demo/bnltk/`).then((response) => {
      setNews(response.data);
    });
  }, [apiBaseUrl]);

  function handleDownloadExcel() {
    try {
      console.log("here i am");
        
      axios.get(`${apiBaseUrl}/news/scrape_news/`).then((response) => {
        if(response.data){
        }
      });
      
    } catch (error) {
      console.error("Error updating database:", error);
    }
  }

  return (
    <div>
      {news}
      <button
        className="btn btn-lg btn-success me-2"
        aria-current="page"
        onClick={handleDownloadExcel}
      >Updata Database</button>
    </div>
  );
}

export default Demo;
