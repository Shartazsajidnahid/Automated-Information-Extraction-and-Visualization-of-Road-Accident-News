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
      <h3 className="text-center mt-4">Top 5 Latest News</h3>
      <hr></hr>
      <ul>
        {latestNews.map((newsItem) => (
          <div className="card ">
            <div className="card-body">
              <h5 className="card-title text-white bg-dark">
                {newsItem?.title}
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
              {/* <Link to={{ pathname: `/news/${index}`, state: { newsItem: newsItem } }}>Read More</Link> Use Link */}
            </div>
          </div>
        ))}
      </ul>
    </div>
  );
}

export default LatestNews;
