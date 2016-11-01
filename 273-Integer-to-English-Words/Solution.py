class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        hundreds = ['Hundred']
        thousands = ['Thousand', 'Million', 'Billion']
        words = []
        digits = 0
        while num:
            token = num % 1000
            num = num / 1000
            word = ''
            if token > 99:
                word += ones[token / 100] + ' ' + hundreds[0] + ' '
                token = token % 100
            if token > 19:
                word += tens[token / 10 - 2] + ' '
                token = token % 10
            if token > 0:
                word += ones[token] + ' '
            word = word.strip()
            if word:
                word += ' ' + thousands[digits - 1] if digits else ''
                words.append(word)
            digits += 1
        return ' '.join(words[::-1]) or 'Zero'
