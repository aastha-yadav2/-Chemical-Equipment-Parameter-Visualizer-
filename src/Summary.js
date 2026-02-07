import axios from "axios";
import { useEffect, useState } from "react";
import ChartView from "./ChartView";

export default function Summary() {

  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/summary/")
      .then(res => setData(res.data))
  }, []);

  if (!data) return <p>No Data Found</p>;

  return (
    <div>

      <h3>Total Equipment: {data.total}</h3>
      <h4>Avg Flowrate: {data.avg_flowrate}</h4>
      <h4>Avg Pressure: {data.avg_pressure}</h4>
      <h4>Avg Temperature: {data.avg_temperature}</h4>

      <ChartView types={data.types} />

      {/* ---------- TABLE ADDED HERE ---------- */}

      <h3 style={{ marginTop: 20 }}>Equipment Type Distribution</h3>

      <table border="1" cellPadding="8" style={{ marginTop: 10 }}>
        <thead>
          <tr>
            <th>Type</th>
            <th>Count</th>
          </tr>
        </thead>

        <tbody>
          {Object.entries(data.types).map(([type, count]) => (
            <tr key={type}>
              <td>{type}</td>
              <td>{count}</td>
            </tr>
          ))}
        </tbody>

      </table>

    </div>
  );
}
