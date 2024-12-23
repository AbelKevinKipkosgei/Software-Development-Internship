class Temp_Converter:
    def __init__(self, temperature):
        self.temperature = temperature
    
    def convert_to_celsius(self, temperature):
        return (temperature - 32) * 5/9
    
    def convert_to_fahrenheit(self, temperature):
        return (temperature * 9/5) + 32

# Menu function
def display_menu():
    print("\nTemperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

# Main function
def main():
    temp_converter = Temp_Converter(0)
    while True:
        display_menu()

        # Get input from user
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == "1":
            temperature = float(input("Enter temperature in Celsius: "))
            print(f"{temperature}°C is equal to {temp_converter.convert_to_fahrenheit(temperature)} Fahrenheit")
        elif choice == "2":
            temperature = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temperature}°F is equal to {temp_converter.convert_to_celsius(temperature)} Degrees Celsius")
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
