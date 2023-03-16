import random

passwordName = input("Digite o nome da senha desejada:\n>>> ")
    
password = ""
baseWords = "1234567%Abc"
for x in range(12):
    index = random.randint(0, len(baseWords) - 1)
    password = password + baseWords[index]

output = f"{passwordName}: {password}\n"
print(output)

with open("output.txt", "a") as file:
    file.write(output)