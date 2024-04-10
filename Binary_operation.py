from decimal import Decimal

class Binary:
    def __init__(self,num1):
        if num1[0] not in ['+', '-']:
            num1.insert(0,"+")
        self.num = num1
    def __iter__(self):
        return iter(self.num)
    def length(self):
        return len(self.num)
    def __getitem__(self,index):
        return self.num[index]
    def change_item(self,index,value):
        self.num[index] = value
    def pop(self, index):
        return self.num.pop(index)
    def insert(self , index, value):
        self.num.insert(index,value)
    def __lt__(self,other):
        num1 = int(''.join(map(str,self.num)))
        num2 = int(''.join(map(str,other.num)))
        return num1 < num2
    def __gt__(self,other):
        num1 = int(''.join(map(str,self.num)))
        num2 = int(''.join(map(str,other.num)))
        return num1 > num2
    def __add__(self,other):
        sign = [self.num[0],other.num[0]]
        num1 = self.num
        num2 = other.num
        num1.pop(0)
        num2.pop(0)
        diff = len(num1)-len(num2)
        if diff > 0:
            for _ in range(diff):
                num2.insert(0,0)
        elif diff < 0:
            for _ in range(diff*-1):
                num1.insert(0,0)
        ans = []
        for i in range((len(num1)-1),-1,-1):
            term1 = num1[i]+num2[i]
            carry = 0
            if term1 == 2:
                term1 = 0
                carry = 1
                num1[i-1] = num1[i-1] + 1
            elif term1 == 3:
                term1 = 1
                carry = 1
                num1[i-1] = num1[i-1] + 1
            ans.insert(0,term1)
        if carry == 1:
            ans.insert(0,carry)
        a=0
        for i in num1:
            if i > num2[a]:
                ans.insert(0,sign[0])
                break
            elif num2[a] > i:
                ans.insert(0,sign[1])

                break
            if self.num == other.num:
                ans.insert(0,sign[0])
                break 
            a=a+1
        return Binary(ans)
    def __sub__(self, other):
        num1 = self.num
        num2 = other.num
        int_num1 = int(''.join(map(str, num1[1:])))
        int_num2 = int(''.join(map(str, num2[1:])))
        if self.num == other.num:
            return "0000"
        diff = len(num1)-len(num2)
        if diff > 0:
            for _ in range(diff):
                num2.insert(1,0)
            z = len(num1)
        elif diff < 0:
            for _ in range(diff*-1):
                num1.insert(1,0)
            z = len(num2)
        else:
            z = len(num2)
        
        negative = Binary.two_complement(num2)
        ans = Binary(num1)+negative

        num2.pop(0)
        if ans.length() > z:
            ans.pop(1)

        if int_num1 < int_num2:
            ans = Binary.two_complement(ans)

            ans.change_item(0,"-")
        return ans
    def __str__(self) :
        return(''.join(map(str,self.num)))
    def two_complement(value):
        neg_other = [1 if i == 0 else 0 for i in value[1:]]
        neg_other.insert(0,"+")
        neg_other = Binary(neg_other) + Binary(["+", 1])
        return neg_other
    @classmethod
    def power(cls,a):
        p = 1
        for _ in range(a):
            p = p*2
        return p
    @classmethod
    def convert_to_binary(cls,num):
        num=int(num)
        if num < 0:
            sign = -1
            num = num*-1
        else:
            sign = 1
        ones = []
        BiNum = []
        while True:
            for i in range(1000000000000000):
                val = Binary.power(i)
                if val > num:
                    ones.append(i-1)
                    num = num - Binary.power(i-1)
                    break
            if num == 0:
                break
        for i in range(ones[0] + 1):
            BiNum.append(0)

        for i in ones:
            ind = len(BiNum) - 1 - i
            BiNum[ind] = 1
        
        if sign == -1:
            BiNum.insert(0,"-")
        else:
            BiNum.insert(0,"+")
        return Binary(BiNum)
    @classmethod
    def convert_to_int(cls,num):
        num=str(num)
        length = len(num) - 1
        index = 0
        integer = []
        for i in range(length,-1,-1):
            if num[index] == '1':
                integer.append(Binary.power(i))
            index = index + 1
        return (sum(integer))

def main():
    cond = True
    while cond:
        try:
            num1 = Binary.convert_to_binary(Decimal(int(input("Enter first number: "))))
            cond = False
        except ValueError:
            print("Invalid Input!")
    cond = True
    while cond:
        try:
            num2 = Binary.convert_to_binary(Decimal(int(input("Enter second Number: "))))
            cond = False
        except ValueError:
            print("Invalid Input")
    while True:        
        operation = input("1) Addition\n2) Substraction\nWhat Arithmetic operation do you want to perform: ")
        if operation not in ["1","2"]:
            print("You can choose only between options 1 and 2!")
        else:
            break
    if operation == "1":
        num3 = num1 + num2
        print(f"Binary sum is {num3}")
    elif operation == "2":
        num3 = num1 - num2
        print(f"Binary difference is {num3}")

if __name__=="__main__":
    main()
