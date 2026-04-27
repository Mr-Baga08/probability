# The Birthday Problem: What is the probability that in a group of n people, at least two people share a birthday?
# Assuming there are 365 days in a year and each person's birthday is equally likely to be.


"""
=============================================================================
DERIVATION: TAYLOR SERIES APPROXIMATION FOR THE BIRTHDAY PROBLEM
=============================================================================

STEP 1: THE EXACT DISCRETE MODEL
The exact probability that NO ONE shares a birthday in a group of n people 
is a discrete chain of multiplying fractions:
P(No Match) = (365/365) * (364/365) * (363/365) * ... * ((365 - n + 1)/365)

By dividing each term individually, we can rewrite this as:
P(No Match) = 1 * (1 - 1/365) * (1 - 2/365) * ... * (1 - (n-1)/365)

STEP 2: THE TAYLOR SERIES APPROXIMATION
The Taylor series expansion for the exponential function e^x is:
e^x = 1 + x + (x^2)/2! + (x^3)/3! + ...

When x is a very small number (close to zero), x^2 and x^3 become 
negligibly tiny. We can drop the higher-order terms for a first-order 
approximation:
e^x ≈ 1 + x  (for small x)

STEP 3: MAPPING THE APPROXIMATION
In our discrete model, the fraction (k / 365) is a very small number.
If we set x = -k/365, it perfectly matches our first-order approximation:
e^(-k/365) ≈ 1 - (k/365)

STEP 4: THE EXPONENTIAL COMPRESSION
We replace every single discrete (1 - fraction) term with its continuous
exponential equivalent:
P(No Match) ≈ e^(-1/365) * e^(-2/365) * e^(-3/365) * ... * e^(-(n-1)/365)

When multiplying variables with the same base (e), we simply add the exponents:
P(No Match) ≈ e^( -1/365 - 2/365 - 3/365 - ... - (n-1)/365 )

STEP 5: SOLVING THE EXPONENT SUM
Let's factor out the common denominator (-1/365) from the exponent:
Exponent = (-1/365) * (1 + 2 + 3 + ... + n-1)

The sum of an arithmetic progression from 1 to K is: K(K + 1) / 2
Since our sequence ends at (n - 1), the sum is: (n - 1)(n) / 2
Sum = n(n - 1) / 2

Substitute this sum back into the factored exponent:
Exponent = (-1/365) * [ n(n - 1) / 2 ]
Exponent = -n(n - 1) / (2 * 365)

FINAL RESULT:
Dropping the solved exponent back onto our base 'e':
P(No Match) ≈ e^( -n(n - 1) / (2 * 365) )

Therefore, the probability that a match DOES occur is 1 minus that result:
P(Match) ≈ 1 - e^( -n(n - 1) / (2 * 365) )
=============================================================================
"""

"""
=============================================================================
ANALYSIS: THE DIVERGENCE OF ERROR (ABSOLUTE VS. RELATIVE)
=============================================================================

1. THE SQUASH EFFECT (Absolute Error - Plot 2)
   - Why the 'Hill'? Initially, as 'n' grows, the gap between the linear 
     approximation (1-x) and the exponential curve (e^-x) widens.
   - The Peak: Around n=35, the Taylor series is 'most wrong' on a 0.0 to 1.0 
     visual scale, with an absolute difference of approx 0.01 (1%).
   - The Decay: Because both functions are forced toward a logical 'rail' 
     of 1.0 (Certainty), the raw distance between them must eventually 
     shrink back to zero. This is a visual illusion—not a sign of accuracy.

2. THE SYSTEM FRACTURE (Relative Error - Plot 3)
   - Why the 'Rocket'? Relative error focuses on the 'No-Match' probability, 
     which is shrinking toward an absolute floor of zero.
   - The Breakdown: The Exact probability (P_exact_no) vanishes significantly 
     faster than the Taylor Approximation (P_approx_no). 
   - At n=365:
     * P_exact_no ≈ 1.4 x 10^-157 (Ultra-microscopic)
     * P_approx_no ≈ 2.7 x 10^-80 (Comparatively massive)
   - Result: The approximation overestimates the remaining probability by 
     ~77 orders of magnitude, causing the relative error to hit 10^80%.

FIRST PRINCIPLES LESSON:
The Taylor approximation e^-x ≈ 1-x is a LOCAL approximation (valid near x=0). 
In a system where we multiply terms (compounding), the higher-order terms 
we discarded (x^2, x^3...) create a 'mathematical debt.' By n=365, this 
compounded debt results in a galaxy-sized discrepancy hidden behind a 
saturated macroscopic signal.
=============================================================================
"""


