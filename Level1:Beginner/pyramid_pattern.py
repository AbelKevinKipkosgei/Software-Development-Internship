def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except:
            print("Invalid input. Please enter a number.")

# Get number of levels from user
levels = get_positive_integer("Enter the number of levels: ")

# Get type of character from user
char_type = input("Enter the type of character: ")

# Get type of pyramid from user
pyramid_type = input("Do you want the pyramid inverted('yes'or'no')?: ").strip().lower()

if pyramid_type == "yes":
    for i in range(levels, 0, -1):
        # Spacing calculation
        print(" " * (levels - i), end="")
        # Character calculation
        print(char_type * (2 * i - 1))
else:
    for i in range(1, levels + 1):
        # Spacing calculation
        print(" " * (levels - i), end="")
        # Character calculation
        print(char_type * (2 * i - 1))