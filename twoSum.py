# Arlen Griswold
# May 5th 2026



def twoSumLoops(numbers, target):
    # https://interviewing.io/questions/two-sum
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return(i, j)
            

def twoSumDict(numbers, target):
    # https://interviewing.io/questions/two-sum
    numToIndex = {}
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement in numToIndex:
            return numToIndex[complement], i
        numToIndex[numbers[i]] = i


def twoSumLoopsAll(numbers, target):
    combos = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                combos.append([i, j])
    return(combos)



def twoSumDictAll(numbers, target):
    combos = []
    d = {}

    for i in range(len(numbers)):
        complement = target - numbers[i]


        if complement in d:
            for stored_index in d[complement]:
                combos.append([stored_index, i])
        
        if numbers[i] in d:
            d[numbers[i]].append(i)
        else:
            d[numbers[i]] = [i]

    return combos


     

def main():
    numbers = [4, 5, 8, 11, 17]
    target = 15
    result = twoSumLoops(numbers, target)
    result_dict = twoSumDict(numbers, target)
    result_LoopsAll = twoSumLoopsAll(numbers, target)
    result_SumDictAll = twoSumDictAll(numbers, target)
    print(f"The two indices are {result} from twoSumLoops()")
    print(f"The two indices are {result_dict} from twoSumDict()")
    print(f"The possible pairs are {result_LoopsAll}")
    print(f"the possible paris are {result_SumDictAll}")



if __name__ == "__main__":
    main()

