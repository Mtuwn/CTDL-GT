class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        StringArray = []
        
        for symbol, value in  dictionary:
            while Value <= num:
                StringArray.append(Symbol)
                num -= Value
        
        print(StringArray)


number = input("Nhap 1 so: ")
test = Solution()
test.intToRoman(number)