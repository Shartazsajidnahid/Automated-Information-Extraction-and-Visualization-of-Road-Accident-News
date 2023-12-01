import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./App.css";
import VehicleChart from "./VehicleChart";
import TimeChart from "./TimeChart";

function Dashboard() {
  return (
    <Container  className="">
      <Row className="full-height-row">
        <Col md={6} className="p-4 rounded shadow custombackground full-height-col">
          <VehicleChart></VehicleChart>
        </Col>
        <Col md={6} className="p-4 rounded shadow custombackground full-height-col">
          <TimeChart></TimeChart>
        </Col>
        
      </Row>
      <Row className="full-height-row">
        <Col md={6} className="p-4 rounded shadow custombackground full-height-col">
          <VehicleChart></VehicleChart>
        </Col>
        <Col md={6} className="p-4 rounded shadow custombackground full-height-col">
          <TimeChart></TimeChart>
        </Col>
        
      </Row>
    </Container>
  );
}

export default Dashboard;
