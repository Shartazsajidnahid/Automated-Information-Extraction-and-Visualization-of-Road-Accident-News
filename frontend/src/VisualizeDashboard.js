import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./App.css";
import VehicleChart from "./VehicleChart";
import TimeChart from "./TimeChart";
import PlaceChart from "./PlaceChart";

function Dashboard() {
  return (
    <Container fluid className="full-height-container" >
      <Row className="full-height-row">
        <Col md={4} className="  custombackground full-height-col border" >
          <VehicleChart></VehicleChart>
        </Col>
        <Col md={4} className="  custombackground full-height-col border">
          <TimeChart></TimeChart>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
          <PlaceChart></PlaceChart>
        </Col>
      </Row>
      <Row className="full-height-row">
      <Col md={4} className="   custombackground full-height-col border">
          <PlaceChart></PlaceChart>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
          <VehicleChart></VehicleChart>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
          <TimeChart></TimeChart>
        </Col>
        
      </Row>
    </Container>
  );
}

export default Dashboard;
