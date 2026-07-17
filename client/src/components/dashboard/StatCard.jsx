import { Card, CardContent } from "@/components/ui/card";

export default function StatCard({
  title,
  value,
  icon: Icon,
  color = "text-blue-500",
}) {
  return (
    <Card className="bg-zinc-900 border-zinc-800 text-white">
      <CardContent className="p-5 flex items-center justify-between">
        <div>
          <p className="text-zinc-400 text-sm">{title}</p>

          <h2 className="text-3xl font-bold mt-2">
            {value}
          </h2>
        </div>

        <div className={`${color}`}>
          <Icon size={36} />
        </div>
      </CardContent>
    </Card>
  );
}