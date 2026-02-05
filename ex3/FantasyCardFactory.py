from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

class FantasyCardFactory:
    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "ice"],
            "artifacts": ["mana_ring"]
        }

    def create_creature(self, name_or_power=None) -> CreatureCard:
        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None) -> SpellCard:
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        return ArtifactCard("Mana Crystal", 2, "Rare", 3, "Permanent: +1 mana per turn")
