import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import LatestNews from "./LatestNews";

function Allnews() {
  const [news, setNews] = useState([]);
  const [latestNews, setLatestNews] = useState([]);

  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    // Fetch all news
    axios.get(`${apiBaseUrl}/news/news-article/`).then((response) => {
      setNews(response.data);
    });

    // Fetch the top 5 latest news
    axios.get(`${apiBaseUrl}/news/latest-news/`).then((response) => {
      setLatestNews(response.data);
    });
  }, [apiBaseUrl]);

  const truncateText = (text, maxLength) => {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + "...";
    }
    return text;
  };

  const keywords = [
    "Technology",
    "Sports",
    "Politics",
    "Entertainment",
    "Science",
  ];

  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col-md-2 mt-4 text-center">
          <h3 mt-4 text-center>Keywords</h3>
          <hr />
          <ul className="list-group">
            {keywords.map((keyword) => (
              <li key={keyword} className="list-group-item">
                <span>{keyword}</span>
              </li>
            ))}
          </ul>
        </div>
        <div className="col-md-7 border-start">
          <h3 className="mt-4 text-center">News Articles</h3>
          <hr />
          <div className="row">
            {news.map((newsItem, index) => (
              <div className="col-md-4 mb-4" key={index}>
                <div className="card">
                  <div className="card-body">
                    <h5 className="card-title">
                      <>{newsItem?.title}</>
                    </h5>
                    <p className="card-text">
                      {truncateText(newsItem?.content, 100)}
                    </p>
                    <Link
                      to={`/news-article/${newsItem?._id}`}
                      className="btn btn-sm btn-secondary"
                    >
                      Read More
                    </Link>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
        <div className="col-md-3 border-start">
          <LatestNews latestNews={latestNews} />
        </div>
      </div>
    </div>
  );
}

export default Allnews;
