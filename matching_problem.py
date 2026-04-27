import math
import matplotlib.pyplot as plt

def exact_no_match_prob(n):
    """
    Calculates the probability of NO matches (Derangements) 
    using the Inclusion-Exclusion series.
    """
    prob = 0
    for k in range(n + 1):
        # This is the Taylor series expansion for e^-1
        prob += ((-1)**k) / math.factorial(k)
    return prob

def approximate_no_match_prob(n):
    # As n -> infinity, the probability of no matches is 1/e
    return math.exp(-1)

def main():
    x = list(range(1, 101)) # Reduced to 100 for visual clarity; n > 100 is identical
    
    y_exact_match = []
    y_approx_match = []
    absolute_errors = []
    relative_errors = []

    for n in x:
        # P(No one wins)
        exact_no = exact_no_match_prob(n)
        approx_no = approximate_no_match_prob(n)
        
        # P(At least one person wins)
        exact_match = 1.0 - exact_no
        approx_match = 1.0 - approx_no
        
        # Errors
        abs_err = abs(exact_match - approx_match)
        # Use a tiny epsilon to prevent division by zero
        rel_err = abs_err / exact_match if exact_match > 0 else 0

        y_exact_match.append(exact_match)
        y_approx_match.append(approx_match)
        absolute_errors.append(abs_err)
        relative_errors.append(rel_err)

    # Plotting OUTSIDE the loop
    fig, axis = plt.subplots(3, 1, figsize=(10, 12))
    
    # Match Probability
    axis[0].plot(x, y_exact_match, label='Exact (Inclusion-Exclusion)')
    axis[0].plot(x, y_approx_match, label='Approx (1 - 1/e)', linestyle='--')
    axis[0].set_title('Probability that AT LEAST ONE person wins')
    axis[0].legend()
    axis[0].grid(True)

    # Absolute Error
    axis[1].plot(x, absolute_errors, color='red')
    axis[1].set_title('Absolute Error')
    axis[1].grid(True)

    # Relative Error
    axis[2].plot(x, relative_errors, color='orange')
    axis[2].set_title('Relative Error')
    axis[2].set_yscale('log') # Error drops so fast we need a log scale
    axis[2].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()