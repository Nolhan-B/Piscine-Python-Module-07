from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random

class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, card_id: str, name: str, cost: int, rarity: str, attack: int, health: int, base_rating: int):
        Card.__init__(self, name, cost, rarity)
        self.card_id = card_id
        self.attack_power = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.rating = base_rating

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "status": "ready_for_tournament"
        }

    def attack(self, target) -> dict:
        outcome = random.choice([True, False])
        return {
            "attacker": self.card_id,
            "defender": target.card_id,
            "winner": self.card_id if outcome else target.card_id
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def defend(self, damage: int) -> dict:
        self.health -= damage
        defeated = self.health <= 0
        return {
            "defender": self.card_id,
            "damage_taken": damage,
            "defeated": defeated
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }
