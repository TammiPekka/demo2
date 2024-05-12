class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.scores = {player1_name: 0, player2_name : 0}
        self.player1_name = player1_name
        self.player2_name = player2_name

    def won_point(self, player_name):
        self.scores[player_name] += 1


    def _score_tied(self, score):
        if score < 3:
            return ["Love-All", "Fifteen-All", "Thirty-All"][score]
        else:
            return "Deuce"

    def _score_more_than_four(self, player1_score, player2_score):
        score_diff = player1_score - player2_score
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"


    def _regular_score(self, player1_score, player2_score):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{scores[player1_score]}-{scores[player2_score]}"

    def get_score(self):
        player1_score, player2_score = self.scores[self.player1_name], self.scores[self.player2_name]

        if player1_score == player2_score:
            return self._score_tied(player1_score)
        elif player1_score >= 4 or player2_score >= 4:
            return self._score_more_than_four(player1_score, player2_score)
        else:
            return self._regular_score(player1_score, player2_score)
