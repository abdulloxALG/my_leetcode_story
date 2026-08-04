n = int(input("Talabalar soni: "))


talabalar = []


for i in range(n):
    ism = input(f"{i+1}-talaba ismi: ")
    ball = int(input(f"{ism} balli: "))
    talabalar.append([ism, ball])

for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if talabalar[j][1] > talabalar[max_index][1]:
            max_index = j
    talabalar[i], talabalar[max_index] = talabalar[max_index], talabalar[i]

print("Talabalar Reytingi")

for i in range(n):
    print(f"{i+1}. {talabalar[i][0]} - {talabalar[i][1]} ball")

print("\nEng yuqori ball:")
print(f"{talabalar[0][0]} - {talabalar[0][1]} ball")

print("Eng past ball:")
print(f"{talabalar[-1][0]} - {talabalar[-1][1]} ball")