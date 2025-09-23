import random
import matplotlib.pyplot as plt
import numpy as np
import math

function_determiner = input("Define the function you want to integrate (e.g. x**2 + 3*x + 1): f(x) = ")
point_a = float(input("Enter the lower bound a: "))
point_b = float(input("Enter the upper bound b: "))

while True:
    try:
        given_attempt_number = int(input("How many attempts do you want for the Monte Carlo Integral Simulation? "))
        if given_attempt_number <= 0:
            print("Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

allowed_funcs = {
    "np": np,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "exp": np.exp,
    "log": np.log,
    "sqrt": np.sqrt,
    "abs": np.abs
}

def f(x):
     return eval(function_determiner, {"x": x, "__builtins__": None}, allowed_funcs)

def monte_carlo_integral(f, a, b, attempts):
    f_max = max(f(x) for x in np.linspace(a, b, 10000))
    correct_guess = 0
    for _ in range(attempts):
        x = random.uniform(a, b)
        y = random.uniform(0, f_max)
        if y <= f(x):
            correct_guess += 1
    estimated_integral = (correct_guess/attempts) * (b - a) * f_max
    print(f"Definite integral between {a} and {b} is estimated as {estimated_integral}")



monte_carlo_integral(f, point_a, point_b, given_attempt_number)

#------------------------------------------------------------------------

def graph_monte_carlo_integral(f, a, b, attempts):
    f_max = max(f(x) for x in np.linspace(a, b, 10000))
    correct_guess = 0
    
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    for _ in range(attempts):
        x = random.uniform(a, b)
        y = random.uniform(0, f_max)
        if y <= f(x):
            correct_guess += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
        
    estimated_integral = (correct_guess/attempts) * (b - a) * f_max
    print(f"Definite integral between {a} and {b} is estimated as {estimated_integral}")

    plt.figure(figsize=(6, 6))
    xs = np.linspace(a, b, 200)
    ys = [f(x) for x in xs]
    plt.plot(xs, ys, 'k-', label="f(x)")
    plt.scatter(x_inside, y_inside, color="red", s=1, label="Inside the Function")
    plt.scatter(x_outside, y_outside, color="blue", s=1, label="Outside the Function")
    plt.legend()
    plt.show()

graph_monte_carlo_integral(f, point_a, point_b, given_attempt_number)