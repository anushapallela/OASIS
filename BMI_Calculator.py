def calculate_bmi(weight, height):
    """Calculate BMI using weight (in kg) and height (in meters)."""
    return weight / (height ** 2)

def main():
    print("Welcome to the BMI Calculator!")
    
    # Get user input for weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Output the result
        print(f"Your BMI is: {bmi:.2f}")
        
        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        print(f"Category: {category}")
    
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
