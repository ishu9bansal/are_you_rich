import numpy as np
import matplotlib.pyplot as plt

def calculate_transaction_amount(amount1, amount2, transaction_mean, transaction_variance):
    # Determine the wealth of the less wealthy person
    less_wealthy_amount = min(amount1, amount2)
    # Calculate the transaction fraction as a random variable from a normal distribution
    transaction_fraction = np.random.normal(transaction_mean, transaction_variance)
    # Ensure the transaction fraction is between 0 and 1
    transaction_fraction = np.clip(transaction_fraction, 0, 1)
    # Calculate the transaction amount
    transaction_amount = less_wealthy_amount * transaction_fraction
    # ChatGPT gave this wrong code which made me crazy, and it gave wrong results
    # Here it is always making the lesser wealthy person as the profitier in the transaction
    # Below is the corrected code
    # # Determine who gives and who receives
    # if amount1 < amount2:
    #     return transaction_amount, -transaction_amount
    # else:
    #     return -transaction_amount, transaction_amount
    return transaction_amount, -transaction_amount

def simulate_wealth_distribution(population_size, initial_capital, time_steps, transaction_mean, transaction_variance):
    # Initialize the population with equal wealth
    wealth = np.full(population_size, initial_capital)
    
    for _ in range(time_steps):
        # Permute the population
        np.random.shuffle(wealth)
        
        # Perform transactions
        for i in range(0, population_size - 1, 2):
            transaction_amount1, transaction_amount2 = calculate_transaction_amount(wealth[i], wealth[i + 1], transaction_mean, transaction_variance)
            wealth[i] += transaction_amount1
            wealth[i + 1] += transaction_amount2
    
    return wealth

def plot_wealth_distribution(wealth, bins=50):
    plt.hist(wealth, bins=bins, edgecolor='black')
    plt.xlabel('Wealth')
    plt.ylabel('Number of People')
    plt.title('Wealth Distribution')
    plt.show()

# Parameters
population_size = 1000
initial_capital = 1000.0
time_steps = 100
transaction_mean = 0.1  # Mean of the transaction fraction
transaction_variance = 0.05  # Variance of the transaction fraction

# Run simulation
final_wealth = simulate_wealth_distribution(population_size, initial_capital, time_steps, transaction_mean, transaction_variance)

# Plot the final wealth distribution
plot_wealth_distribution(final_wealth)
