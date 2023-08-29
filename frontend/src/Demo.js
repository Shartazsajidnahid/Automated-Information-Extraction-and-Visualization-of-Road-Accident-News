

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

  return (
    <div>
      {news}
    </div>
  );
}

export default Demo;
