print('Welcome to the calculator')


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


def division(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


def print_menu():
    print('1: Add')
    print('2: Multiply')
    print('3: Subtract')
    print('4: Divide')


def main():
    while True:
        try:
            num_1 = float(input('Enter your first number: '))
            num_2 = float(input('Enter your second number: '))
            print_menu()
            choosing_option = input('Pick between 1/2/3/4: ')

            if choosing_option == '1':
                print('Result: ', add(num_1, num_2))
            elif choosing_option == '2':
                print('Result: ', multiply(num_1, num_2))
            elif choosing_option == '3':
                print('Result: ', subtract(num_1, num_2))
            elif choosing_option == '4':
                print('Result: ', division(num_1, num_2))
            else:
                print("Invalid option selected. Please choose between 1, 2, 3, or 4.")

        except ValueError:
            print("Oops! That was not a valid number. Try again...")

        using_again = input('Do you want to use the calculator again? (y/n): ')
        if using_again.lower() == 'n':
            print('Thanks for using the calculator!')
            break


if __name__ == "__main__":
    main()
