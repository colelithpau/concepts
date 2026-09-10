"""
Programming Activity: Factorial and Fibonacci Series Using Python
Objective: To apply Recursion

This program displays a menu-driven interface allowing the user to:
1. Compute the factorial of a positive integer (using recursion).
2. Generate a Fibonacci series up to a specified number of terms (using recursion).

"""

def factorial_recursive(n: int) -> int:
    """
    Compute the factorial of n using recursion.
    factorial(n) = n * factorial(n-1), with factorial(0) = factorial(1) = 1.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_notation_string(n: int) -> str:
    """
    Return a string showing the factorial notation, e.g. '5! = 5 × 4 × 3 × 2 × 1'.
    """
    if n == 0 or n == 1:
        return f"{n}! = {n}"
    terms = " × ".join(str(i) for i in range(n, 0, -1))
        return f"{n}! = {terms}"


def fibonacci_recursive(n: int, memo: dict | None = None) -> int:
    """
    Compute the n-th Fibonacci number using recursion with memoization.
    fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2) for n >= 2.
    Memoization avoids exponential recomputation.
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
        return memo[n]


def generate_fibonacci_series(terms: int) -> list[int]:
    """
    Generate a list containing the first 'terms' Fibonacci numbers.
    """
    return [fibonacci_recursive(i) for i in range(terms)]


def display_menu() -> None:
    """Display the main menu."""
    print("===========================")
    print("MAIN MENU")
    print("===========================")
    print("1. Factorial")
    print("2. Fibonacci Series")
    print("===========================")


def get_positive_int(prompt: str) -> int:
    """
    Prompt the user for a positive integer.
    Repeats until a valid positive integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer (greater than 0).")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def main() -> None:
    """Main program logic: menu, input validation, and output."""
    display_menu()

    # Get and validate menu choice
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice not in (1, 2):
                print("Invalid choice! Please select 1 or 2 only.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    if choice == 1:
        # Factorial option
        n = get_positive_int("Enter a positive integer: ")
        result = factorial_recursive(n)
        notation = factorial_notation_string(n)

        print("\nFactorial Notation:\n")
        print(notation)
        print(f"Answer: {result}")

    elif choice == 2:
        # Fibonacci option
        terms = get_positive_int("Enter the number of terms: ")
        series = generate_fibonacci_series(terms)

        print("Fibonacci Series:")
        print(" ".join(str(x) for x in series))


if __name__ == "__main__":
    main()
