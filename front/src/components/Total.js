import React from "react";


function Total({cost}) {
  return (
    <div
      style={{
        width: "300px",
        marginRight: "500px",
        marginTop: "100px",
        float: "right",
        fontSize: "18px",
        border: "1px solid black",
      }}
    >
      <p
        style={{
          margin: "0",
          fontSize: "24px",
          borderBottom: "1px solid black",
          color: "white",
          backgroundColor: "black",
        }}
      >
        Total
      </p>
      <h1>{cost}</h1>
    </div>
  );
}

export default Total;
