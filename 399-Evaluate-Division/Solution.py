class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        quotient = collections.defaultdict(dict)
        for (dividend, divisor), val in zip(equations, values):
            quotient[dividend][dividend] = 1.0
            quotient[divisor][divisor] = 1.0
            quotient[dividend][divisor] = val
            quotient[divisor][dividend] = 1 / val
        for k, i, j in itertools.permutations(quotient, 3):
            if k in quotient[i] and j in quotient[k]:
                quotient[i][j] = quotient[i][k] * quotient[k][j]
        return [quotient[dividend].get(divisor, -1.0) for dividend, divisor in queries]
