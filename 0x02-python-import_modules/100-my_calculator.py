#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    o = sys.argv[2]
    if o != '+' and o != '-' and o != '*' and o != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if 0 == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif 0 == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif 0 == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
