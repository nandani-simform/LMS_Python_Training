""" generate all combinations of well-formed parentheses """


def generate_parenthesis():
    try:
        n = int(input("Enter number: "))
        ans = []
        currentstack = []

        def findparenthesis(open, close):
            if open == close == n:
                ans.append("".join(currentstack))
                return

            if open < n:
                currentstack.append("(")
                findparenthesis(open+1, close)
                currentstack.pop()

            if close < open:
                currentstack.append(")")
                findparenthesis(open, close+1)
                currentstack.pop()        

        """
            Parameters:
                open (int): left counter
                close (int): right counter
            Raises:
                ValueError: in event of invalid input number
            Returns:
                None
        """
    
        findparenthesis(0, 0)
        return ans
    
    except ValueError:
        print("Only Integer are allowed")



if __name__ == '__main__':
    print(generate_parenthesis())
