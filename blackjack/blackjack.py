from Chips import Chips
from Deck import Deck
from Hand import Hand

playing = True


def take_bet(chips):
    while True:
        try:
            bet = int(input("Place your bet: "))
            if bet < 1:
                raise
        except:
            print("That is not a valid bet!")
        else:
            if bet > chips.total:
                print("Insufficient funds")
                continue
            else:
                chips.bet = bet
                break


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        choice = input("Hit or stand?(h/s): ")
        if choice.lower() == 'h':
            hit(deck, hand)
            break
        elif choice.lower() == 's':
            playing = False
            break


def show_some(player, dealer):
    print("Player cards:", end=' ')
    print(*player.cards, sep=", ")
    print(f'Total: {player.value}\n')
    print(f'Dealer cards: {dealer.cards[1]}\n')


def show_all(player, dealer):
    print("Player cards:", end=' ')
    print(*player.cards, sep=", ")
    print(f'Total: {player.value}\n')
    print("Dealer cards:", end=' ')
    print(*dealer.cards, sep=", ")
    print(f'Total: {dealer.value}\n')


def player_busts():
    print("Player busts")
    return True


def player_wins(chips):
    chips.win_bet()
    print("Player wins!")


def dealer_busts():
    print("Dealer busts")
    return True


def dealer_wins(chips):
    chips.lose_bet()
    print("Dealer wins!")


def push():
    print("Push")


print("Welcome to the blackjack table!")
# set up player chips
player_chips = Chips()
while True:
    # check if valid funds
    if player_chips.total == 0:
        print("You ran out of money. Goodbye!")
        break

    choice = input("\nWould you like to play?(y/n): ")
    if choice.lower() == 'y':
        pass
    elif choice.lower() == 'n':
        break
    else:
        continue

    playing = True
    blackjack = False
    player_bust = False
    dealer_bust = False

    # Create & shuffle the deck
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()

    # Prompt the Player for their bet
    take_bet(player_chips)
    print()

    # deal cards
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())

    # check for blackjack
    if player.value == 21 or dealer.value == 21:
        playing = False
        blackjack = True
        print("Blackjack!")
        show_all(player, dealer)

    while playing and player.value < 21:
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_bust = player_busts()

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while not player_bust and not blackjack:
        # Show all cards
        show_all(player, dealer)
        if dealer.value < 17:
            hit(deck, dealer)
        else:
            break

    # check dealer bust
    if dealer.value > 21:
        dealer_bust = dealer_busts()

    # Run different winning scenarios
    if (player_bust or dealer.value > player.value) and not dealer_bust:
        dealer_wins(player_chips)
    elif dealer.value == player.value:
        push()
    else:
        player_wins(player_chips)

    # Inform Player of their chips total
    print(f'Total chips: {player_chips.total}')

    del deck
    del player
    del dealer
