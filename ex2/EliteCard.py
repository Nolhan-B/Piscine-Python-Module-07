from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int = 5,
        defense: int = 3,
        mana: int = 5
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or defense < 0 or mana < 0:
            raise ValueError("Invalid EliteCard stats")

        self.attack_power = attack
        self.defense_power = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("mana", 0)):
            return {"error": "Not enough mana to play EliteCard"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters the battlefield"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense_power, incoming_damage)
        taken = incoming_damage - blocked

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < self.attack_power
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense_power
        }

    def cast_spell(self, spell_name: str, targets: List[str]) -> dict:
        mana_cost = 4
        if self.mana < mana_cost:
            return {"error": "Not enough mana to cast spell"}

        self.mana -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        if amount <= 0:
            raise ValueError("Mana amount must be positive")

        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "current_mana": self.mana
        }
