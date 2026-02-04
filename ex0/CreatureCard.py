from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int
                 ) -> None:
        super().__init__(self, name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if self.is_playable(self) is True:
            return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": 'Creature summoned to battlefield'
                    }
        print("Playable: False")
        return {}

    def attack_target(self, target: Card) -> dict:
        return {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": True
               }
