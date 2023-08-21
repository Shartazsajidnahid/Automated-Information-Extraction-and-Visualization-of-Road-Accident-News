import React, { useState, useEffect } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css"; // Import Bootstrap CSS
import "./App.css"; // Import your own custom CSS (if needed)

function App() {
  const [news, setNews] = useState([]);
  const [newNews, setNewNews] = useState("");

  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    axios.get(`${apiBaseUrl}/news/`).then((response) => {
      setNews(response.data);
    });
  }, [apiBaseUrl]);

  const handleAddNews = () => {
    axios.post(`${apiBaseUrl}/news/`, { news: newNews }).then((response) => {
      setNews([...news, newNews]);
      setNewNews("");
    });
  };

  const truncateText = (text, maxLength) => {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + "...";
    }
    return text;
  };

  return (
    <div className="container">
      <h1 className="mt-4">News Articles</h1>
      <div className="row">
        {news.map((newsItem, index) => (
          <div className="col-md-4 mb-4" key={index}>
            <div className="card">
              <div className="card-body">
                <p className="card-text">{truncateText(newsItem.content, 100)}</p>
                <a href={newsItem.link} >
                  Read More
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
      <div className="mt-4">
        <input
          type="text"
          value={newNews}
          onChange={(e) => setNewNews(e.target.value)}
          className="form-control"
        />
        <button onClick={handleAddNews} className="btn btn-primary mt-2">
          Add News
        </button>
      </div>
    </div>
  );
}

export default App;
