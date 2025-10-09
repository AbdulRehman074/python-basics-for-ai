# --- Program to Calculate Sum and Average of 5 Numbers ---

# Configuration
NUMBER_COUNT = 5
total_sum = 0.0

print(f"--- Enter {NUMBER_COUNT} Numbers ---")

# Use a for loop to iterate exactly 5 times
for i in range(NUMBER_COUNT):
    
    # Input handling loop to ensure a valid number is entered
    while True:
        try:
            # Prompt user for the Nth number (i+1)
            prompt = f"Enter number {i + 1} of {NUMBER_COUNT}: "
            user_input = input(prompt)
            
            # Convert input to a float (to handle decimals)
            number = float(user_input)
            
            # Valid input received, exit the inner loop
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    
    # Add the valid number to the running total
    total_sum += number

# --- Calculations ---
# Calculate the average
average = total_sum / NUMBER_COUNT

# --- Output Results ---
print("\n--- Results ---")
print(f"The Total Sum is: {total_sum:.2f}")
print(f"The Average is: {average:.2f}")
print("---------------")
