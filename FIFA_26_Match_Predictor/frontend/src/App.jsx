import MatchPredictor from "./components/MatchPredictor";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-10">
      <div className="w-full max-w-lg">
        <h1 className="text-3xl font-bold mb-6 text-center">
          ⚽ FIFA Match Predictor
        </h1>
        <MatchPredictor />
      </div>
    </div>
  );
}




