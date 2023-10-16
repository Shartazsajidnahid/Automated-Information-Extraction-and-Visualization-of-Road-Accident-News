import React, { useState } from "react";
import { Bar, Pie } from "react-chartjs-2";

const data = [
  { vehicle_type: "motorcycle", count: 10 },
  { vehicle_type: "bike", count: 4 },
];

const SelectChartType = () => {
  const [chartType, setChartType] = useState("bar");

  const handleChange = (e) => {
    setChartType(e.target.value);
  };

  const renderChart = () => {
    switch (chartType) {
      case "bar":
        return <Bar data={data} />;
      case "pie":
        return <Pie data={data} />;
      default:
        return null;
    }
  };

  return (
    <div>
      <select value={chartType} onChange={handleChange}>
        <option value="bar">Bar Chart</option>
        <option value="pie">Pie Chart</option>
      </select>
      {renderChart()}
    </div>
  );
};

export default SelectChartType;