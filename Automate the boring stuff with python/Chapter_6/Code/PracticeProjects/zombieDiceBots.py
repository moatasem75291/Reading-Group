#! python3
# zombieDiceBots.py - Simulates multiple games of Zombie Dice with bots.
"""
Zombie Dice is a game where you roll dice to eat brains, but if you get shot three times, you lose.
The game is played with 13 dice, each with 6 sides. 3 sides are brains, 2 are footprints, and 1 is a shotgun.
The game is played with 2-8 players, and each player takes turns rolling 3 dice at a time.
The game ends when a player has 13 brains or a player has been shot 3 times.
The winner is the player with the most brains.
The game is played with 3 different colored dice, each with a different probability of rolling a shotgun.
The game is played with 6 green dice, 4 yellow dice, and 3 red dice.
The green dice have 1 shotgun, the yellow dice have 2 shotguns, and the red dice have 3 shotguns.
The game is played with 3 different bots, each with a different strategy.
The first bot is the random bot, which randomly decides to roll again or stop.
The second bot is the cautious bot, which stops after 2 shotguns.
The third bot is the aggressive bot, which stops after 1 shotgun.
"""

import zombiedice
import sys


class GameState:
    """Represent the state of the game for all players."""

    def __init__(self, players: list):
        self.players = {
            name: {
                "score": 0,
                "brains_eaten": 0,
                "shotguns_taken": 0,
                "zombie_tokens": 0,
            }
            for name in players
        }

    def update_state(
        self,
        name,
        score: int,
        brains_eaten: int,
        shotguns_taken: int,
        zombie_tokens: int,
    ) -> None:
        """Update the state of the game for a player"""
        self.players[name] = {
            "score": score,
            "brains_eaten": brains_eaten,
            "shotguns_taken": shotguns_taken,
            "zombie_tokens": zombie_tokens,
        }


class MyZombie:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.brains_eaten = 0
        self.shotguns_taken = 0
        self.zombie_tokens = 0

    def turn(self, gameState: GameState) -> None:
        dice_results = zombiedice.roll()
        self.process_results(dice_results, gameState)

    def process_results(self, dice_results: list, gameState: GameState) -> None:
        """Process the results and update the player's score, tokens, etc."""
        brains = dice_results["brains"]
        self.brains_eaten += brains
        self.score += brains
        # print(f"{self.name} ate {brains} brains.")

        footsteps = dice_results["footsteps"]
        # print(f"{self.name} got {footsteps} footsteps.")

        shotguns = dice_results["shotgun"]
        self.shotguns_taken += shotguns
        # print(f"{self.name} got {shotguns} shotgun blasts.")

        self.zombie_tokens += 1


def main():
    """Simulate a game of Zombie Dice with bots."""
    if len(sys.argv) < 2:
        print("Usage: python3 zombieDiceBots.py [player1] [player2] [player3] ...")
        sys.exit()

    player_names = sys.argv[1:]

    players = [MyZombie(name) for name in player_names]
    zombies = (
        zombiedice.examples.RandomCoinFlipZombie(name="Random"),
        zombiedice.examples.MonteCarloZombie(
            name="Monte Carlo", riskiness=40, numExperiments=20
        ),
        zombiedice.examples.RollsUntilInTheLeadZombie(name="Until Leading"),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(
            name="Stop at 2 Shotguns", minShotguns=2
        ),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(
            name="Stop at 1 Shotgun", minShotguns=1
        ),
        zombiedice.examples.AlwaysRollsTwiceZombie(name="Roll Twice"),
        *players,
    )

    zombiedice.runWebGui(zombies=zombies, numGames=10000)
    # zombiedice.runTournament(zombies=zombies, numGames=1000)


if __name__ == "__main__":
    main()
