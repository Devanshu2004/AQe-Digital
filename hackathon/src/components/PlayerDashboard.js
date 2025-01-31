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
  const [exitVelocityData, setExitVelocityData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch player list on component mount
    axios
      .get("http://127.0.0.1:5000/api/players")
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
          `http://127.0.0.1:5000/get_player_data?player=${selectedPlayer}`
        );
        // Safely parse the exit_velocity data
        try {
          setExitVelocityData(JSON.parse(response.data.exit_velocity));
        } catch (parseError) {
          console.error("Error parsing exit velocity data:", parseError);
          setExitVelocityData(null); // Handle parsing error
        }
      } catch (error) {
        console.error("Error fetching player data:", error);
        setExitVelocityData(null); // Handle fetch error
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
        ) : exitVelocityData ? (
          <div className="mt-4">
            <Plot
              data={exitVelocityData.data}
              layout={exitVelocityData.layout}
            />
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
