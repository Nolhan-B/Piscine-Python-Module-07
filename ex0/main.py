from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    print(f"CreatureCard Info:\n{dragon.get_card_info()}")

    mana_dict = {'mana': 6}
    print(f"\nPlaying {dragon.name} with "
          f"{mana_dict["mana"]} mana available")
    if (dragon.is_playable(mana_dict['mana'])):
        print("Playable: True")
        res = dragon.play(mana_dict)
        print(res)
        print(f"\nFire Dragon attacks {goblin.name}")
        print(dragon.attack_target(goblin))
    print("Playable: False")
    print("\nTesting insufficient mana (3 available):")
    mana_dict = {'mana': 3}
    dragon.play(mana_dict)

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
