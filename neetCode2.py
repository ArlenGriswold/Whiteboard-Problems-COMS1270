# Arlen Griswold
# Lab 11 - NeetCode: Valid Anagram
# https://neetcode.io/problems/is-anagram

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS = {}
    countT = {}
    
    for i in range(len(s)):
        # increment count of s[i] in countS
        # increment count of t[i] in countT
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1
    
    return countS == countT


def main():
    print(isAnagram("racecar", "carrace"))   # True
    print(isAnagram("jar", "jam"))           # False
    print(isAnagram("anagram", "nagaram"))   # True
    print(isAnagram("rat", "car"))           # False


if __name__ == "__main__":
    main()