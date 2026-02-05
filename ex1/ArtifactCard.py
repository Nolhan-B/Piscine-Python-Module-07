from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)

        if durability <= 0:
            raise ValueError("Durability must be a positive integer")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state["mana"]):
            return {"error": "Not enough mana to play artifact"}

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.effect}"
        }

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "Artifact is destroyed"
            }

        self.durability -= 1

        return {
            "artifact": self.name,
            "activated": True,
            "remaining_durability": self.durability,
            "effect": self.effect
        }
