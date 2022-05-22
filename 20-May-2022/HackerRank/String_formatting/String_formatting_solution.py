def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(width), octa.rjust(width),
              hexa.rjust(width), binary.rjust(width))
# your code goes here


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
