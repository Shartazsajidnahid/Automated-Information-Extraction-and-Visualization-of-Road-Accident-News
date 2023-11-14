// Allnews.js
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import LatestNews from "./LatestNews";
import Leftbar from "./Leftbar";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import {
  division_districts,
  bangla_days,
  vehicle_types,
} from "../Data/FilterData";

function Allnews() {
  const [news, setNews] = useState([]);
  const [latestNews, setLatestNews] = useState([]);
  const [filters, setFilters] = useState({
    division: "",
    district: "",
    timeOfDay: "",
    dayOfWeek: "",
    vehicle: "",
  });
  const [filtersOpen, setFiltersOpen] = useState(false);

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

  const handleDivisionChange = (event) => {
    // Reset district when division changes
    setFilters({ ...filters, division: event.target.value, district: "" });
  };

  const handleSearch = () => {
    const filteredNews = news.filter((newsItem) => {
      const parameters = newsItem.parameters;

      return (
        (!filters.division || parameters.division === filters.division) &&
        (!filters.district || parameters.district === filters.district) &&
        (!filters.timeOfDay || parameters.timeofday === filters.timeOfDay) &&
        (!filters.dayOfWeek || parameters.dayofweek === filters.dayOfWeek) &&
        (!filters.vehicle ||
          parameters.vehicle1 === filters.vehicle ||
          parameters.vehicle2 === filters.vehicle)
      );
    });

    setNews(filteredNews);
  };

  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col-md-2 mt-4 text-center">
          <Leftbar></Leftbar>
        </div>
        <div className="col-md-7 border-start">
          <div className="card mb-4">
            <div className="card-header">
              <div className="row">
                <div className="col-md-2">
                  <h5 className="mb-0 mt-3 text-center">
                    <button
                      className="btn btn-outline-success"
                      onClick={() => setFiltersOpen(!filtersOpen)}
                    >
                      Filters &nbsp;
                      <i class="fa-solid fa-caret-down"></i>
                    </button>
                  </h5>
                </div>
                <div className="col-md-8">
                  <h3 className="mt-3 text-center">News Articles</h3>
                </div>
                <div className="col-md-2"></div>
              </div>
            </div>
            {filtersOpen && (
              <div className="card-body">
                <div className="filter-bar row g-3">
                  <div className="col-md-4 form-group d-flex align-items-center">
                    <label
                      htmlFor="division"
                      className="form-label me-2 fw-bold text-secondary small"
                    >
                      Division:
                    </label>
                    <select
                      id="division"
                      name="division"
                      className="form-select-sm"
                      value={filters.division}
                      onChange={handleDivisionChange}
                    >
                      <option value="">
                        <small>Select Division</small>
                      </option>
                      {Object.keys(division_districts).map((division) => (
                        <option
                          key={division}
                          value={division}
                          className="small"
                        >
                          {division}
                        </option>
                      ))}
                    </select>
                  </div>

                  <div className="col-md-4 form-group d-flex align-items-center">
                    <label
                      htmlFor="district"
                      className="form-label me-2  fw-bold text-secondary small"
                    >
                      District:
                    </label>
                    <select
                      id="district"
                      name="district"
                      className="form-select-sm"
                      value={filters.district}
                      onChange={(event) =>
                        setFilters({ ...filters, district: event.target.value })
                      }
                    >
                      <option value="">Select District</option>
                      {filters.division &&
                        division_districts[filters.division].map((district) => (
                          <option key={district} value={district}>
                            {district}
                          </option>
                        ))}
                    </select>
                  </div>

                  <div className="col-md-4 form-group d-flex align-items-center">
                    <label
                      htmlFor="vehicle"
                      className="form-label me-2 fw-bold text-secondary small"
                    >
                      Vehicle:
                    </label>
                    <select
                      id="vehicle"
                      name="vehicle"
                      className="form-select-sm"
                      value={filters.vehicle}
                      onChange={(event) =>
                        setFilters({ ...filters, vehicle: event.target.value })
                      }
                    >
                      <option value="">Select Vehicle</option>
                      {vehicle_types.map((vehicle) => (
                        <option key={vehicle} value={vehicle}>
                          {vehicle}
                        </option>
                      ))}
                    </select>
                  </div>

                  <div className="col-md-4 form-group d-flex align-items-center">
                    <label
                      htmlFor="timeOfDay"
                      className="form-label me-2 fw-bold text-secondary small"
                    >
                      Time of Day:
                    </label>
                    <select
                      id="timeOfDay"
                      name="timeOfDay"
                      className="form-select-sm"
                      value={filters.timeOfDay}
                      onChange={(event) =>
                        setFilters({
                          ...filters,
                          timeOfDay: event.target.value,
                        })
                      }
                    >
                      <option value="">Select Time of Day</option>
                      <option value="দিন">দিন</option>
                      <option value="রাত">রাত</option>
                    </select>
                  </div>

                  <div className="col-md-4 form-group d-flex align-items-center">
                    <label
                      htmlFor="dayOfWeek"
                      className="form-label me-2 fw-bold text-secondary small"
                    >
                      Day of Week:
                    </label>
                    <select
                      id="dayOfWeek"
                      name="dayOfWeek"
                      className="form-select-sm"
                      value={filters.dayOfWeek}
                      onChange={(event) =>
                        setFilters({
                          ...filters,
                          dayOfWeek: event.target.value,
                        })
                      }
                    >
                      <option value="">Select Day of Week</option>
                      {bangla_days.map((day) => (
                        <option key={day} value={day}>
                          {day}
                        </option>
                      ))}
                    </select>
                  </div>

                  <div className="col-md-4 form-group d-flex align-items-center justify-content-center">
                    <button
                      onClick={handleSearch}
                      className="btn btn-sm btn-success"
                    >
                      Search
                    </button>
                  </div>
                </div>
              </div>
            )}
          </div>
          <hr />
          <div className="row">
            {news.map((newsItem, index) => (
              <div className="col-md-4 mb-4" key={index}>
                <div className="card bg-light p-4 rounded shadow">
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
