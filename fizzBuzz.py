# Arlen Griswold
# May 5th 2026



def fizzbuzzModulus(user_integer):
    # https://www.enjoyalgorithms.com/blog/fizz-buzz-problem
    output = []
    for i in range(1, user_integer + 1):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            output.append("FizzBuzzBazz")
        elif i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0 and i % 7 == 0:
            output.append("FizzBazz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        elif i % 7 == 0:
            output.append("Bazz")
        else:
            output.append(str(i))


        
    return output


def fizzBuzzDict(user_integer):
    output = []
    fizz_buzz = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    for i in range(1, user_integer+1):
        s = ""
        for key in fizz_buzz:
            if i % key == 0:
                s = s + fizz_buzz[key]
        if s == "":
            s = str(i)
        output.append(s)
    
    return output



def main():
    user_integer = int(input("Enter an integer: "))
    user_output = fizzbuzzModulus(user_integer)
    print(f"{user_output}")
    user_output_dictionary = fizzBuzzDict(user_integer)
    print(f"{user_output_dictionary}")




if __name__ == "__main__":
    main()
