import numpy as np
import matplotlib.pyplot as plt

def calculate_transaction_amounts(wealth, transaction_mean, transaction_variance):
    # Generate transaction fractions for pairs of individuals
    transaction_fractions = np.random.normal(transaction_mean, transaction_variance, len(wealth) // 2)
    transaction_fractions = np.clip(transaction_fractions, 0, 1)
    
    # Calculate the wealth of the less wealthy individuals in each pair
    first_half = wealth[:len(wealth) // 2]
    second_half = wealth[len(wealth) // 2:]
    wealth_pairs = np.minimum(first_half, second_half)
    
    # Calculate transaction amounts for each pair
    transaction_amounts = wealth_pairs * transaction_fractions
    
    # Create a full length array with transaction amounts
    full_transaction_amounts = np.zeros_like(wealth)
    full_transaction_amounts[:len(wealth) // 2] = transaction_amounts
    full_transaction_amounts[len(wealth) // 2:] = -transaction_amounts
    
    return full_transaction_amounts

def simulate_wealth_distribution(population_size, initial_capital, time_steps, transaction_mean, transaction_variance):
    # Initialize the population with equal wealth
    wealth = np.full(population_size, initial_capital)
    
    for _ in range(time_steps):
        # Permute the population (shuffle the entire wealth array)
        np.random.shuffle(wealth)
        
        # Calculate transaction amounts for the pairs
        transaction_amounts = calculate_transaction_amounts(wealth, transaction_mean, transaction_variance)
        
        # Apply transactions to the wealth array
        wealth += transaction_amounts
    
    return wealth

def plot_wealth_distribution(wealth, bins=50):
    plt.hist(wealth, bins=bins, edgecolor='black')
    plt.xlabel('Wealth')
    plt.ylabel('Number of People')
    plt.title('Wealth Distribution')
    plt.show()

# Parameters
population_size = 1000
initial_capital = 1000.0  # Initial capital set to float
time_steps = 100  # Reduced time steps for quicker iterations
transaction_mean = 0.1  # Mean of the transaction fraction
transaction_variance = 0.05  # Variance of the transaction fraction

# Run simulation
final_wealth = simulate_wealth_distribution(population_size, initial_capital, time_steps, transaction_mean, transaction_variance)

# Plot the final wealth distribution
plot_wealth_distribution(final_wealth)
