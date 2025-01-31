import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./Layout";
import HomePage from "./components/Home/HomePage";
import AdminPanel from "./components/Admin/AdminPanel";
import Dashboard from "./components/Admin/Dashboard";
import PlayerDashboard from "./components/PlayerDashboard";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<HomePage />} />
          <Route path="/admin" element={<AdminPanel />} />
          <Route path="/admin/dashboard" element={<Dashboard />} />
          <Route path="/player/:playerName" element={<PlayerDashboard />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
