import React from "react";
import Map from "./Map";

export default function Heatchart({height, width}) {
  return <div style={{ maxWidth: width ||'none', maxHeight: height || 'none', overflow: 'auto' }}><Map /></div>;
}
