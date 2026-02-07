import Upload from "./Upload";
import Summary from "./Summary";

function App() {
  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "20px auto",
        padding: "20px",
        backgroundColor: "#f8f9fa",
        borderRadius: "10px",
        boxShadow: "0 0 10px rgba(0,0,0,0.1)",
        fontFamily: "Arial"
      }}
    >
      <h2 style={{ textAlign: "center", color: "#2c3e50" }}>
        Chemical Equipment Parameter Visualizer
      </h2>

      <div
        style={{
          backgroundColor: "white",
          padding: "15px",
          borderRadius: "8px",
          marginBottom: "15px"
        }}
      >
        <Upload />
      </div>

      <div
        style={{
          backgroundColor: "white",
          padding: "15px",
          borderRadius: "8px"
        }}
      >
        <Summary />
      </div>
    </div>
  );
}

export default App;
