from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int
                 ) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("mana", 0)):
            return {"error": "Not enough mana to play"}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target):
        damage = self.attack
        if isinstance(target, str):
            target_name = target
        else:
            target_name = target.name
            target.health -= self.attack
        combat_res = True
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": damage,
            "combat_resolved": combat_res
        }
