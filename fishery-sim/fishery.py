pop = 500
r = 0.3
K = 1000
total1 = 0
total2 = 0

print("You run a fishing company for 20 years.")
print("Catch as many fish as you can without destroying the fishery.\n")

for year in range(1, 21):
    print("Year", year, "- Fish population:", round(pop))
    harvest1 = int(input("Player 1, how many fish will you catch? "))
    harvest2 = int(input("Player 2, how many fish will you catch? "))

    total1 = total1 + harvest1
    total2 = total2 + harvest2
    pop = pop + r * pop * (1 - pop / K) - harvest1 - harvest2

    if pop <= 0:
        pop = 0
        print("\nThe fishery has collapsed in year", year, "!")
        break

print("\nGame over.")
print("Fish left in the lake:", round(pop))
print("Player 1 total:", total1)
print("Player 2 total:", total2)

if total1 > total2:
    print("Player 1 wins!")
elif total2 > total1:
    print("Player 2 wins!")
else:
    print("It's a tie!")