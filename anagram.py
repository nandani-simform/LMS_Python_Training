""" group the anagrams together """


def anagram():
    words = []
    ans = []
    res = {}

    n = int(input('Enter number of words you want: '))

    for i in range(n):
        x = input(f"Enter word {i+1}: ")
        words.append(x)

    for word in words:
        temp = "".join(sorted(word))
        if temp in res:
            res[temp] += [word]
        else:
            res[temp] = [word]

    for i in res.values():
        ans.append(i)

    return ans


if __name__ == '__main__':
    print(anagram())
