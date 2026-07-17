import { Card, CardContent } from "@/components/ui/card";

const transactions = [
  {
    name: "Salary",
    amount: "+ ₹85,000",
  },
  {
    name: "Amazon",
    amount: "- ₹2,499",
  },
  {
    name: "Swiggy",
    amount: "- ₹420",
  },
  {
    name: "Fuel",
    amount: "- ₹1,200",
  },
];

export default function RecentTransactions() {
  return (
    <Card className="bg-zinc-900 border-zinc-800 text-white">
      <CardContent className="p-6">
        <h2 className="font-bold text-xl mb-5">
          Recent Transactions
        </h2>

        <div className="space-y-4">
          {transactions.map((item) => (
            <div
              key={item.name}
              className="flex justify-between border-b border-zinc-800 pb-3"
            >
              <span>{item.name}</span>

              <span>{item.amount}</span>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}