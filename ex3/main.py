from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("\n=== DataDeck Game Engine ===\n")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Configuring Fantasy Card Game...")
    print("Factory:", type(factory).__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")
    turn_result = engine.simulate_turn()
    hand_str = ""
    for card in engine.hand:
        if hand_str:
            hand_str += ", "
        hand_str += card.name + " (" + str(card.cost) + ")"

    print("Hand:", hand_str)

    print("\nTurn execution:")
    print("Strategy:", turn_result["strategy"])
    print("Actions:", turn_result["actions"])

    print("\nGame Report:")
    print({
        "turns_simulated": 1,
        "strategy_used": turn_result["strategy"],
        "total_damage": turn_result["actions"]["damage_dealt"],
        "cards_created": 4
    })
    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
