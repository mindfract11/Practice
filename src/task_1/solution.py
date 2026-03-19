"""
Cosmic Cafe

You are the manager of a space station cafe. An astronaut has arrived and wants to place an order.
Your program must greet the astronaut, record the order details, and print the final bill.

Input

Read the following values from standard input in this exact order:

1. The astronaut name (string)
2. The number of pizza portions ordered (integer)
3. The price of one portion in credits (float)

Output

Print the following lines in this exact order:

Line 1:  a separator of 40 dashes
Line 2:  "Hello, NAME! Welcome to the Cosmic Cafe!"   where NAME is the astronaut name
Line 3:  "Portions ordered: COUNT"                    where COUNT is the integer from input
Line 4:  "Price per portion: PRICE credits"           where PRICE is the float from input
Line 5:  "Total: TOTAL credits"                       where TOTAL is COUNT * PRICE rounded to 2 decimal places
Line 6:  a separator of 40 dashes

Constraints

The astronaut name contains only printable characters and no leading or trailing whitespace.
1 <= COUNT <= 1000
0.01 <= PRICE <= 9999.99
TOTAL must always be printed with exactly 2 digits after the decimal point.

Sample 1

Input:
Julia
3
75.5

Output:
----------------------------------------
Hello, Julia! Welcome to the Cosmic Cafe!
Portions ordered: 3
Price per portion: 75.5 credits
Total: 226.50 credits
----------------------------------------

Sample 2

Input:
Max
2
10.0

Output:
----------------------------------------
Hello, Max! Welcome to the Cosmic Cafe!
Portions ordered: 2
Price per portion: 10.0 credits
Total: 20.00 credits
----------------------------------------

Sample 3

Input:
Oleg
10
9.99

Output:
----------------------------------------
Hello, Oleg! Welcome to the Cosmic Cafe!
Portions ordered: 10
Price per portion: 9.99 credits
Total: 99.90 credits
----------------------------------------


Run the tests with command:

```bash
pytest src/tests/test_task_1.py
```

"""


def main():
    c = input("Enter your name: ")
    b = int(input("Enter your number: "))
    p =  float(input("Enter your price: "))

    print("-"*40)
    print(f"Hello, {c}! Welcome to the Cosmic Cafe!")
    print(f"Portions ordered: {b}")
    print(f"Price per portion: {p}")
    print(f"Total: {round(b*p) }")
    print("-"*40)

    pass


if __name__ == "__main__":
    main()
