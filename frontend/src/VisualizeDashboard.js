import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./App.css";
import VehicleChart from "./VehicleChart";
import TimeChart from "./TimeChart";
import PlaceChart from "./PlaceChart";

function Dashboard() {
  const radartype = "radar";
  return (
    <Container fluid className="full-height-container" >
      <Row className="full-height-row">
        <Col md={4} className="  custombackground full-height-col border" >
          <VehicleChart type={"bar"}></VehicleChart>
        </Col>
        <Col md={4} className="  custombackground full-height-col border">
        <TimeChart  type= {"line"}></TimeChart>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
          <PlaceChart type={"radar"}></PlaceChart>
        </Col>
      </Row>
      <Row className="full-height-row">
      <Col md={4} className="   custombackground full-height-col border">
          <PlaceChart type={"bar"}></PlaceChart>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
          <VehicleChart type={"radar"}></VehicleChart>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
          <TimeChart  type= {"pie"}></TimeChart>
        </Col>
        
      </Row>
    </Container>
  );
}

export default Dashboard;
