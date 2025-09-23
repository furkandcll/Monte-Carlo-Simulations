import random
import matplotlib
import matplotlib.pyplot as plt

a = int(input("How much money you have? "))
b = int(input("How much do you want to bet each round? "))
c = int(input("How many rounds will you play? "))
total_simulations = int(input("Total number of simulations: "))

dynamic_threshold_input = input("Would you like to activate dynamic threshold? (TRUE, FALSE): ").strip().lower()
dynamic_threshold = dynamic_threshold_input == "true"

strategy_input = input("Would you like to change the default martingale factor? (TRUE, FALSE) (default: 2): ").strip().lower()
strategy_change = strategy_input == "true"
if strategy_change:
    strategy = float(input("Martingale factor: "))
else:
    strategy = 2

if a <= 0 or b <= 0 or c <= 0:
    print("Please enter positive numbers and try again.")
    exit()

if b > a:
    print("Warning: your bet cannot be bigger than the amount of money you have.")
    exit()

broke_count = 0

ending_balances = []

def roll(losing_streak, winning_streak):
    if dynamic_threshold:
        threshold = 50 + (losing_streak * 2) - (winning_streak * 2)
        threshold = max(0, min(threshold, 100))
    else:
        threshold = 50
    
    return random.randint(1, 100) > threshold
    

def martingale(funds, first_bet, max_rounds):

    global strategy

    losing_streak = 0
    winning_streak = 0
    
    total_amount = funds

    bet = first_bet

    current_round = 1

    previous_result = None

    global broke_count

    Xaxis = []
    Yaxis = []

    while current_round <= max_rounds and total_amount > 0:

        if previous_result == "win":

            bet = first_bet
        
            if roll(losing_streak, winning_streak):
                winning_streak += 1
                losing_streak = 0

                total_amount += bet
                previous_result = "win"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

            else:
                winning_streak = 0
                losing_streak += 1

                total_amount -= bet
                previous_result = "loss"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

        elif previous_result == "loss":
            
            bet = min(bet*strategy, total_amount)

            if roll(losing_streak, winning_streak):
                winning_streak += 1
                losing_streak = 0

                total_amount += bet
                previous_result = "win"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

            else:
                winning_streak = 0
                losing_streak += 1

                total_amount -= bet
                previous_result = "loss"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

        elif previous_result is None:

            if roll(losing_streak, winning_streak):
                winning_streak += 1
                losing_streak = 0

                total_amount += bet
                previous_result = "win"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

            else:
                winning_streak = 0
                losing_streak += 1

                total_amount -= bet
                previous_result = "loss"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)


        current_round += 1

    if total_amount <= 0:
        broke_count += 1

    ending_balances.append(total_amount)

    plt.plot(Xaxis, Yaxis, alpha=0.5, color='red' if total_amount <= 0 else 'green')

for _ in range(total_simulations):
    martingale(a, b, c)

probability_of_ruin = broke_count / total_simulations
print(f"Probability of bankruptcy: {probability_of_ruin*100:.2f}%")

print(f"Average ending balance: {sum(ending_balances)/len(ending_balances):.2f}")

plt.axhline(y=0, color='r', linestyle='--', label='Bankrupt')
plt.legend()

plt.title("Martingale Strategy")
plt.xlabel("Amount of Bets")
plt.ylabel("Total Value in Dollars")

plt.show()