import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { Form, Container, Row, Col } from "react-bootstrap";
// import { useNavigate } from "react-router-dom";
import Chart from "chart.js/auto";
import "./App.css"

function VehileChart() {
  const [chartType, setChartType] = useState("bar");
  const [dataOption, setDataOption] = useState("vehicles");
  const [vehicleData, setvehicleData] = useState([]);
  // const navigate = useNavigate();
  const chartRef = useRef(null);
  const chartDataRef = useRef(null);
  const myChartRef = useRef(null);
  const table_name = "vehicle_info";
  const occurrence_type = "occurrence";


const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;


  const placeData = [
    { typename: "ঢাকা", count: 12 },
    { typename: "বান্দরবান", count: 34 },
    { typename: "ময়মনসিংহ", count: 8 },
    { typename: "কক্সবাজার", count: 15 },
    { typename: "সিলেট", count: 22 }
];

  const dayOfWeekData = [
    { typename: "রবিবার", count: 9 },
    { typename: "সোমবার", count: 8 },
    { typename: "মঙ্গলবার", count: 5 },
    { typename: "বুধবার", count: 7 },
    { typename: "বৃহস্পতিবার", count: 12 },
    { typename: "শুক্রবার", count: 3 },
    { typename: "শনিবার", count: 10 }
    
  ];

  const timeofDayData = [
    { typename: "দিন", count: 4 },
    { typename: "রাত", count: 11 },
  ];

  const dataOptions = {
    vehicles: { data: vehicleData, label: "Vehicle Occurrence", key: "typename" },
    places: { data: placeData, label: "Place Occurrences", key: "typename" },
    dayofweek: { data: dayOfWeekData, label: "Occurrences", key: "typename" },
    timeofday: { data: timeofDayData, label: "Occurrences", key: "typename" },
  };

  useEffect(() => {
    // Fetch vehicleData
    axios.get(`${apiBaseUrl}/graphchart/get-data/${table_name}/${occurrence_type}`)
      .then((response) => {
        setvehicleData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [apiBaseUrl, table_name, occurrence_type]);
  
  useEffect(() => {
    if (chartRef.current) {
      if (myChartRef.current) {
        myChartRef.current.destroy();
      }
      myChartRef.current = new Chart(chartRef.current, {
        type: chartType,
        data: chartDataRef.current,
        options: {
          maintainAspectRatio: false,
          responsive: true,
        },
      });
      updateChart(chartType, dataOption);
    }
  }, [chartType, dataOption, vehicleData]);
  
  const updateChart = (selectedChartType, selectedDataOption) => {
    const selectedData = dataOptions[selectedDataOption].data;
    const labelKey = dataOptions[selectedDataOption].key;

    const labels = selectedData.map((item) => item[labelKey]);
    const counts = selectedData.map((item) => item.count);

    let backgroundColors, border;

    if (selectedChartType === "pie") {
      // For Pie chart, let Chart.js use its default colors
      backgroundColors = undefined;
    } else {
      // For other chart types (e.g., bar, line), use your specified colors
      const colors = [
        "rgba(117, 14, 33, 0.8)", // Dark Red
        // 'rgba(0, 100, 0, 0.7)', // Dark Green
        // 'rgba(0, 0, 139, 0.7)', // Dark Blue
      ];

      backgroundColors = counts.map((count, index) => {
        const colorIndex = index % colors.length;
        return colors[colorIndex];
      });
    }

    if (selectedChartType === "line") {
        // For Pie chart, let Chart.js use its default colors
        border = 3;
    } else{
        border = undefined;
    }
  
    chartDataRef.current = {
      labels: labels,
      datasets: [
        {
          label: dataOptions[selectedDataOption].label,
          data: counts,
          borderWidth: border,
          backgroundColor: backgroundColors,
          borderJoinStyle: 'miter'
        },
      ],
    };

    myChartRef.current.config.type = selectedChartType;
    myChartRef.current.update();
  };

  return (
    <Container>
      <Row className="justify-content-center">
        <Col md={12} className=" p-2 rounded shadow custombackground">
          <Form>
            <Row>
              <Col md={4}>
              <h2 className="text-center ">Vehicle</h2>
              </Col>
              <Col md={4}>
                <Form.Group controlId="chartType">
                  <Form.Control
                    as="select"
                    value={chartType}
                    onChange={(e) => {
                      const selectedChartType = e.target.value;
                      setChartType(selectedChartType);
                      updateChart(selectedChartType, dataOption);
                    }}
                  >
                    <option value="bar">Bar Chart</option>
                    <option value="pie">Pie Chart</option>
                    <option value="line">Line Chart</option>
                    <option value="radar">Radar Chart</option>
                  </Form.Control>
                </Form.Group>
              </Col>
              <Col md={4}>
                <Form.Group controlId="dataOption">
                  <Form.Control
                    as="select"
                    value={dataOption}
                    onChange={(e) => {
                      const selectedDataOption = e.target.value;
                      setDataOption(selectedDataOption);
                      updateChart(chartType, selectedDataOption);
                    }}
                  >
                    <option value="vehicles">Vehicles</option>
                    <option value="places">Places</option>
                    <option value="dayofweek">Weekdays</option>
                    <option value="timeofday">Time of Day</option>
                  </Form.Control>
                </Form.Group>
              </Col>
            </Row>
          </Form>
        </Col>
      </Row>
      <Row className="justify-content-center mt-4">
        <Col md={12}>
        <canvas ref={chartRef} style={{ width: '100%', height: '100%' }}></canvas>
        </Col>
      </Row>
    </Container>
  );
}

export default VehileChart;
