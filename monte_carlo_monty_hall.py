import random
import pandas as pd

def monty_hall():

    def the_logic(strategy):

        car = random.randrange(0, 3)
        choice = random.randrange(0, 3)

        available = []
        for i in range(3):
            if i != car and i != choice:
                available.append(i)

        eliminated = random.choice(available)

        remaining = []
        for i in range(3):
            if i != eliminated and i != choice:
                remaining.append(i)

        if strategy == "switch":
            final_answer = remaining[0]
        else:
            final_answer = choice

        return final_answer == car

    def simulate(n=100_000):
        results = []
        for tactic in ["stay", "switch"]:
            wins = 0
            for turn in range(n):
                if the_logic(tactic):
                    wins += 1
            results.append({"Strategy": tactic, "Wins": wins, "Trials": n, "Win Rate": (wins / n) * 100})
        df = pd.DataFrame(results)
        print(df)
    
    simulate()

monty_hall()