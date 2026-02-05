from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilites:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    elite = EliteCard("Arcane Warrior", 4, "Epic")

    print("Combat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result :", elite.defend(5))
    print("Magic phase:")
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", elite.channel_mana(3))


if __name__ == "__main__":
    main()
