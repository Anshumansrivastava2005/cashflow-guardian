import { Card, CardContent } from "@/components/ui/card";
import { Brain } from "lucide-react";

export default function AIInsights() {
  return (
    <Card className="bg-zinc-900 border-zinc-800 text-white h-full">
      <CardContent className="p-6">
        <div className="flex items-center gap-3 mb-5">
          <Brain className="text-blue-500" />
          <h2 className="font-bold text-xl">
            AI Insights
          </h2>
        </div>

        <ul className="space-y-4 text-zinc-300">
          <li>💡 Reduce food spending by ₹3,000</li>

          <li>📈 Increase SIP investment by ₹5,000</li>

          <li>⚠ Savings rate decreased this month</li>

          <li>✅ Financial health is excellent</li>
        </ul>
      </CardContent>
    </Card>
  );
}