import math
import matplotlib.pyplot as plt 

def exact_no_match_prob(n):
    """
    Calculates the exact probability of NO shared birthdays.
    Uses a simple loop instead of recursion to prevent stack overflows at n=365.
    """
    if n > 365:
        return 0.0
        
    probability = 1.0
    for i in range(n):
        probability *= (365 - i) / 365
        
    return probability

def recursive(n):
    if n == 1:
        return 1.0
    else:
        return (365 - n + 1) / 365 * recursive(n - 1)

def birthday_probability(n):
    if n > 365:
        return 1.0  # More people than days means a guaranteed match

    probability_no_match = recursive(n)

    return 1 - probability_no_match

# The approximation for large n is given by: P(n) ≈ 1 - e^(-n(n-1)/(2*365))
# as 1 * (1 - 1/365)*(1 - 2/365) * ... can be approximated by e^{-n(n-1)/(2*365)} for large n.
# Taylor expansion of e^-x around x=0 is 1 - x which can be used to derive the approximation.


def birthday_approximation(n):
    if n > 365:
        return 1.0
        
    # Calculate the exponent: -n(n-1) / (2 * 365)
    exponent = -(n * (n - 1)) / (2 * 365)
    
    # Calculate e^exponent
    probability_no_match = math.exp(exponent)
    
    return probability_no_match

def main():
    # Let's push n all the way to 150 to see the math fully fracture
    x = list(range(1, 366))
    
    y_exact_match = []
    y_approx_match = []
    absolute_errors = []
    relative_errors = []

    for n in x:
        # 1. Get the base No-Match probabilities
        exact_no = exact_no_match_prob(n)
        approx_no = birthday_approximation(n)
        
        # 2. Calculate Match probabilities
        exact_match = 1.0 - exact_no
        approx_match = 1.0 - approx_no
        
        # 3. Calculate Errors
        abs_err = abs(exact_match - approx_match)
        
        if exact_no > 0:
            rel_err = (abs(exact_no - approx_no) / exact_no) * 100
        else:
            rel_err = 0
            
        # Store data
        y_exact_match.append(exact_match)
        y_approx_match.append(approx_match)
        absolute_errors.append(abs_err)
        relative_errors.append(rel_err)

    # Build the dashboard
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    
    # --- PLOT 1: The Probabilities (The Illusion) ---
    axs[0].plot(x, y_exact_match, label='Exact', color='blue', linewidth=2)
    axs[0].plot(x, y_approx_match, label='Approx', color='orange', linestyle='--', linewidth=2)
    axs[0].set_title('1. Match Probability (The Illusion: They look identical)')
    axs[0].set_ylabel('Probability')
    axs[0].grid(True)
    axs[0].legend()

    # --- PLOT 2: Absolute Error (The Squash Effect) ---
    axs[1].plot(x, absolute_errors, color='red', linewidth=2)
    axs[1].set_title('2. Absolute Error (The difference between the two lines above)')
    axs[1].set_ylabel('Raw Difference')
    axs[1].grid(True)

    # --- PLOT 3: Relative Error (The Mathematical Truth) ---
    axs[2].plot(x, relative_errors, color='purple', linewidth=2)
    axs[2].set_title('3. Relative Error of No-Match (The math fracturing)')
    axs[2].set_xlabel('Number of People (n)')
    axs[2].set_ylabel('Error Percentage (%)')
    # Using a logarithmic scale here because the error explodes into the millions
    axs[2].set_yscale('log') 
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()