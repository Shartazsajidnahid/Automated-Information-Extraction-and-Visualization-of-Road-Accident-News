import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./App.css";
import VehicleChart from "./VehicleChart";
import TimeChart from "./TimeChart";
import PlaceChart from "./PlaceChart";

function Dashboard() {
  return (
    <Container fluid className="full-height-container">
      <Row className="full-height-row">
        <Col md={4} className="p-4 rounded shadow custombackground full-height-col">
          <VehicleChart></VehicleChart>
        </Col>
        <Col md={4} className="p-4 rounded shadow custombackground full-height-col">
          <TimeChart></TimeChart>
        </Col>
        <Col md={4} className="p-4 rounded shadow custombackground full-height-col">
          <PlaceChart></PlaceChart>
        </Col>
      </Row>
      <Row className="full-height-row">
      <Col md={4} className="p-4 rounded shadow custombackground full-height-col">
          <PlaceChart></PlaceChart>
        </Col>
        <Col md={4} className="p-4 rounded shadow custombackground full-height-col">
          <VehicleChart></VehicleChart>
        </Col>
        <Col md={4} className="p-4 rounded shadow custombackground full-height-col">
          <TimeChart></TimeChart>
        </Col>
        
      </Row>
    </Container>
  );
}

export default Dashboard;
