import random

MAX_LINES = 3
MAX_BET=1000
MIN_BET= 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8 
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all symbols.append(symbol)
    columns = [[],[],[]]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols{:} #copies list rather than reference with slice operator
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid number!")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines will you bet on (1-"+ str(MAX_LINES)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid number of lines")
        else:
            print("Please enter a number!")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number!")
    return amount
    
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Total bet exceeds current balance!(Balance: ${balance} Total bet: ${total_bet})")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}!")
    
    
main()