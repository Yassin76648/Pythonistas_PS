

# def say_number(number):
#     if number < 0 or number > 999_999_999_999:
#         raise ValueError("Out of range")

#     ones = {
#         0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
#         5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
#     }

#     teens = {
#         10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
#         14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
#         17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
#     }

#     tens = {
#         20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
#         60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
#     }

#     scales = ["", "Thousand", "Million", "Billion"]

#     def say_0_to_999(n):
#         words = []

#         if n >= 100:
#             words.append(ones[n // 100])
#             words.append("Hundred")
#             n %= 100

#         if 10 <= n <= 19:
#             words.append(teens[n])
#         else:
#             if n >= 20:
#                 words.append(tens[(n // 10) * 10])
#                 n %= 10
#             if n > 0:
#                 words.append(ones[n])

#         return " ".join(words)

#     if number == 0:
#         return "Zero"

#     result = []
#     scale_index = 0

#     while number > 0:
#         chunk = number % 1000
#         if chunk != 0:
#             words = say_0_to_999(chunk)
#             if scales[scale_index]:
#                 words += " " + scales[scale_index]
#             result.append(words)
#         number //= 1000
#         scale_index += 1

#     return " ".join(reversed(result))


# print(say_number(int(input("Enter number: "))))
            