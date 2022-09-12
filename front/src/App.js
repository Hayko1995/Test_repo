import "./App.css";
import React, { useEffect, useState } from "react";
import axios from "axios";

import MultiLineChart from "./components/MultiLineChart";
import ResponsiveAppBar from "./components/Hader";
import Total from "./components/Total";
import Sheet from "./components/Sheet";


function App() {
  const [linarChart, setLinarChart] = useState([]);
  const [cost, setCost] = useState(0);
  const [list, setList] = useState([]);



  useEffect(() => {
    setInterval(fetchData, 1000); // The function will be called
  }, []);

  const fetchData = async () => {
    try {
      const { data: response } = await axios.get(
        "http://127.0.0.1:8000/simple_page/"
      );
      var col = response[1].map(function (value, index) {
        return [value[3], parseFloat(value[2])];
      });
      var headers = []
      headers.push( response[0].map(function (value, index){
        return {value: value};
      }))

      response[1].forEach((element) => {
        headers.push( element.map(function (value, index){
          return {value: value};
        }))
      });

      setList(headers)
      var chart = [];
      chart.push(["x", "chart"]);
      col.forEach((element) => chart.push(element));
      setLinarChart(chart);
      var cost = 0
      response[1].forEach((element) => cost +=  parseFloat(element[2]));
      setCost(cost)

    } catch (error) {
      console.error(error.message);
    }
  };

  return (
    <div className="App">
      <ResponsiveAppBar />
      <MultiLineChart chart={linarChart} />
      <Total cost={cost} />
      <Sheet list= {list} />

    </div>
  );
}

export default App;
