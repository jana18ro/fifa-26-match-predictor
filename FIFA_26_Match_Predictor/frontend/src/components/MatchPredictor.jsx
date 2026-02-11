import { useState } from "react";

export default function MatchPredictor() {
  const [team1, setTeam1] = useState("");
  const [team2, setTeam2] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  async function handlePredict() {
    setError(null);
    setResult(null);

    try {
      const res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ team1, team2 }),
      });

      if (!res.ok) {
        throw new Error("Prediction failed");
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError("Could not fetch prediction. Is backend running?");
    }
  }

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <input
        className="border p-2 w-full mb-3"
        placeholder="Team 1"
        value={team1}
        onChange={(e) => setTeam1(e.target.value)}
      />

      <input
        className="border p-2 w-full mb-4"
        placeholder="Team 2"
        value={team2}
        onChange={(e) => setTeam2(e.target.value)}
      />

      <button
        onClick={handlePredict}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 w-full"
      >
        Predict
      </button>

      {error && (
        <p className="text-red-600 mt-4 text-sm">{error}</p>
      )}

      {result && (
        <pre className="mt-4 text-sm bg-gray-100 p-3 rounded">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}
