# Implement function def tournament_winner(competitions: List[List[str]], results: List[int]) -> str:
# Competition is a list of list "two dementional array" representing the list of competitions
# Each element in competition consists of two entries "each is the name of competitors" example:my_list = [['HTML', 'C#'], ['C++', 'Python']]v
# Result is a list of integers "zero or one" zero means away team won and one means first team one
# example example:my_list = [['HTML', 'C#'], ['C++', 'Python']], result = [1,0] means 'HTML' won and 'Python' won
# Each winner gets 3 points and a team with the highest score  is the winner  the name of winner will be returned by the function
# Assume clear winner no ties
# run python3 tournament_winner.py
from typing import List
import unittest


def tournament_winner(competitions: List[List[str]], results: List[int]) -> str:
    """
    Assuming there are no ties and there is always a clear winner.
    Time complexity: O(n) where n is the number of competitions.
    Space complexity: O(k) where k is the number of unique teams.
    """
    # Initialize a dictionary to keep track of scores
    scores = {}
    current_winner = ""
    max_score = 0

    for i, competition in enumerate(competitions):
        home_team, away_team = competition
        winner = home_team if results[i] == 1 else away_team

        if winner not in scores:
            scores[winner] = 3
        else:
            scores[winner] += 3

        # Check if the current team has more points than the current winner
        if scores[winner] > max_score:
            current_winner = winner
            max_score = scores[winner]
        elif scores[winner] == max_score and current_winner == "":
            current_winner = winner

    return current_winner

# ---------------------------------------------------------

class tournamentWinner(unittest.TestCase):

 def test_tournament_winner(self):
    # Test case 1: HTML wins with 3 points
    competitions = [['HTML', 'C#']]
    results = [1]
    self.assertEqual(tournament_winner(competitions, results), 'HTML')

    # Test case 2: HTML wins with 6 points
    competitions = [['HTML', 'C#'], ['C++', 'Python'], ['HTML', 'Python']]
    results = [1, 0, 1]
    self.assertEqual(tournament_winner(competitions, results), 'HTML')

    # Test case 3: C++/HTML wins with 3 points
    competitions = [['HTML', 'C#'], ['C++', 'Python'], ['HTML', 'C++']]
    results = [1, 0, 0]
    self.assertEqual(tournament_winner(competitions, results), 'HTML')

    # Test case 4: Clear winner with multiple teams
    competitions = [['A', 'B'], ['A', 'C'], ['C', 'B'], ['D', 'B'], ['A', 'D']]
    results = [1, 1, 1, 1, 0]
    self.assertEqual(tournament_winner(competitions, results), 'A')

    # Test case 5: Another scenario with multiple teams
    competitions = [['A', 'B'], ['C', 'D'], [
        'E', 'F'], ['A', 'C'], ['B', 'D']]
    results = [0, 1, 1, 0, 0]
    self.assertEqual(tournament_winner(competitions, results), 'C')
    


# ---------------------------------------
if __name__ == "__main__":
    unittest.main()
