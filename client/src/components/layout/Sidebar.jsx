import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Wallet,
  BarChart3,
  Brain,
  ShieldCheck,
} from "lucide-react";

const links = [
  {
    name: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    name: "Transactions",
    path: "/transactions",
    icon: Wallet,
  },
  {
    name: "Analytics",
    path: "/analytics",
    icon: BarChart3,
  },
  {
    name: "AI Advisor",
    path: "/advisor",
    icon: Brain,
  },
  {
    name: "Risk",
    path: "/risk",
    icon: ShieldCheck,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-zinc-900 border-r border-zinc-800">
      <div className="p-6 text-2xl font-bold">
        💰 CashFlow Guardian
      </div>

      <nav className="px-4 space-y-2">
        {links.map((link) => (
          <NavLink
            key={link.path}
            to={link.path}
            className={({ isActive }) =>
              `flex items-center gap-3 rounded-lg px-4 py-3 transition ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "hover:bg-zinc-800 text-zinc-300"
              }`
            }
          >
            <link.icon size={20} />
            {link.name}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}