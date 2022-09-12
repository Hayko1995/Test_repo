import React from "react";
import Spreadsheet from "react-spreadsheet";


function Sheet({ list }) {
    console.log(list)
  return (
    <div
      style={{
        width: "300px",
        margin: "50px",
        float: "left",
        fontSize: "18px",
      }}
    >
      <Spreadsheet data={list} />
    </div>
  );
}

export default Sheet;
