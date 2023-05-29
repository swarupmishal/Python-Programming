from lib.deck import Deck
from lib.player import Player
from lib.war_card_game import WarCardGame

if __name__ == '__main__':
    player = Player("Swarup", Deck(is_empty=True))
    computer = Player("Computer", Deck(is_empty=True), is_computer=True)
    deck = Deck()
    game = WarCardGame(player, computer, deck)

    game.print_welcome_message()

    while not game.check_game_over():
        game.start_battle()
        game.print_stats()
        if game.check_game_over():
            break

        answer = input("\nAre you ready for the next round?\nPress Enter to continue. Enter X to stop.")

        if answer.lower() == "x":
            break
