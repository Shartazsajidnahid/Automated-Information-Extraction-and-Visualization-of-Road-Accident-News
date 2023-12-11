import React from "react";
import { Link } from "react-router-dom";

import { Container, Row, Col } from "react-bootstrap";
import "./App.css";
import PlaceChart from "./Charts/PlaceChart";
import VehicleChart from "./Charts/VehicleChart"
import TimeChart from "./Charts/TimeChart";
import DowChart from "./Charts/DowChart"
import Heatchart from "./Heatchart/Heatchart"
import Heatmap from "./Heatmap"
import "./App.css"
import DivisionChart from "./Charts/DivisionChart";

function Dashboard() {
  return (
    <Container fluid className="full-height-container custombackground" >
      <Row className="full-height-row border">
        <Col md={4} className="  custombackground full-height-col border" >
          <VehicleChart type={"radar"}></VehicleChart>
        </Col>
        <Col md={4} className="  custombackground full-height-col border">
        <DowChart  type= {"line"}></DowChart>
        </Col>
        <Col md={4} className="   custombackground full-height-col border">
          <PlaceChart type={"bar"}></PlaceChart>
        </Col>
      </Row>
      <Row className="full-height-row border">
      <Col md={4} className="   custombackground full-height-col border">
          <DivisionChart type={"pie"}></DivisionChart>
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
