# Arlen Griswold
# May 5th 2026



def isPalindromeIterative(user_input):
    i = 0
    j = len(user_input) - 1
    while i < j:
        if user_input[i] != user_input[j]:
            return False
        i += 1
        j -= 1
    return True
                
    

def isPalindromeRecursive(user_input):
    if len(user_input) <= 1:
        return True
    if user_input[0] != user_input[-1]:
        return False
    return isPalindromeRecursive(user_input[1:-1])
    


def main():
    user_input = str(input("Enter a word to check: "))
    output_iter = isPalindromeIterative(user_input)
    output_recu = isPalindromeRecursive(user_input)
    print(f"{output_iter}")
    print(f"{output_recu}")




if __name__ == "__main__":
    main()