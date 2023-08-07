""" group the anagrams together """


def anagram():
   
    """
        Raises:
            ValueError: in event of invalid input number
        Returns:
            None
    """
    words = []
    ans = []
    res = {}

    try:
        n = int(input('Enter number of words you want: '))
    
        """
            Raises:
                ValueError: in event of invalid input string
            Returns:
                list: ans
        """

        for i in range(n):
            x = str(input(f"Enter word {i+1}: "))
            try:
                if x.isalpha():
                    words.append(x)
                else:
                    raise Exception()
               
            except :
                print("Error: value must be string")
                return

        for word in words:
            temp = "".join(sorted(word))
            if temp in res:
                res[temp] += [word]
            else:
                res[temp] = [word]

        for i in res.values():
            ans.append(i)

        return ans
    
    except ValueError:
        print("Error: value must be an integer")
        return

if __name__ == '__main__':
    print(anagram())
