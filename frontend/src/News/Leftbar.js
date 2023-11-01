import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import { Button} from "react-bootstrap";


function Leftbar() {
  const [news, setNews] = useState([]);
  const [latestNews, setLatestNews] = useState([]);
  const navigate = useNavigate()

  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;

//   useEffect(() => {
//     // Fetch all news
//     axios.get(`${apiBaseUrl}/news/news-article/`).then((response) => {
//       setNews(response.data);
//     });

//     // Fetch the top 5 latest news
//     axios.get(`${apiBaseUrl}/news/latest-news/`).then((response) => {
//       setLatestNews(response.data);
//     });
//   }, [apiBaseUrl]);


  const keywords = [
    "ঢাকা",
    "চট্টগ্রাম",
    "রাজশাহী",
    "খুলনা",
    "বরিশাল",
    "সিলেট",
    "ময়মনসিংহ",
    "রংপুর",
  ];
  const division = "division"

  return (
    <>
      <h3 mt-4 text-center>
        Divisions
      </h3>
      <hr />
      <ul className="list-group">
        {keywords.map((keyword) => (
          // <Link
          //   className="list-group-item"
          //   style={{ cursor: "pointer" }}
          //   key={keyword}
          //   to="/searchednews"
          // >
          //   <span>{keyword}</span>
          // </Link>
          <Button
          className="list-group-item"
          onClick={() => {
            navigate("/searchednews", {replace:true, state:{keyword,division}});
          }}
        >
          <span>{keyword}</span>
        </Button>
        ))}
      </ul>
    </>
  );
}

export default Leftbar;
