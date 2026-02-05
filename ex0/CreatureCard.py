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
        if self.is_playable(game_state) is True:
            print("Playable: True")
            return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": 'Creature summoned to battlefield'
                    }
        print("Playable: False")
        return {}

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        }

    def attack_target(self, target: Card) -> dict:
        combat_res = True if target.health - self.attack <= 0 else False
        return {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": combat_res
               }
