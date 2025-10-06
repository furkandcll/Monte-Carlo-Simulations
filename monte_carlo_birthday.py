import random

def monte_carlo_birthdays_least(sample=50, simulation=10_000):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def birthday_func():
        birthdays = []
        for birth in range(sample):
            the_month = random.randrange(1, 13)
            person = {"Month": the_month, "Day": random.randrange(1,months[the_month] + 1)}
            birthdays.append(person)
        return birthdays


    def to_detect(birthdays):
        for i in range(len(birthdays)):
            for j in range(i + 1, len(birthdays)):
                if birthdays[i] == birthdays[j]:
                    return True
        return False

    same = 0
    for _ in range(simulation):
        birthdays = birthday_func()
        if to_detect(birthdays):
            same += 1
    
    percentage = same / simulation

    print(f"The probability that at least two people share a birthday in a group of {sample} people is {percentage * 100:.2f}%")

monte_carlo_birthdays_least()

#---------------------------------------------------------------------------------------------------

# What are the chances of all having unique birthdays in a sample?

def monte_carlo_unique_birthdays(sample=365, simulation=10_000, leap_year=False):
    days_in_year = 366 if leap_year else 365

    def birthday_func():
        birthdays = []
        for people in range(sample):
            birthdays.append(random.randrange(1, days_in_year + 1))
        return birthdays

    def to_detect(birthdays):
        return len(birthdays) == len(set(birthdays))

    perfect = 0
    for _ in range(simulation):
        birthdays = birthday_func()
        if to_detect(birthdays):
            perfect += 1
    
    percentage = perfect / simulation

    print(f"The probability that a group of {sample} people has all unique birthdays is {percentage * 100:.2f}%")

monte_carlo_unique_birthdays()

#---------------------------------------------------------------------------------------------------

# What are the chances of having all the possible birthdays in a year?

def monte_carlo_all_birthdays(sample=2000, simulation=10_000, leap_year=False):
    days_in_year = 366 if leap_year else 365

    def birthday_func():
        birthdays = []
        for people in range(sample):
            birthdays.append(random.randrange(1, days_in_year + 1))
        return birthdays

    def to_detect(birthdays):
        return len(set(birthdays)) >= 365

    all_in = 0
    for _ in range(simulation):
        birthdays = birthday_func()
        if to_detect(birthdays):
            all_in += 1
    
    percentage = all_in / simulation

    print(f"The probability that a group of {sample} people has all possible birthdays in a year is {percentage * 100:.2f}%")

monte_carlo_all_birthdays()
