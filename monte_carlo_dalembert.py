import random
import matplotlib
import matplotlib.pyplot as plt

a = int(input("How much money you have? "))
b = int(input("How much do you want to bet each round? "))
c = int(input("How many rounds will you play? "))
total_simulations = int(input("Total number of simulations: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Please enter positive numbers and try again.")
    exit()

if b > a:
    print("Warning: your bet cannot be bigger than the amount of money you have.")
    exit()

broke_count = 0

ending_balances = []

def roll():
    if random.random() > 0.5:
        return True
    else:
        return False
    

def dalembert(funds, first_bet, max_rounds):
    
    total_amount = funds

    bet = first_bet

    current_round = 1

    previous_result = None

    global broke_count

    Xaxis = []
    Yaxis = []

    while current_round <= max_rounds and total_amount > 0:

        if previous_result == "win":
            
            bet = max(first_bet, bet - 1)
        
            if roll():

                total_amount += bet
                previous_result = "win"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

            else:

                total_amount -= bet
                previous_result = "loss"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

        elif previous_result == "loss":

            bet += 1

            if roll():

                total_amount += bet
                previous_result = "win"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

            else:

                total_amount -= bet
                previous_result = "loss"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

        elif previous_result is None:

            if roll():

                total_amount += bet
                previous_result = "win"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

            else:

                total_amount -= bet
                previous_result = "loss"
                Xaxis.append(current_round)
                Yaxis.append(total_amount)

        current_round += 1

    if total_amount <= 0:
        broke_count += 1
    
    ending_balances.append(total_amount)

    plt.plot(Xaxis, Yaxis, alpha=0.5, color='red' if total_amount <= 0 else 'green')

plt.figure(figsize=(10,6))

for _ in range(total_simulations):
    dalembert(a, b, c)

probability_of_ruin = broke_count / total_simulations
print(f"Probability of bankruptcy: {probability_of_ruin*100:.2f}%")

print(f"Average ending balance: {sum(ending_balances)/len(ending_balances):.2f}")

plt.axhline(y=0, color='r', linestyle='--', label='Bankrupt')
plt.legend()

plt.title("D'Alembert Strategy")
plt.xlabel("Amount of Bets")
plt.ylabel("Total Value in Dollars")

plt.show()