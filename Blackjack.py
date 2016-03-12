suits = ['H', 'D', 'S', 'C']
# Create dictionary of the values of each rank.  Issue of Ace being 11 will be dealt with later.
values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

class Player(object):
    
    def __init__(self, name, bank):
        self.name = name
        self.bank = round(bank, 2)

    # Calculates new bank total after a win/loss.
    def new_bank(self, change):
        self.bank += change

class Card(object):
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + self.suit


class Hand(object):

    def __init__(self):
        # Set initial hand to be an empty list with a value of zero.
        self.cards = []
        self.value = 0
        # Will change to true if an ace is added to the hand.
        self.ace = False

    def add_card(self, newcard):
        self.cards.append(newcard)
        if newcard.rank == 'A':
            self.ace = True
            
    def calculate_value(self):
        self.value = 0
        for card in self.cards:
            self.value += values[card.rank]
        # If there is an ace in the hand and making it count as 11 does not bust the hand, make it 11.
        if self.ace == True and (self.value + 10) <= 21:
            self.value += 10
            
    def __str__(self):
        return ' '.join(map(str, self.cards))
    
name = input('What is your name? ')
# Keep asking until a numeric bank value is entered.
while True:
    try:
        bank = float(input('How much money do you have to start? '))
    except ValueError:
        print('Initial bank must be a positive number. Please try again.')
        continue
    else:
        break
    
#Keep asking until a positive bank value is entered
while bank <= 0:
    print('Initial bank must be a positive number. Please try again.')
    bank = float(input('How much money do you have to start? '))

# Initialize player object and remove temporary variables.
player = Player(name, bank)
del name, bank

# Ask player for bet until a numeric value is entered.
while True:
    try:
        current_bet = float(input('How much would you like to bet? '))
    except ValueError:
        print('Invalid bet amount. Please try again.')
        continue
    else:
        break

# Make sure bet is positive and less than current bank value.    
while current_bet > player.bank or current_bet <= 0:
    current_bet = float(input('You currently have $' +
                              str('%.2f' %player.bank) +
                              ' in your bank. Please enter a positive value less than this amount: '))
