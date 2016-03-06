class Player(object):
    
    def __init__(self, name, bank):
        self.name = name
        self.bank = round(bank, 2)

    # Calculates new bank total after a win/loss.
    def new_bank(self, change):
        self.bank += change
    
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
