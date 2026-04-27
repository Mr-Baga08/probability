import random
import matplotlib.pyplot as plt 
import math

def simulate_birthday(num_people, num_trials):
    """
    Simulates the birthday problem by generating random birthdays for a given number of people
    and counting how many times at least two people share a birthday.
    """
    shared_birthday_count = 0
    
    for _ in range(num_trials):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if len(set(birthdays)) < num_people:  # Check for duplicates
            shared_birthday_count += 1
            
    return shared_birthday_count / num_trials


def approximate_birthday_probability(n):
    if n > 365:
        return 1.0
        
    exponent = -(n * (n - 1)) / (2 * 365)
    probability_no_match = math.exp(exponent)
    
    return 1 - probability_no_match

def main():
    x = list(range(2, 61, 2))  # Simulate for even numbers of people from 2 to 60
    trials = 2000

    birthday_results = [simulate_birthday(n, trials) for n in x]
    theoretical_results = [approximate_birthday_probability(n) for n in x]

    plt.scatter(x, birthday_results, color='red', label='Simulation (Empirical)')
    plt.plot(x, theoretical_results, color='blue', linestyle='--', label='Theoretical')
    plt.title(f"Birthday Problem Simulation ({trials} trials/point)")
    plt.ylabel("Probability of Collision")
    plt.grid(True)
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()