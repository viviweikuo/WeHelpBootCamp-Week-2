
# 要求一：函式與流程控制
# 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可以假設 max 一定大於 min 且為整數，step 為正整數。

def calculate(min, max, step):

    result = 0

    for i in range(min, max+1, step):
        result = result + i
        
    print(result)

calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2) 


# 要求二：Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量不定的情況。

def avg(data):

    total = 0
    average = 0
    salary_num = 0

    for table in data["employees"]:
        if not table["manager"]:
            total = total + table["salary"]
            salary_num = salary_num + 1
            
    average = total / salary_num

    print(average)

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
        ]
})


# 要求三：
# 完成以下函式，最後能印出程式中註解所描述的結果。

def func(a):
    def func2(b, c):
        print(a + b * c)
    return func2


func(2)(3, 4)
func(5)(1, -5)
func(-3)(2, 9)


# 要求四：
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。

def maxProduct(nums):

    length = len(nums)
    nums_product = 0
    max_num = 0
    nums_Array = []

    for i in range(0, length):
        for j in range(0, length):
            if nums[i] != nums[j]:
                nums_product = nums[i] * nums[j]
                nums_Array.append(nums_product)
    
    max_num = max(nums_Array)

    print(max_num)


maxProduct([5, 20, 2, 6]) #得到 120
maxProduct([10, -20, 0, 3]) #得到 30
maxProduct([10, -20, 0, -3]) #得到 60
maxProduct([-1, 2]) #得到-2
maxProduct([-1, 0, 2]) #得到0
maxProduct([5,-1, -2, 0]) #得到2
maxProduct([-5, -2]) #得到10


# 要求五：
# Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.

def twoSum(nums, target):

    length = len(nums)

    for i in range(0, length):
        for j in range(0, length):
            if nums[i] + nums[j] == target:
                return [i, j]

result = twoSum([2, 11, 7, 15], 9)

print(result) 