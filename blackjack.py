import random, time

cards = {
    'ace of hearts' : 1, 'two of hearts' : 2, 'three of hearts': 3, 'four of hearts' : 4, 'five of hearts' : 5, 'six of hearts': 6, 'seven of hearts' : 7,
    'eight of hearts' : 8, 'nine of hearts': 9, 'ten of hearts': 10, 'jack of hearts': 10, 'queen of hearts': 10, 'king of hearts': 10, 'ace of spades' : 1,
    'two of spades' : 2, 'three of spades': 3, 'four of spades' : 4, 'five of spades' : 5, 'six of spades': 6, 'seven of spades' : 7, 'eight of spades' : 8,
    'nine of spades': 9, 'ten of spades': 10, 'jack of spades': 10, 'queen of spades': 10, 'king of spades': 10, 'ace of diamonds' : 1, 'two of diamonds' : 2,
    'three of diamonds': 3, 'four of diamonds' : 4, 'five of diamonds' : 5, 'six of diamonds': 6, 'seven of diamonds' : 7, 'eight of diamonds' : 8, 'nine of diamonds': 9,
    'ten of diamonds': 10, 'jack of diamonds': 10, 'queen of diamonds': 10, 'king of diamonds': 10, 'ace of clubs' : 1, 'two of clubs' : 2, 'three of clubs': 3,
    'four of clubs' : 4, 'five of clubs' : 5, 'six of clubs': 6, 'seven of clubs' : 7, 'eight of clubs' : 8, 'nine of clubs': 9, 'ten of clubs': 10,
    'jack of clubs': 10, 'queen of clubs': 10, 'king of clubs': 10,
    }

deck = list(cards.keys())
random.shuffle(deck)

class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.deck = list(cards.keys())

    def getDeck(self):
        return random.shuffle(self.deck)

    def gameSetup(self, player, dealer):
        if len(self.deck) < 10:
            self.deck = list(cards.keys())
        self.getDeck()
        player.hand = [self.deck.pop(-4), self.deck.pop(-2)]
        dealer.hand = [self.deck.pop(-3), self.deck.pop(-1)]
        player.handValue = player.getValue()
        dealer.handValue = dealer.getValue()
        for n in dealer.hand:
            if n[0] == 'a' and dealer.handValue < 12:
                dealer.handValue += 10
        self.firstEval(player, dealer)
        return
        
    def firstEval(self, player, dealer):
        print('... shuffling cards')
        time.sleep(1)
        print('================================================================\n')
        print(f'You have {player.hand[0]} and {player.hand[1]} for a total of {player.handValue}\n')
        print(f'Dealer is showing {dealer.hand[1]}\n')
        print('================================================================')
        if player.handValue == 21:
            print('Congratulations!! You have BlackJack!!')
            print(f"Dealer has revealed {dealer.hand[0]}. That makes Dealer's total {dealer.handValue}")
        return

    def playerHit(self, player):
        card = self.deck.pop()
        player.hand.append(card)
        player.handValue += cards[card]
        return

    def playerEval(self, player):
        response = 'a'
        while response.lower() != 's':
            response = input(f' You have {player.handValue}. Do you want to hit or stand? (h/s) ')
            if response.lower() == 'h':
                self.playerHit(player)
                print(f'You have been dealt a {player.hand[-1]}. That makes your total {player.handValue}')
                if player.handValue > 21:
                    break
                elif player.handValue == 21:
                    print('You have 21, great hand!')
                    response = 's'
            elif response.lower() == 's':
                continue
            else:
                print("Please enter 'h' for hit or 's' for stand.")
        return

    def dealerEval(self, dealer):
        print(f"Dealer has revealed {dealer.hand[0]}. That makes Dealer's total {dealer.handValue}")
        while dealer.handValue < 17:
            self.dealerHit(dealer)
            print(f'Dealer has been dealt {dealer.hand[-1]}, bringing their total to {dealer.handValue}')
        return            

    def dealerHit(self, dealer):
        card = self.deck.pop()
        dealer.hand.append(card)
        dealer.handValue += cards[card]
        return

    def handOver(self, player, dealer):
        if player.handValue > 21 and dealer.handValue > 21:
            print('You and the dealer both busted, you push.')
            player.pushes
        elif dealer.handValue > 21:
            print('Dealer busts, you win!!')
            player.wins += 1
        elif player.handValue > 21:
            print('You busted :(')
            player.losses += 1
        elif player.handValue > dealer.handValue:
            print(f"You have won with {player.handValue}, which beats Dealer's {dealer.handValue}.")
            player.wins += 1
        elif dealer.handValue > player.handValue:
            print(f'Dealer has won with {dealer.handValue}, which beats your {player.handValue}.')
            player.losses += 1
        elif player.handValue == dealer.handValue:
            print(f'You and the Dealer both have {player.handValue}. You pushed.')
            player.pushes += 1
        return


class Player:
    def __init__(self, hand = [], handValue = 0, wins = 0, losses = 0, pushes = 0):
        self.hand = hand
        self.handValue = handValue
        self.wins = wins
        self.losses = losses
        self.pushes = pushes

    def getValue(self):
        self.handValue = [cards[card] for card in self.hand]
        return sum(self.handValue)

class Dealer:
    def __init__(self, hand = [], handValue = 0):
        self.hand = hand
        self.handValue = handValue

    def getValue(self):
        self.handValue = [cards[card] for card in self.hand]
        return sum(self.handValue)


name = input('What is your name? ')
player = name
player = Player()
dealer = Dealer()
blackjack = Game(player, dealer)
while True:
    blackjack.gameSetup(player, dealer)
    blackjack.playerEval(player)
    blackjack.dealerEval(dealer)
    blackjack.handOver(player, dealer)
    while True:
        playAgain = input('Do you want to play again? (y/n) ')
        if playAgain.lower() == 'n':
            print('Here are your stats: ')
            print(f'For player: {name}\nWins: {player.wins}\nLosses: {player.losses}\nPushes: {player.pushes}')
            raise SystemExit
        elif playAgain.lower() == 'y':
            break
        else:
            print('Please enter either "y" for yes or "n" for no.')

