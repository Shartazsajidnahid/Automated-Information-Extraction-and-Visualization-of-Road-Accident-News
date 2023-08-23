import React from "react";
// import { useParams } from "react-router-dom"; // Import useParams

const NewsDetail = ({ newsitem }) => {
//   const { id } = useParams(); // Get the id from the dynamic route parameter
  console.log("nahid");
  console.log(newsitem?.content);

  return (
    <div className="container">
      <h2>News Details</h2>
      <p>{newsitem?.content}</p>
      {/* <a href={selectedNews.link} target="_blank" rel="noopener noreferrer">
        Read Full Article
      </a> */}
    </div>
  );
};

export default NewsDetail;
