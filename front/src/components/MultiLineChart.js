import React from "react";
import Chart from "react-google-charts";

function MultiLineChart({chart}) {

  return (
    <div 
    style={{
      margin: "0 auto",
      padding: "40px 25px",
      marginTop: "50px",
      float: "left"
    }}>
      <Chart
        width={"700px"}
        height={"410px"}
        chartType="LineChart"
        loader={<div>Loading Chart</div>}
        data={chart}
      />
    </div>
  );
}

export default MultiLineChart;
