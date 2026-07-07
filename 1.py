#leetcode
#problem 9): is it palindrome or not.
class Student:
    def isPalindrome(self,x:int)->bool:
        if str(x)==str(x)[::-1]:
            return True
        return False
s=Student()
print(s.isPalindrome(121))    