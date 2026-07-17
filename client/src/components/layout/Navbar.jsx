import { useEffect, useState } from "react";
import { LogOut } from "lucide-react";
import { useNavigate } from "react-router-dom";

import { getCurrentUser, logout } from "../../services/auth";

export default function Navbar() {
  const navigate = useNavigate();

  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const data = await getCurrentUser();
        setUser(data);
      } catch (err) {
        console.error("Failed to fetch user:", err);

        logout();
        navigate("/login");
      }
    };

    fetchUser();
  }, [navigate]);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <header className="flex items-center justify-between border-b bg-white px-6 py-4 shadow-sm">
      <div>
        <h1 className="text-2xl font-bold text-gray-800">
          CashFlow Guardian
        </h1>

        <p className="text-gray-500">
          Welcome,{" "}
          <span className="font-semibold">
            {user ? user.full_name : "Loading..."} 👋
          </span>
        </p>
      </div>

      <button
        onClick={handleLogout}
        className="flex items-center gap-2 rounded-lg bg-red-600 px-4 py-2 text-white hover:bg-red-700 transition"
      >
        <LogOut size={18} />
        Logout
      </button>
    </header>
  );
}