import random
import  sys

username = input("Enter your username : ")
username2 = "Jarvis"
print('')
overs = eval(input("No. of Overs you want to play : "))
print('')
balls = overs * 6

#Function for batting
def batting(runs):
    comp1 = [0, 1, 2, 3, 4, 5, 6]
    values1 = random.choices(comp1, k=balls)
    for a in values1:
        lst3 = [1, 2, 3]
        for m in lst3:
            index = lst3.index(m)
            b = eval(input("Enter your no. : "))
            if 0 <= b <= 6:
                break
            else:

                if index == 0 :
                    print("Please enter the number between or equal to 0 to 6")
                    print("")
                    print("Two chances left")
                elif index == 1 :
                    print("Please enter the number between or equal to 0 to 6")
                    print("")
                    print("One chance left")
                else:
                    print("You didn't enter the number between 0 to 6")
                    print("")
                    print("Zero chances left")
                    print("")
                    print("Rerun")
                    sys.exit()
        print(f'{username2} chose {a}')

        if a == b:
            print("OUT")
            break
        elif 0 <= b <= 6:
            runs += b
            print(f"{runs} runs")
    print(f"Total {runs} runs of {username}")
    return runs

#Function for bowling
def bowling(runs1):
    comp2 = [0, 1, 2, 3, 4, 5, 6]
    values2 = random.choices(comp2, k=balls)
    for c in values2:
        lst4 = [1, 2, 3]
        for n in lst4:
            index1 = lst4.index(n)
            d = eval(input("Enter your no. : "))
            if 0 <= d <= 6:
                break
            else:

                if index1 == 0:
                    print("Please enter the number between or equal to 0 to 6")
                    print("")
                    print("Two chances left")
                elif index1 == 1:
                    print("Please enter the number between or equal to 0 to 6")
                    print("")
                    print("One chance left")
                else:
                    print("You didn't enter the number between 0 to 6")
                    print("")
                    print("Zero chances left")
                    print("")
                    print("Rerun")
                    sys.exit()
        print(f"{username2} chose {c}")

        if c == d:
            print("OUT")
            break
        elif 0 <= d <= 6:
            runs1 += c
            print(f"{runs1} runs")
    print(f"Total {runs1} runs of {username2}")
    return runs1

#Function for comparing runs
def compare():
    if runs > runs1:
        print(f"{username} wins")
    elif runs==runs1:
        print("Match ties")
    else:
        print(f"{username2} wins")

comp3 = [1, 2, 3, 4, 5, 6]
values3 = random.choices(comp3)

lst1 = [1, 2, 3]
for e in lst1:
    index3 = lst1.index(e)
    choose = input("Even (Even, even, E, e) or Odd (Odd, odd, O, o) : ")
    print('')
    if choose == "Even" or choose == "even" or choose == 'E' or choose == 'e':
        f = eval(input("Enter your no. : "))
        print("")
        for i in values3:
            print(f"Computer chose : {i}")
            print("")
            i += f
            if i % 2 == 0:
                print(f"The sum is {i} which even no.")
                print('')
            else:
                print(f"The sum is {i} which is odd no.")
                print('')

        j = i % 2
        if j == 0:
            lst2 = [1, 2, 3]
            for l in lst2:
                index2 = lst2.index(l)
                choose1 = input("Bat or Ball : ")
                print('')
                if choose1 == "Bat" or choose1 == "bat":
                    print(f"{username} chose to {choose1} first")
                    runs = batting(0)
                    print("Your turn to ball")
                    print('')
                    runs1 = bowling(0)
                    print('')
                    compare()
                    print('')
                    break
                elif choose1 == "Ball" or choose1 == "ball":
                    print(f"{username} chose to {choose1} first")
                    runs1 = bowling(0)
                    print('')
                    print("Your turn to bat")
                    print('')
                    runs = batting(0)
                    print('')
                    compare()
                    print('')
                    break
                else:
                    if index2 == 0:
                        print("Please enter bat or ball")
                        print("")
                        print("Two chances left")
                        print("")
                    elif index2 == 1:
                        print("Please enter bat or ball")
                        print("")
                        print("One chance left")
                        print("")
                    else:
                        print("You didn't enter bat or ball")
                        print("")
                        print("Zero chances left")
                        print("")
                        print("Rerun")
                        sys.exit()
                    continue
            break

        else:
            comp4 = ["Bat", "Ball"]
            values4 = random.choices(comp4)
            for k in values4:
                print(f"{username2} chose to {k} first")
                print('')
                if k == "Bat":
                    print("Your turn to ball")
                    print('')
                    runs1 = bowling(0)
                    print('')
                    print("Your turn to bat")
                    print('')
                    runs = batting(0)
                    print('')
                    compare()
                    print('')
                    break
                else:
                    print("Your turn to bat")
                    print('')
                    runs = batting(0)
                    print('')
                    print("Your turn to ball")
                    print('')
                    runs1 = bowling(0)
                    print('')
                    compare()
                    print('')
                    break

    elif choose == "Odd" or choose == "odd" or choose == 'O' or choose == 'o':
        f = eval(input("Enter your no. : "))
        print('')
        for i in values3:
            i += f
            if i % 2 == 0:
                print(f"The sum is {i} which even no.")
                print('')
            else:
                print(f"The sum is {i} which is odd no.")
                print('')

        j = i % 2
        if j != 0:
            lst2 = [1, 2, 3]
            for l in lst2:
                index2 = lst2.index(l)
                choose = input("Bat or Ball : ")
                print("")
                if choose == "Bat" or choose == "bat":
                    print(f"{username} chose to {choose} first")
                    runs = batting(0)
                    print('')
                    print("Your turn to ball")
                    print('')
                    runs1 = bowling(0)
                    print('')
                    compare()
                    print('')
                    break
                elif choose == "Ball" or choose == "ball":
                    print(f"{username} chose to {choose} first")
                    runs1 = bowling(0)
                    print('')
                    print("Your turn to bat")
                    print('')
                    runs = batting(0)
                    print('')
                    compare()
                    print('')
                    break
                else:
                    if index2 == 0:
                        print("Please enter bat or ball")
                        print("")
                        print("Two chances left")
                        print("")
                    elif index2 == 1:
                        print("Please enter bat or ball")
                        print("")
                        print("One chance left")
                        print("")
                    else:
                        print("You didn't enter bat or ball")
                        print("")
                        print("Zero chances left")
                        print("")
                        print("Rerun")
                        sys.exit()
                    continue
            break

        else:
            comp4 = ["Bat", "Ball"]
            values4 = random.choices(comp4)
            for k in values4:
                print(f"{username2} chose to {k} first")
                print('')
                if k == "Bat":
                    print("Your turn to ball")
                    print('')
                    runs1 = bowling(0)
                    print('')
                    print("Your turn to bat")
                    print('')
                    runs = batting(0)
                    print('')
                    compare()
                    print('')
                    break
                else:
                    print("Your turn to bat")
                    print('')
                    runs = batting(0)
                    print('')
                    print("Your turn to ball")
                    print('')
                    runs1 = bowling(0)
                    print('')
                    compare()
                    print('')
                    break

    else:
        if index3 == 0:
            print("Please enter Even or Odd")
            print("")
            print("Two chances left")
            print("")
        elif index3 == 1:
            print("Please enter Even or Odd")
            print("")
            print("One chance left")
            print("")
        else:
            print("You didn't enter Even or Odd")
            print("")
            print("Zero chances left")
            print("")
            print("Rerun")
            sys.exit()
        continue
    break
