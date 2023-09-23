'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
'''
'''
X,Y≤1000
S = X + Y
P = X * Y
'''

S = int(input("Введите сумму чисел X и Y: "))
P = int(input("Введите произведение чисел X и Y: "))
i = 0

for X in range(S):
    for Y in range(S):
        if S == X + Y and P == X * Y:
            i += 1
            print(f"X = {X}, Y = {Y}.")
if S > 2000 or P > 1000000:
    print("Числа X и Y должны быть НЕ больше 1000!!!")

