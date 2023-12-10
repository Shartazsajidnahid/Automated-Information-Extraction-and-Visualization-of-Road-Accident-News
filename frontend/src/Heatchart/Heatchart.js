import React from "react";
import Map from "./Map";

export default function Heatchart({height, width}) {
  return <div style={{ maxWidth: width, maxHeight: height, overflow: 'auto' }}><Map /></div>;
}
