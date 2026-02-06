from typing import List
from ex0.Card import Card


class GameEngine:
    def configure_engine(self, factory, strategy):
        self.factory = factory
        self.strategy = strategy
        self.hand: List[Card] = [
            factory.create_creature("dragon"),
            factory.create_creature("goblin"),
            factory.create_spell(),
            factory.create_artifact()
        ]
        self.battlefield: List[Card] = []

    def simulate_turn(self) -> dict:
        return self.strategy.execute_turn(self.hand, self.battlefield)

    def get_engine_status(self) -> dict:
        return {"hand": [c.name for c in self.hand]}
