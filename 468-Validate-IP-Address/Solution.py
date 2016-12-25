class Solution(object):
    def checkDecimalism(self, address):
        if len(address) == 0:
            return False
        if address[0] == '0' and len(address) != 1:
            return False
        if not address.isdigit():
            return False
        num = int(address)
        if num >= 0 and num < 256:
            return True
        else:
            return False
    def checkHex(self, num):
        hex_digits = set("0123456789ABCDEFabcdef")
        for char in num:
            if char not in hex_digits:
                return False
        return True
    def checkHexadecimal(self, address):
        if len(address) == 0:
            return False
        if len(address) > 4 or not self.checkHex(address):
            return False
        return True
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        nums = IP.split('.')
        if len(nums) == 4:
            for num in nums:
                if not self.checkDecimalism(num):
                    return "Neither"
            return "IPv4"
        nums = IP.split(':')
        if len(nums) == 8:
            for num in nums:
                if not self.checkHexadecimal(num):
                    return "Neither"
            return "IPv6"
        return "Neither"
        
        
