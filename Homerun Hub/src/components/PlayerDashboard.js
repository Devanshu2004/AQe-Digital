import React, { useEffect, useState } from "react";
import { useParams, useLocation } from "react-router-dom";
import axios from "axios";
import Plot from "react-plotly.js";
import Sidebar from "../components/Admin/Sidebar";

const PlayerDashboard = () => {
  const { playerName: playerNameFromUrl } = useParams(); // Get playerName from URL
  const location = useLocation();

  // Extract player details from location.state
  const {
    playerName: passedPlayerName,
    position,
    profileImage,
  } = location.state || {};

  // If state is not passed, fall back to playerName from URL
  const finalPlayerName = passedPlayerName || playerNameFromUrl;

  const [players, setPlayers] = useState([]); // List of players for selection
  const [selectedPlayer, setSelectedPlayer] = useState(finalPlayerName); // Selected player
  const [figures, setFigures] = useState([]); // All figures for the player
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch player list on component mount
    axios
      .get(`http://127.0.0.1:8000/api/dashboard.json?player=${selectedPlayer}`)
      .then((response) => {
        setPlayers(response.data);
        setSelectedPlayer(response.data[0] || finalPlayerName); // Set default player or fallback
      })
      .catch((error) => console.error("Error fetching players:", error));
  }, [finalPlayerName]);

  useEffect(() => {
    if (!selectedPlayer) return;

    // Fetch player data based on selected player
    const fetchPlayerData = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/dashboard.json?player=${selectedPlayer}`
        );
        if (response.data.error) {
          console.error(response.data.error);
          setFigures([]);
        } else {
          setFigures(response.data.dashboard); // Set all figures
        }
      } catch (error) {
        console.error("Error fetching player data:", error);
        setFigures([]); // Handle fetch error
      } finally {
        setLoading(false);
      }
    };

    fetchPlayerData();
  }, [selectedPlayer]);

  return (
    <div style={{ display: "flex" }}>
      {/* Render Sidebar with passed data */}
      <Sidebar
        playerName={selectedPlayer}
        position={position}
        profileImage={profileImage}
      />
      <div style={{ flex: 1 }} className="p-4">
        <h2 className="text-2xl font-bold">{selectedPlayer}'s Performance</h2>

        {loading ? (
          <p className="text-gray-500 mt-4">Loading data...</p>
        ) : figures.length > 0 ? (
          <div className="mt-4">
            {figures.map((figure, index) => (
              <div key={index} style={{ marginBottom: "40px" }}>
                <Plot
                  data={JSON.parse(figure).data}
                  layout={JSON.parse(figure).layout}
                />
              </div>
            ))}
          </div>
        ) : (
          <div className="mt-4">
            <p className="text-gray-500">No data available for this player.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default PlayerDashboard;