import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function Allnews() {
  const [news, setNews] = useState([]);

  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    axios.get(`${apiBaseUrl}/news/dummy_news/`).then((response) => {
      setNews(response.data);
    });
  }, [apiBaseUrl]);


  const truncateText = (text, maxLength) => {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + "...";
    }
    return text;
  };
  return (
    <div>
      <h1 className="mt-4">News Articles</h1>
      
      <div className="row">
        {news.map((newsItem, index) => (
          <div className="col-md-4 mb-4" key={index}>
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{newsItem?.headline}</h5>
                <p className="card-text">
                  {truncateText(newsItem?.content, 100)}
                </p>
                <Link to={`/news-article/${newsItem?.id}`}>Read More</Link>
                {/* <Link to={{ pathname: `/news/${index}`, state: { newsItem: newsItem } }}>Read More</Link> Use Link */}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Allnews;
