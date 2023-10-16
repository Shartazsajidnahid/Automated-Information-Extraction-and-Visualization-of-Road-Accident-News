import React, { useEffect, useRef } from "react";
import { useLocation } from "react-router-dom";
import Chart from "chart.js/auto";

function ViewChart(props){
  const location = useLocation();
  // console.log(location.state.chartType)
  // const chartType = location.state.chartType;
  const chartType = location.state.chartType
  const chartRef = useRef(null);
  let myChart = null;

  useEffect(() => {
    if (chartType) {
      const data = [
        { vehicle_type: "motorcycle", count: 10 },
        { vehicle_type: "bike", count: 4 },
      ];

      const labels = data.map((item) => item.vehicle_type);
      const counts = data.map((item) => item.count);

      const ctx = chartRef.current.getContext("2d");

      // Destroy the previous chart, if it exists
      if (myChart) {
        myChart.destroy();
      }

      myChart = new Chart(ctx, {
        type: chartType,
        data: {
          labels: labels,
          datasets: [
            {
              label: "Vehicle Counts",
              data: counts,
              backgroundColor: [
                "rgba(75, 192, 192, 0.2)",
                "rgba(255, 99, 132, 0.2)",
              ],
              borderColor: ["rgba(75, 192, 192, 1)", "rgba(255, 99, 132, 1)"],
              borderWidth: 1,
            },
          ],
        },
        options: {
          maintainAspectRatio: false, // Disable aspect ratio
          responsive: false, // Disable responsiveness
        },
      });
    }
  }, [chartType]);

  return (
    <div>
      <h1>View Chart</h1>
      <canvas ref={chartRef} width="1000" height="500"></canvas>
    </div>
  );
}

export default ViewChart;
