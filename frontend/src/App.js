import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"; // Import Router and related components
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Allnews from "./News/Allnews";
import NewsArticleDetails from "./News/NewsArticleDetails";
import Demo from "./Demo";


// import Newsdetail from "./News/Newsdetail";


function App() {
  return (
    // <Demo></Demo>
    <Router>
      <div className="container">
        <Routes>
          <Route path="/allnews" element={<Allnews />} />
          <Route path="/" element={<Allnews />} />
          <Route path="/news-article/:id" element={<NewsArticleDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
