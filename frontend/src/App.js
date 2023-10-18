import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"; // Import Router and related components
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Allnews from "./News/Allnews";
import NewsArticleDetails from "./News/NewsArticleDetails";
import Demo from "./Demo";
import Navbar from "./Navbar";
import SelectChartType from "./SelectChartType";
import ViewChart from "./ViewChart";

// import Newsdetail from "./News/Newsdetail";

function App() {
  return (
    // <Demo></Demo>
    <>
      <Router>
        <Navbar></Navbar>
        <div>
          <Routes>
            <Route path="/allnews" element={<Allnews />} />
            <Route path="/" element={<Allnews />} />
            <Route path="/news-article/:id" element={<NewsArticleDetails />} />

            <Route path="/selectChartType" element={<SelectChartType />} />
            <Route path="/viewChart" element={<ViewChart />} />


          </Routes>
        </div>
      </Router>
    </>
  );
}

export default App;
