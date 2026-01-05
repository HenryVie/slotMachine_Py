import random

symbols = ['7', 'A', 'B', 'C', 'D']

symbol_chance = {
    '7': 5,
    'A': 10,
    'B': 17,
    'C': 20,
    'D': 22
}

payouts = {
    '7': 10,
    'A': 7,
    'B': 5,
    'C': 4,
    'D': 2
}

def betting(balance): # Player betting function
    while True:
        bet = input(f"How much would you like to bet? $ ") # Ask for bet amount

        if bet.isdigit(): # Check if the input is valid
            bet = int(bet)
            if bet > balance:
                print("You can't bet more than your current balance.")
                print(f"Your current balance is ${balance}.")
                continue

            elif bet <= 0:
                print("Please enter a positive amount to bet.")
                continue

            else:
                print(f"You have bet ${bet}. Good luck!")
                return bet
        else:
            print("Please enter a valid number.")
            continue

def money_ctrl(bet, balance): # Control money after betting
    balance -= bet
    return balance

def spin_chance(): # Generate spin chance list
    chance_display = []
    for symbol, chance in symbol_chance.items():
        for _ in range(chance):
            chance_display.append(symbol)
    return chance_display

def spin_reels(chance_display): #Random mechanism for slot machine
    reels = []
    for _ in range(3): # 3 columns
        column = random.choices(chance_display, k=3) # 3 rows
        reels.append(column)
    return reels

def display_reels(reels): # Display the reels to the player
    for row in range(3):
        print(reels[0][row], "|", reels[1][row], "|", reels[2][row])

def all_rows(reels, bet): # Check all rows for wins
    total_win = 0

    for row in range(3):
        middle_symbols = [reels[0][row], reels[1][row], reels[2][row]]

        if middle_symbols.count(middle_symbols[0]) == 3:
            symbol = middle_symbols[0]
            win_amount = bet * payouts[symbol]
            total_win += win_amount

            print(f" Row {row + 1} win: {symbol} | {symbol} | {symbol} (+${win_amount})")

    return total_win

def main():
    balance = 100

    # Welcome message
    print("Welcome to the Terminal Slot Machine!")
    print("Let's start the game.")
    
    # Main game loop
    while True:
        print(f"Your current balance is ${balance}.")

        bet = betting(balance)
        balance = money_ctrl(bet, balance)

        symbol_pool = spin_chance()
        reels = spin_reels(symbol_pool)
        display_reels(reels)

        # Adjust balance based on win/loss
        winnings = all_rows(reels, bet)
        balance += winnings

        # Check the balance after spinning
        if balance > 0:
            print(f"Your current balance is ${balance}.")
            quit_game = input("Would you like to quit the game? (y/n): ").lower()
                
            if quit_game == 'y':
                    print("Thank you for playing!")
                    break

            elif quit_game == 'n':
                continue

            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

        else:
            print("You have run out of money!")
            print("Game over. Thanks for playing!")
            break

main()