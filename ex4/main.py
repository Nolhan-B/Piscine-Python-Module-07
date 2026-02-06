from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main():
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    dragon = TournamentCard(
        "dragon_001", "Fire Dragon", 5, "Legendary", 7, 5, 1200
    )
    wizard = TournamentCard(
        "wizard_001", "Ice Wizard", 4, "Epic", 5, 4, 1150
    )

    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in [dragon, wizard]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}\n")

    print("Creating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")
    for line in platform.get_leaderboard():
        print(line)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
