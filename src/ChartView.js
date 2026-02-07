import { Pie } from "react-chartjs-2";
import { Chart, ArcElement, Tooltip, Legend } from "chart.js";

Chart.register(ArcElement, Tooltip, Legend);

export default function ChartView({ types }) {

  const data = {
    labels: Object.keys(types),
    datasets: [
      {
        data: Object.values(types),
        backgroundColor: [
          "red","blue","green","orange","purple","cyan"
        ]
      }
    ]
  };

  return (
    <div style={{ width: 400 }}>
      <Pie data={data} />
    </div>
  );
}
