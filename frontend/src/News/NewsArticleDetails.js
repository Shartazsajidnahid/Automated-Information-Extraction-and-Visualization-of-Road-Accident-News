import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const NewsArticleDetails = () => {
  let params = useParams();
  // console.log(params)
  const articleId = params.id;
  // console.log(articleId)
  const [newsArticle, setNewsArticle] = useState(null);
  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    axios
      .get(`${apiBaseUrl}/news/news-article/${articleId}`)
      .then((response) => {
        setNewsArticle(response.data);
      });
    // setNewsArticle(n1);
  }, [articleId, apiBaseUrl]);

  if (!newsArticle) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <div className="navbar">
        <div className="navbar-brand">News Articles</div>
      </div>

      <div className="container">
        <div className="card mb-3">
          <div className="card-body">
            <h5 className="card-title">{newsArticle?.news.title}</h5>
            <p className="card-text">{newsArticle?.news.content}</p>
          </div>
        </div>

        <div className="card">
          <div className="card-body">
            <ul>
              <li>
                <strong>Location:</strong> {newsArticle?.location}
              </li>
              <li>
                <strong>Time:</strong> {newsArticle?.time}
              </li>
              <li>
                <strong>Vehicle:</strong> {newsArticle?.vehicle}
              </li>
              <li>
                <strong>Dead:</strong> {newsArticle?.dead}
              </li>
              <li>
                <strong>Injured:</strong> {newsArticle?.injured}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </>
  );
};

export default NewsArticleDetails;
