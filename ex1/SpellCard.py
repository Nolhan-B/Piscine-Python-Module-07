from ex0.Card import Card
from typing import List

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)

        if effect_type not in {"damage", "heal", "buff", "debuff"}:
            raise ValueError("Invalid effect type")

        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state['mana']):
            return {"error": "Not enough mana to cast spell"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self._describe_effect()
        }

    def resolve_effect(self, targets: List[str]) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }

    def _describe_effect(self) -> str:
        if self.effect_type == "damage":
            return "Deal 3 damage to target"
        if self.effect_type == "heal":
            return "Restore 3 health to target"
        if self.effect_type == "buff":
            return "Increase target stats temporarily"
        if self.effect_type == "debuff":
            return "Reduce target stats temporarily"

        return "Unknown spell effect"