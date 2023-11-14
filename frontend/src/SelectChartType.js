import React, { useState, useEffect, useRef } from "react";
import { Form, Container, Row, Col } from "react-bootstrap";
// import { useNavigate } from "react-router-dom";
import Chart from "chart.js/auto";

function ChartPage() {
  const [chartType, setChartType] = useState("bar");
  const [dataOption, setDataOption] = useState("vehicles");
  // const navigate = useNavigate();
  const chartRef = useRef(null);
  const chartDataRef = useRef(null);
  const myChartRef = useRef(null);

  const vehicleData = [
    { vehicle_type: "মোটরসাইকেল", count: 10 },
    { vehicle_type: "বাইক", count: 4 },
    { vehicle_type: "ভ্যান", count: 8 },
    { vehicle_type: "গাড়ি", count: 20 },
    { vehicle_type: "বাস", count: 5 }
];


  const placeData = [
    { place: "ঢাকা", count: 12 },
    { place: "বান্দরবান", count: 34 },
    { place: "ময়মনসিংহ", count: 8 },
    { place: "কক্সবাজার", count: 15 },
    { place: "সিলেট", count: 22 }
];

  // Create a mapping of data options to their respective data and label
  const dataOptions = {
    vehicles: { data: vehicleData, label: "Vehicle Occurrence", key: "vehicle_type" },
    places: { data: placeData, label: "Place Occurrences", key: "place" },
  };

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
          responsive: false,
        },
      });

      updateChart(chartType, dataOption);
    }
  }, [chartType, dataOption]);

  const updateChart = (selectedChartType, selectedDataOption) => {
    const selectedData = dataOptions[selectedDataOption].data;
    const labelKey = dataOptions[selectedDataOption].key;

    const labels = selectedData.map((item) => item[labelKey]);
    const counts = selectedData.map((item) => item.count);

    chartDataRef.current = {
      labels: labels,
      datasets: [
        {
          label: dataOptions[selectedDataOption].label,
          data: counts,
          borderWidth: 1,
        },
      ],
    };

    myChartRef.current.config.type = selectedChartType; // Update the chart type
    myChartRef.current.update();
  };

  return (
    <Container className="mt-3">
      <Row className="justify-content-center">
        <Col md={6} className="bg-light p-4 rounded shadow">
          <h2 className="text-center mb-4">Customize</h2>
          <Form>
            <Row>
              <Col md={6}>
                <Form.Group controlId="chartType">
                  <Form.Label><b>Chart Type</b></Form.Label>
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
              <Col md={6}>
                <Form.Group controlId="dataOption">
                  <Form.Label><b>Data Option</b></Form.Label>
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
                  </Form.Control>
                </Form.Group>
              </Col>
            </Row>
          </Form>
        </Col>
      </Row>
      <Row className="justify-content-center mt-4">
        <Col md={8}>
          <canvas ref={chartRef} width="1000" height="500"></canvas>
        </Col>
      </Row>
    </Container>
  );
}

export default ChartPage;
