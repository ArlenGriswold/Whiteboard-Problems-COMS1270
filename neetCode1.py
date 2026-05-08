# Arlen Griswold
# Lab 11 - NeetCode: Contains Duplicate

def hasDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def main():
    test1 = [1, 2, 3, 3]
    test2 = [1, 2, 3, 4]
    test3 = [1]
    print(hasDuplicate(test1))  
    print(hasDuplicate(test2))   
    print(hasDuplicate(test3))   

if __name__ == "__main__":
    main()

