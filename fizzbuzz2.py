def fizzbuzz(n):
    if int(n) % 5 == 0 and int(n) % 3 == 0:
        return "fizzbuzz"
    elif int(n) % 5 == 0:
        return "buzz"
    elif int(n) % 3 == 0:
        return "fizz"
    else:
        return n
    
def main():
    n = input("what is your number")
    if n.isdigit():
        print(fizzbuzz(n))
    else:
        print("invalid input")

if __name__ == "__main__":
    main()
    