import { useEffect, useState } from "react";

import {
  Wallet,
  TrendingUp,
  TrendingDown,
  Brain,
} from "lucide-react";

import {
  getSummary,
  getMonthly,
} from "../services/dashboard";

import { getCurrentUser } from "../services/auth";

import StatCard from "@/components/dashboard/StatCard";
import CashFlowChart from "@/components/dashboard/CashFlowChart";
import AIInsights from "@/components/dashboard/AIInsights";
import RecentTransactions from "@/components/dashboard/RecentTransactions";

export default function Dashboard() {
  const [user, setUser] = useState(null);

  const [summary, setSummary] = useState({
    current_balance: 0,
    total_income: 0,
    total_expense: 0,
    total_transactions: 0,
  });

  const [monthly, setMonthly] = useState([]);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadDashboard = async () => {
      try {
        const userData = await getCurrentUser();
        setUser(userData);

        const summaryData = await getSummary();
        setSummary(summaryData);

        const monthlyData = await getMonthly();
        setMonthly(monthlyData);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    loadDashboard();
  }, []);

  if (loading) {
    return (
      <div className="text-white text-2xl">
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold text-white">
          Welcome Back, {user?.full_name} 👋
        </h1>

        <p className="text-zinc-400 mt-2">
          Here's your financial overview.
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <StatCard
          title="Current Balance"
          value={`₹${summary.current_balance}`}
          icon={Wallet}
          color="text-blue-500"
        />

        <StatCard
          title="Income"
          value={`₹${summary.total_income}`}
          icon={TrendingUp}
          color="text-green-500"
        />

        <StatCard
          title="Expenses"
          value={`₹${summary.total_expense}`}
          icon={TrendingDown}
          color="text-red-500"
        />

        <StatCard
          title="Transactions"
          value={summary.total_transactions}
          icon={Brain}
          color="text-purple-500"
        />

      </div>

      <div className="grid gap-6 lg:grid-cols-3">

        <div className="lg:col-span-2">
          <CashFlowChart data={monthly} />
        </div>

        <AIInsights />

      </div>

      <RecentTransactions />

    </div>
  );
}