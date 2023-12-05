import React from "react";
import { Link } from "react-router-dom";

import { Container, Row, Col } from "react-bootstrap";
import "./App.css";
import VehicleChart from "./VehicleChart";
import TimeChart from "./TimeChart";
import PlaceChart from "./PlaceChart";
import Heatchart from "./Heatchart/Heatchart"
import Heatmap from "./Heatmap"

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
          <Link to="/heatmap"><Heatmap height="400px" width="400px" ></Heatmap></Link>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
        <Link to="/heat"><Heatchart height="400px" width="400px" ></Heatchart></Link>

        </Col>
        
      </Row>
    </Container>
  );
}

export default Dashboard;
