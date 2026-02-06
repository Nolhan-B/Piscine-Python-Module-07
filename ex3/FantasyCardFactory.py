import random
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power=None) -> CreatureCard:
        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None) -> SpellCard:
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        return ArtifactCard("Mana Crystal",
                            2,
                            "Rare",
                            3,
                            "Permanent: +1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            card_type = random.choice(['creature', 'spell', 'artifact'])
            if card_type == 'creature':
                deck.append(self.create_creature())
            elif card_type == 'spell':
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {'cards': deck, 'size': len(deck)}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "ice"],
            "artifacts": ["mana_ring"]
        }
