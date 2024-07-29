def kidsWithCandies(candies, extraCandies):
    max_ = max(candies)
    for i in range(len(candies)):
        print("start", candies[i])
        if (candies[i] + extraCandies) >= max_:
            candies[i] = True
        else:
            candies[i] = False
        print("end", candies[i])


    return candies

print(kidsWithCandies([2,3,5,1,3], 3))
