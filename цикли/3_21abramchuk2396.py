# https://www.e-olymp.com/uk/submissions/7548306

nums = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred", 200: "two hundred", 300: "three hundred"
    , 400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred"
    , 900: "nine hundred"
}


def eng_num(num):
    if num in nums:
        print(nums[num])
    elif num < 100:
        tenb = (num // 10) * 10
        print(nums[tenb] + ' ' + nums[num - tenb])
    else:
        hundredb = (num // 100) * 100
        tenb = ((num - hundredb) // 10) * 10
        if num - hundredb in nums:
            print(nums[hundredb] + ' ' + nums[num - hundredb])
        elif tenb == 0:
            print(nums[hundredb] + ' ' + nums[num - hundredb - tenb])
        else:
            print(nums[hundredb] + ' ' + nums[tenb] + ' ' + nums[num - hundredb - tenb])


num = int(input())
eng_num(num)