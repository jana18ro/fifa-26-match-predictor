export async function predictMatch(team1, team2) {
  const res = await fetch("http://localhost:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      team1: team1.name,
      team2: team2.name,
    }),
  });

  if (!res.ok) {
    throw new Error("Prediction failed");
  }

  return res.json();
}
