# Arlen Griswold



def reverseIterative(user_input):
    word_reversed = ""
    for i in range(len(user_input) - 1, -1, -1):
        word_reversed += user_input[i]
    return word_reversed



def reverseRecursive(user_input):
    if len(user_input) <= 1:
        return user_input
    return reverseRecursive(user_input[1:]) + user_input[0]


def main():
    user_input = str(input("Enter a string: "))
    result = reverseIterative(user_input)
    print(f"Word reversed is: {result}")
    result_rec = reverseRecursive(user_input)
    print(f"Word reversed is: {result_rec}")



if __name__ == "__main__":
    main()

