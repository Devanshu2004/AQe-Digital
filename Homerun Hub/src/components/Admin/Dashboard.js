// import React from "react";

// const Dashboard = () => {
//   return <div></div>;
// };

// export default Dashboard;

import React, { useEffect, useState } from "react";
import axios from "axios";
import Plot from "react-plotly.js";

const Dashboard = () => {
  const [player, setPlayer] = useState(""); // Selected player
  const [players, setPlayers] = useState([]); // List of players
  const [figures, setFigures] = useState([]); // Figures for the plots
  const [loading, setLoading] = useState(true); // Loading state

  // Fetch the list of players on component mount
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/players") // Replace with your API endpoint
      .then((response) => {
        setPlayers(response.data);
        if (response.data.length > 0) {
          setPlayer(response.data[0]); // Set the default player
        }
      })
      .catch((error) => console.error("Error fetching players:", error));
  }, []);

  // Fetch player data when the selected player changes
  useEffect(() => {
    if (!player) return;

    setLoading(true);
    axios
      .get(`http://127.0.0.1:8000/api/dashboard.json?player=${player}`)
      .then((response) => {
        if (response.data.error) {
          console.error(response.data.error);
          setFigures([]);
        } else {
          setFigures(response.data.dashboard);
        }
      })
      .catch((error) => console.error("Error fetching player data:", error))
      .finally(() => setLoading(false));
  }, [player]);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Baseball Player Performance Dashboard</h1>

      {/* Dropdown to select a player */}
      <div>
        <label htmlFor="player-select">Select Player: </label>
        <select
          id="player-select"
          value={player}
          onChange={(e) => setPlayer(e.target.value)}
        >
          {players.map((playerName) => (
            <option key={playerName} value={playerName}>
              {playerName}
            </option>
          ))}
        </select>
      </div>

      {/* Display loading message */}
      {loading && <p>Loading data...</p>}

      {/* Render the plots */}
      {!loading && figures.length > 0 && (
        <div>
          {figures.map((figure, index) => (
            <div key={index} style={{ marginBottom: "40px" }}>
              <Plot
                data={JSON.parse(figure).data}
                layout={JSON.parse(figure).layout}
              />
            </div>
          ))}
        </div>
      )}

      {/* Display error if no data is available */}
      {!loading && figures.length === 0 && (
        <p>No data available for this player.</p>
      )}
    </div>
  );
};

export default Dashboard;