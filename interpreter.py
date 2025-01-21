def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    match y:
        case "+":
            ans = x + z
        case "-":
            ans = x - z
        case "*":
            ans = x * z
        case "/":
            ans = x / z

    print(f"{ans:.1f}")


main()
