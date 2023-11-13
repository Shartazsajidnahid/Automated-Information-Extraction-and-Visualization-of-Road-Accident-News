import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const NewsArticleDetails = () => {
  let params = useParams();
  const articleId = params.id;
  const [newsArticle, setNewsArticle] = useState(null);
  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    axios
      .get(`${apiBaseUrl}/news/news-article/${articleId}`)
      .then((response) => {
        setNewsArticle(response.data);
      });
  }, [articleId, apiBaseUrl]);

  if (!newsArticle) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container mt-3">
      <div className="card mb-3">
        <div className="card-body">
          <h3 className="card-title text-center">{newsArticle?.title}</h3>
          <p className="card-text">{newsArticle?.content}</p>
        </div>
      </div>

      <div className="card">
        <div className="card-body">
          <ul className="list-group list-group-flush">
            <li className="list-group-item">
              <strong>Location:</strong> {newsArticle?.parameters.location}
            </li>
            <li className="list-group-item">
              <strong>Division:</strong> {newsArticle?.parameters.division}
            </li>
            <li className="list-group-item">
              <strong>District:</strong> {newsArticle?.parameters.district}
            </li>
            <li className="list-group-item">
              <strong>Subdistrict:</strong> {newsArticle?.parameters.subdistrict}
            </li>
            <li className="list-group-item">
              <strong>Time:</strong> {newsArticle?.parameters.time}
            </li>
            <li className="list-group-item">
              <strong>Day of week:</strong> {newsArticle?.parameters.dayofweek}
            </li>
            <li className="list-group-item">
              <strong>Time of Day:</strong> {newsArticle?.parameters.timeofday}
            </li>
            <li className="list-group-item">
              <strong>Vehicle1:</strong> {newsArticle?.parameters.vehicle1}
            </li>
            <li className="list-group-item">
              <strong>Vehicle2:</strong> {newsArticle?.parameters.vehicle2}
            </li>
            <li className="list-group-item">
              <strong>Dead:</strong> {newsArticle?.parameters.dead}
            </li>
            <li className="list-group-item">
              <strong>Injured:</strong> {newsArticle?.parameters.injured}
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default NewsArticleDetails;
