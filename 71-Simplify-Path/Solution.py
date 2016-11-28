class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        paths = path.split("/")
        for i in range(len(paths)):
            word = paths[i]
            if word == "." or word == "":
                continue
            elif word == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(word)
        return "/"+"/".join(stack)
