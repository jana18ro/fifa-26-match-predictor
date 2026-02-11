import numpy as np
from sklearn.linear_model import LogisticRegression

class MatchPredictorModel:
    def __init__(self):
        self.model = LogisticRegression()
        self._train_model()

    def _train_model(self):
        # Simple synthetic training data
        # Features: [attack_diff, defense_diff, midfield_diff]
        X = np.array([
            [5, 4, 3],
            [-5, -4, -3],
            [3, 2, 2],
            [-3, -2, -2],
            [1, 1, 0],
            [-1, -1, 0]
        ])

        # 1 = team1 win, 0 = team2 win
        y = np.array([1, 0, 1, 0, 1, 0])

        self.model.fit(X, y)

    def predict_match(self, team1, team2):
        features = np.array([[
            team1["attack"] - team2["attack"],
            team1["defense"] - team2["defense"],
            team1["midfield"] - team2["midfield"]
        ]])

        prob_team1 = float(self.model.predict_proba(features)[0][1])
        prob_team2 = 1 - prob_team1
        draw_prob = 0.15

        score1 = max(0, round(team1["attack"] / 30))
        score2 = max(0, round(team2["attack"] / 30))

        return {
            "team1_score": score1,
            "team2_score": score2,
            "team1_win_probability": int(prob_team1 * 100),
            "team2_win_probability": int(prob_team2 * 100),
            "draw_probability": int(draw_prob * 100),
            "key_player_team1": "Key Attacker",
            "key_player_team2": "Defensive Leader",
            "match_prediction": "Prediction based on comparative team strengths.",
            "excitement_rating": min(5, score1 + score2)
        }
