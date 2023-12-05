import React, { useEffect, useRef } from "react";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet.heat";
import { addressPoints } from "./addressPoints";

export default function Map() {
  const mapRef = useRef(null);

  useEffect(() => {
    // Check if the map is already initialized
    if (!mapRef.current) {
      // Create a new map instance
      const map = L.map("map").setView([23.8103, 90.4125], 8);

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);

      // Use the addressPoints array directly, which includes intensity values
      L.heatLayer(addressPoints).addTo(map);

      // Set the map instance to the ref
      mapRef.current = map;
    }
  }, []);

  return <div id="map" style={{ height: "100vh" }}></div>;
}
