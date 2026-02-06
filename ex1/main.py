from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    print("\n=== DataDeck Deck Builder === \n")

    print("Building deck with different card types...")
    deck = Deck()
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    l_bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
    n_crystal = ArtifactCard("Mana Crystal",
                             2,
                             "Common",
                             5,
                             "Permanent: +1 mana per turn")
    deck.add_card(dragon)
    deck.add_card(l_bolt)
    deck.add_card(n_crystal)
    print("Deck stat :", deck.get_deck_stats())

    mana = {'mana': 100}
    cards_to_play = [
                    {'e': l_bolt, 'type': 'Spell'},
                    {'e': n_crystal, 'type': 'Artifact'},
                    {'e': dragon, 'type': 'Creature'}
                    ]
    for card in cards_to_play:
        print(f"\nDrew: {card['e'].name} ({card['type']})")
        print("Play Result :", card['e'].play(mana))

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
