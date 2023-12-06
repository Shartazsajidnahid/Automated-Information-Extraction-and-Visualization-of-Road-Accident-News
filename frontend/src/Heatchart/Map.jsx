import React, { useEffect, useRef, useState} from "react";
import axios from "axios";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet.heat";
import { addressPoints } from "./addressPoints";

export default function Map() {
  const mapRef = useRef(null);
  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
  const [districtlocations, setdistrictLocations] = useState([]); 
  const occurrence_type = "occurrence";


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`${apiBaseUrl}/graphchart/get-heatmap-data?occurrence_type=${occurrence_type}`);
        setdistrictLocations(response.data);
        console.log("Data fetched successfully:", response.data);
  
        if (!mapRef.current) {
          const map = L.map("map").setView([23.8103, 90.4125], 8);
  
          L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          }).addTo(map);
  
          L.heatLayer(response.data).addTo(map);
  
          mapRef.current = map;
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
  
    fetchData();
  }, []);
  

  return <div id="map" style={{ height: "100vh" }}></div>;
}
