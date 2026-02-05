import random
from typing import List, Optional
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)

        creatures = sum(
            1 for card in self.cards
            if card.__class__.__name__ == "CreatureCard"
        )
        spells = sum(
            1 for card in self.cards
            if card.__class__.__name__ == "SpellCard"
        )
        artifacts = sum(
            1 for card in self.cards
            if card.__class__.__name__ == "ArtifactCard"
        )

        avg_cost = (
            sum(card.cost for card in self.cards) / total_cards
            if total_cards > 0 else 0
        )

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1)
        }
