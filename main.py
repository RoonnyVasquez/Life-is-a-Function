import math

def calculate_circle_area(pi_val, radius):

    return pi_val * (radius ** 2)

def calculate_total_due(money, tax_rate):

    return money + (money * tax_rate)

def convert_fahrenheit_to_celsius(fahrenheit):

    return (fahrenheit - 32) * (5 / 9)

if __name__ == "__main__":
    # Area of a Circle
    print("--- Area of a Circle ---")
    radius_input = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(math.pi, radius_input)
    print(f"The area of the circle is: {area:.2f}")

    # Total Due with Tax
    print("\n--- Total Due with Tax ---")
    money_input = float(input("Enter the initial amount of money: "))
    tax_rate_str = input("Enter the tax rate (e.g., 6%): ")
    tax_rate_decimal = float(tax_rate_str.strip('%')) / 100
    total_due = calculate_total_due(money_input, tax_rate_decimal)
    print(f"The total amount due is: {total_due:.2f}")

    # Convert Fahrenheit to Celsius
    print("\n--- Convert Fahrenheit to Celsius ---")
    fahrenheit_input = float(input("Enter the temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit_input)
    print(f"The temperature in Celsius is: {celsius:.4f}")