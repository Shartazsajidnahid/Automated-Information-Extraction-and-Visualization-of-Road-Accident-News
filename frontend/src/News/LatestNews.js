import React from "react";
import { Link } from "react-router-dom";

function LatestNews({ latestNews }) {
  const truncateText = (text, maxLength) => {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + "...";
    }
    return text;
  };
  return (
    <div>
      <div className="row custombackground" >
        <h3 className="text-center mt-3 mb-3">Top 5 Latest News</h3>
      </div>
      <hr />
      <div className="row">
        <ul>
          {latestNews.map((newsItem, index) => (
            <div key={index}>
              <div className="card custombackground" >
                <div className="card-body">
                  <h5 className="card-title  ">{newsItem?.title}</h5>
                  <p className="card-text small">
                    {truncateText(newsItem?.content, 100)}
                  </p>
                  <Link
                    to={`/news-article/${newsItem?._id}`}
                    className="btn btn-sm text-white"
                    style={{ backgroundColor: "#2b6777" }}
                  >
                    Read More
                  </Link>
                  {/* <Link to={{ pathname: `/news/${index}`, state: { newsItem: newsItem } }}>Read More</Link> Use Link */}
                </div>
              </div>
              <hr></hr>
            </div>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default LatestNews;
