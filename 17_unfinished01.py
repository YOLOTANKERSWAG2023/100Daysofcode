print("LOCAL VERSUS ROCK PAPER SCISSOR")
print("")
victoryusername1 = 0
victoryusername2 = 0
templatechoice = str("""
1. Rock
2. Paper
3. Scissor
""")
scoreusername1 = 0
scoreusername2 = 0
username1 = input("What's your name player 1?: ")
print("")
username2 = input("And player 2's name?:")
print("")
print(username1, "you are player 1,", username2, "you are player 2")
print("")print("LOCAL VERSUS ROCK PAPER SCISSOR")
print("")
victoryusername1 = 0
victoryusername2 = 0
templatechoice = str("""
1. Rock
2. Paper
3. Scissor
""")
scoreusername1 = 0
scoreusername2 = 0
username1 = input("What's your name player 1?: ")
print("")
username2 = input("And player 2's name?:")
print("")
print(username1, "you are player 1,", username2, "you are player 2")
print("")

while True:
    print(username1, '?')
    answer1 = input(templatechoice)

    isanswerrock= (answer1 != '1' and answer1 != "Rock")
    isanswerpaper= (answer1 != '2' and answer1 != "Paper")
    isswerscissor= (answer1 != '3' and answer1 != "Scissor")
    print(isanswerrock,isanswerpaper,isanswerscissor)
  #if answer1=/ 1 ,2 of 3 of Rock paper or scissor repeat ine 21
    correct=False
    if isanswerrock and isanswerpaper  and  isanswerscissor:
      correct=False
    else: correct=True
    print(correct)
    
      

    print(username2, '?')
    answer2 = input(templatechoice)
    print("")

    # gelijkspel
    if (answer1 == "1" or answer1 == "Rock") and (answer2 == "1" or answer2 == "Rock"):
        print("Both took rock, you both suck.")
    elif (answer1 == "2" or answer1 == "Paper") and (answer2 == "2" or answer2 == "Paper"):
        print("Both took Paper, you both suck.")
    elif (answer1 == "3" or answer1 == "Scissor") and (answer2 == "3" or answer2 == "Scissor"):
        print("Both took Scissor, you both suck.")

    # u1 won
    elif (answer1 == "1" or answer1 == "Rock") and (answer2 == "3" or answer2 == "Scissor"):
        print(username1, "won by picking rock")
        scoreusername1 += 1
    elif (answer1 == "3" or answer1 == "Scissor") and (answer2 == "2" or answer2 == "Paper"):
        print(username1, "won by picking scissor")
        scoreusername1 += 1
    elif (answer1 == "2" or answer1 == "Paper") and (answer2 == "1" or answer2 == "Rock"):
        print(username1, "won by picking Paper")
        scoreusername1 += 1

    # u2 won
    elif (answer1 == "3" or answer1 == "Scissor") and (answer2 == "1" or answer2 == "Rock"):
        print(username2, "won by picking rock")
        scoreusername2 += 1
    elif (answer1 == "1" or answer1 == "Rock") and (answer2 == "2" or answer2 == "Paper"):
        print(username2, "won by picking paper")
        scoreusername2 += 1
    elif (answer1 == "2" or answer1 == "Paper") and (answer2 == "3" or answer2 == "Scissor"):
        print(username2, "won by picking scissor")
        scoreusername2 += 1

    

    else:
        print("fu")
    print("")
    print(answer1, "and", answer2, 'were picked in this game')
    print("scores:")

    doorgaan = input("Continue? (yes/no): ")
    if doorgaan == 'no':
        break

while True:
    print(username1, '?')
    answer1 = input(templatechoice)

    isanswerrock= (answer1 != '1' and answer1 != "Rock")
    isanswerpaper= (answer1 != '2' and answer1 != "Paper")
    isanswerscissor= (answer1 != '3' and answer1 != "Scissor")
    print(isanswerrock,isanswerpaper,isanswerscissor)
#if answer1=/ 1 ,2 of 3 of Rock paper or scissor repeat ine 21
    
#correct = false if answer != rock paper scissor
  correct=False
    if isanswerrock and isanswerpaper  and  isanswerscissor:
      correct=False
#correct = true if answer != true
    else: correct=True
    print(correct)
    
      

    print(username2, '?')
    answer2 = input(templatechoice)
    print("")

    # gelijkspel
    if (answer1 == "1" or answer1 == "Rock") and (answer2 == "1" or answer2 == "Rock"):
        print("Both took rock, you both suck.")
    elif (answer1 == "2" or answer1 == "Paper") and (answer2 == "2" or answer2 == "Paper"):
        print("Both took Paper, you both suck.")
    elif (answer1 == "3" or answer1 == "Scissor") and (answer2 == "3" or answer2 == "Scissor"):
        print("Both took Scissor, you both suck.")

    # u1 won
    elif (answer1 == "1" or answer1 == "Rock") and (answer2 == "3" or answer2 == "Scissor"):
        print(username1, "won by picking rock")
        scoreusername1 += 1
    elif (answer1 == "3" or answer1 == "Scissor") and (answer2 == "2" or answer2 == "Paper"):
        print(username1, "won by picking scissor")
        scoreusername1 += 1
    elif (answer1 == "2" or answer1 == "Paper") and (answer2 == "1" or answer2 == "Rock"):
        print(username1, "won by picking Paper")
        scoreusername1 += 1

    # u2 won
    elif (answer1 == "3" or answer1 == "Scissor") and (answer2 == "1" or answer2 == "Rock"):
        print(username2, "won by picking rock")
        scoreusername2 += 1
    elif (answer1 == "1" or answer1 == "Rock") and (answer2 == "2" or answer2 == "Paper"):
        print(username2, "won by picking paper")
        scoreusername2 += 1
    elif (answer1 == "2" or answer1 == "Paper") and (answer2 == "3" or answer2 == "Scissor"):
        print(username2, "won by picking scissor")
        scoreusername2 += 1

    

    else:
        print("fu")
    print("")
    print(answer1, "and", answer2, 'were picked in this game')
    print("scores:")

    doorgaan = input("Continue? (yes/no): ")
    if doorgaan == 'no':
        break