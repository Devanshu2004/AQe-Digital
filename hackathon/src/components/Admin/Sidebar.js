import React, { useState } from "react";

const Sidebar = ({
  playerName = "Default Name",
  position = "Unknown",
  profileImage,
}) => {
  const [profileImageState, setProfileImage] = useState(profileImage);

  // Function to handle image upload
  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setProfileImage(URL.createObjectURL(file));
    }
  };

  // Function to get initials from name
  const getInitials = (name) => {
    if (!name) return ""; // Ensure name is not undefined
    return name
      .split(" ")
      .map((word) => word[0])
      .join("")
      .toUpperCase()
      .slice(0, 2);
  };

  return (
    <div className="w-64 h-screen bg-gray-800 text-white flex flex-col items-center p-4 border-r-4 border-green-600">
      {/* Profile Picture Section */}
      <label className="relative cursor-pointer mb-2">
        <input type="file" className="hidden" onChange={handleImageUpload} />
        <div className="w-28 h-28 rounded-full bg-gray-600 flex items-center justify-center text-white text-2xl font-bold border-3 border-green-600">
          {profileImageState ? (
            <img
              src={profileImageState}
              alt="Profile"
              className="w-full h-full object-cover rounded-full"
            />
          ) : (
            getInitials(playerName)
          )}
        </div>
      </label>
      {/* Player Name and Position */}
      <h3 className="text-2xl font-semibold mt-2">{playerName}</h3>
      <p className="text-gray-400 text-sm">{position}</p>{" "}
      {/* Display position */}
      {/* Sidebar Navigation Links */}
      <nav className="flex flex-col space-y-4 text-lg text-center mt-4 w-full">
        <a
          href="/admin/dashboard"
          className="hover:bg-gray-700 p-2 rounded border-b-2 border-green-600  w-full"
        >
          Dashboard
        </a>
        <a
          href="/admin/players"
          className="hover:bg-gray-700 p-2 rounded border-b-2 border-green-600 w-full"
        >
          Players
        </a>
        <a
          href="/admin/analytics"
          className="hover:bg-gray-700 p-2 rounded border-b-2 border-green-600 w-full"
        >
          Analytics & Stats
        </a>
      </nav>
    </div>
  );
};

export default Sidebar;
