""" generate all combinations of well-formed parentheses """


def generate_parenthesis():
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
    
    findparenthesis(0, 0)
    return ans


if __name__ == '__main__':
    print(generate_parenthesis())
