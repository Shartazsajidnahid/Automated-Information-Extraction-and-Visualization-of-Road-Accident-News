import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import "../App.css";

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
        <div className="card-body  custombackground">
          <h3 className="card-title text-center mt-1">{newsArticle?.title}</h3>
          <hr></hr>
          <p className="card-text">{newsArticle?.content}</p>
        </div>
      </div>

      {/* <div className="card">
        <div className="card-body">
          <ul className="list-group list-group-flush">
            <li
              className="list-group-item custombackground rounded"
              style={{ backgroundColor: "#edf2f4" }}
            >
              <strong>Location:</strong> {newsArticle?.parameters.location}
            </li>
            <li className="list-group-item custombackground">
              <strong>Division:</strong> {newsArticle?.parameters.division}
            </li>
            <li className="list-group-item custombackground">
              <strong>District:</strong> {newsArticle?.parameters.district}
            </li>
            <li className="list-group-item custombackground">
              <strong>Subdistrict:</strong>{" "}
              {newsArticle?.parameters.subdistrict}
            </li>
            <li className="list-group-item custombackground">
              <strong>Time:</strong> {newsArticle?.parameters.time}
            </li>
            <li className="list-group-item custombackground">
              <strong>Day of week:</strong> {newsArticle?.parameters.dayofweek}
            </li>
            <li className="list-group-item custombackground">
              <strong>Time of Day:</strong> {newsArticle?.parameters.timeofday}
            </li>
            <li className="list-group-item custombackground">
              <strong>Vehicle1:</strong> {newsArticle?.parameters.vehicle1}
            </li>
            <li className="list-group-item custombackground">
              <strong>Vehicle2:</strong> {newsArticle?.parameters.vehicle2}
            </li>
            <li className="list-group-item custombackground">
              <strong>Dead:</strong> {newsArticle?.parameters.dead}
            </li>
            <li className="list-group-item custombackground">
              <strong>Injured:</strong> {newsArticle?.parameters.injured}
            </li>
          </ul>
        </div>
      </div> */}
      <div className="card">
        <div className="card-body ">
          <table className="table table-bordered">
            <tbody >
              <tr >
                <td >
                  <strong>Location:</strong>
                </td>
                <td>{newsArticle?.parameters.location}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Division:</strong>
                </td>
                <td>{newsArticle?.parameters.division}</td>
              </tr>
              {/* Add similar rows for other parameters */}
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>District:</strong>
                </td>
                <td>{newsArticle?.parameters.district}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Subdistrict:</strong>
                </td>
                <td>{newsArticle?.parameters.subdistrict}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Time:</strong>
                </td>
                <td>{newsArticle?.parameters.time}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Day of week:</strong>
                </td>
                <td>{newsArticle?.parameters.dayofweek}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Time of Day:</strong>
                </td>
                <td>{newsArticle?.parameters.timeofday}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Vehicle1:</strong>
                </td>
                <td>{newsArticle?.parameters.vehicle1}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Vehicle2:</strong>
                </td>
                <td>{newsArticle?.parameters.vehicle2}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Dead:</strong>
                </td>
                <td>{newsArticle?.parameters.dead}</td>
              </tr>
              <tr>
                <td style={{ width: '15%' }}>
                  <strong>Injured:</strong>
                </td>
                <td>{newsArticle?.parameters.injured}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default NewsArticleDetails;
