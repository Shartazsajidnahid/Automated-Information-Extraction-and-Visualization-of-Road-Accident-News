import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { Form, Container, Row, Col } from "react-bootstrap";
// import { useNavigate } from "react-router-dom";
import Chart from "chart.js/auto";
import "../App.css"

function VehileChart({type}) {
  const [chartType, setChartType] = useState(type);
  const [dataOption, setDataOption] = useState("vehicles");
  const [vehicledata, setVehicledata] = useState([]);
  // const navigate = useNavigate();
  const chartRef = useRef(null);
  const chartDataRef = useRef(null);
  const myChartRef = useRef(null);
  const table_name = "vehicle_info";
  const occurrence_type = "occurrence";
const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;


  const dataOptions = {
    vehicles: { data: vehicledata, label: "Vehicle Occurrence", key: "typename" },
  };

  useEffect(() => {
    // console.log("yes yes ");
    // console.log(vehicledata);
    // updateChart(chartType ,dataOption);
    updateChartAsync();
  }, [vehicledata])

  useEffect(() => {
    // Fetch vehicledata
    const fetchData = async () => {
      try {
        const response = await axios.get(`${apiBaseUrl}/graphchart/get-data?table_name=${table_name}`);
        console.log(response.data);
        setVehicledata(["{typename: 'মোটরসাইকেল', count: 5}"],...response.data);
        console.log(vehicledata);
    
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    if(vehicledata.length <= 0){
      fetchData();
      // updateChart(chartType, dataOption);
    }
  }, [apiBaseUrl, table_name]);
  
  const fetchData = async () => {
    await axios
      .get(`${apiBaseUrl}/graphchart/get-data?table_name=${table_name}`)
      .then((response) => {
        setVehicledata(response.data);
        // console.log(vehicledata);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(() => {
    fetchData();
  }, []);
  const updateChartAsync = async () => {
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
    }
    updateChart(chartType, dataOption)
  };

  useEffect(() => {
    
    updateChartAsync();
  }, [chartType, dataOption, vehicledata]);
  
  const updateChart = (selectedChartType, selectedDataOption) => {
    
    const selectedData = dataOptions[selectedDataOption].data;
    const labelKey = dataOptions[selectedDataOption].key;
    console.log("update: ");
    const labels = selectedData.map((item) => item[labelKey]);
    const counts = selectedData.map((item) => item.count);
    console.log(labels);
    console.log(counts);
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