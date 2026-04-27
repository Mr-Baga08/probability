import random
import matplotlib.pyplot as plt
import math


def simulate_matching(n, trials=1000):
    matches_found = 0
    original = list(range(n))
    for _ in range(trials):
        shuffled = original[:]
        random.shuffle(shuffled)
        
        # Check if any person got their own card
        has_match = any(original[i] == shuffled[i] for i in range(n))
        if has_match:
            matches_found += 1
    return matches_found / trials

def main():
    x = list(range(2, 61, 2))  # Simulate for even numbers of people from 2 to 60
    trials = 2000

    matching_results = [simulate_matching(n, trials) for n in x]

    plt.scatter(x, matching_results, color='red', label='Simulation (Empirical)')
    plt.axhline(y=1 - (1/2.71828), color='black', linestyle='--', label='Theoretical (1 - 1/e)')
    plt.title(f"Matching Problem Simulation ({trials} trials/point)")
    plt.ylabel("Probability of At Least One Match")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()