from typing import List
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List):
        return available_targets

    def execute_turn(self, hand: List, battlefield: List) -> dict:
        actions = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0
        }

        for card in hand:
            if isinstance(card, CreatureCard):
                play_res = card.play({"mana": 10})
                actions["cards_played"].append(card.name)
                actions["mana_used"] += play_res.get("mana_used", 0)
                attack_res = card.attack_target("Enemy Player")
                actions["targets_attacked"].append(attack_res["target"])
                actions["damage_dealt"] += attack_res.get("damage_dealt", 0)
            elif isinstance(card, SpellCard):
                spell_res = card.resolve_effect(["Enemy Player"])
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost
                if card.effect_type == "damage":
                    actions["damage_dealt"] += 3
            elif isinstance(card, ArtifactCard):
                artifact_res = card.activate_ability()
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost

        return {"strategy": self.get_strategy_name(), "actions": actions}
