
nums = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']

with open("LOTPAnthologyUrduScriptFinal.txt", "w+", encoding="utf-8") as f:
    currNum = ""
    for num1 in nums:
        currNum = num1
        for num2 in nums:
            currNum += num2
            f.write(currNum)
            f.write("\n")
            currNum = num1
