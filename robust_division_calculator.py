def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Handle division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."

        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # Handles if input is not a number
        return "Error: Please enter numeric values only."
