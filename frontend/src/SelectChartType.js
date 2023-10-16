import React, { useState } from "react";
import { Button, Form, Container, Row, Col } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";

function ChartGenerator() {
  const [chartType, setChartType] = useState("bar");
  const [generateChart, setGenerateChart] = useState(false);
  const navigate = useNavigate()

  const handleGenerateChart = () => {
    setGenerateChart(true);
  };

  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        <Col md={6} className="bg-light p-4 rounded shadow">
          <h1 className="text-center mb-4">Select Chart Type</h1>
          <Form>
            <Form.Group controlId="chartType">
              <Form.Check
                type="radio"
                label="Bar Chart"
                id="bar"
                checked={chartType === "bar"}
                onChange={() => setChartType("bar")}
              />
              <Form.Check
                type="radio"
                label="Pie Chart"
                id="pie"
                checked={chartType === "pie"}
                onChange={() => setChartType("pie")}
              />
              <Form.Check
                type="radio"
                label="Line Chart"
                id="line"
                checked={chartType === "line"}
                onChange={() => setChartType("line")}
              />
              <Form.Check
                type="radio"
                label="Histogram"
                id="histogram"
                checked={chartType === "histogram"}
                onChange={() => setChartType("histogram")}
              />
            </Form.Group>

            <div className="text-center">
              {/* <Link
                to={{
                  pathname: "/viewChart",
                  state: { chartTypes: chartType },
                }}
              >
              </Link> */}
              <Button
                variant="primary"
                onClick={() => {
                  navigate("/viewChart", {replace:true, state:{chartType}});
                }}
              >
                Generate Chart
              </Button>
            </div>
          </Form>
        </Col>
      </Row>
    </Container>
  );
}

export default ChartGenerator;
