#Display a welcome message
print("Welcome to Rock, Paper, Scissors")

#Players are asked to enter their names
player1name = str(input("Player1 please enter your name please: ")).lower()
player2name = str(input("Player2 please enter your name please: ")).lower()

#Initial score of players is set to 0
scoreplayer1 = 0
scoreplayer2 = 0

#Create a loop to play for 3 rounds, indentation is key to run the loop.
for round in range (1,4):
    print (f"It's a 3 rounds game. This is round number: {round}")
    
#Players are requested to enter their choices.
    choiceP1 = str(input(f"{player1name} please make a choice Rock, Paper, Scissors : ")).lower()
    #Checking if spelling of choice is correct
    while choiceP1 not in ["rock", "paper", "scissors"]:
        print("\n Invalid option. Please enter a valid option")
        choiceP1 = str(input(f"{player1name} please make a choice Rock, Paper, Scissors : ")).lower()
        
    choiceP2 = str(input(f"{player2name} please make a choice Rock, Paper, Scissors : ")).lower()
    #Checking if spelling of choice is correct.
    while choiceP2 not in ["rock", "paper", "scissors"]:
        print ("\n Invalid option. Please enter a valid option")
        choiceP2 = str(input(f"{player2name} please make a choice Rock, Paper, Scissors : ")).lower()


#Comparing choices to detemrine winner, updating and displaying score
    if choiceP1 == choiceP2 :
        print ("It is a tie!")
    elif choiceP1 == "rock" and choiceP2 == "paper":
        scoreplayer2 +=1
        print(f"{player2name} wins, {player2name}'s score is: {scoreplayer2}, {player1name}'s score is: {scoreplayer1}")
    elif choiceP1 == "paper" and choiceP2 == "rock":
        scoreplayer1 +=1
        print(f"{player1name} wins, {player1name}'s score is: {scoreplayer1}, {player2name}'s score is: {scoreplayer2}")
    elif choiceP1 == "rock" and choiceP2 == "scissors":
        scoreplayer1 +=1
        print(f"{player1name} wins, {player1name}'s score is: {scoreplayer1}, {player2name}'s score is: {scoreplayer2}")
    elif choiceP1 == "scissors" and choiceP2 == "rock":
        scoreplayer2 +=1
        print(f"{player2name} wins, {player2name}'s score is: {scoreplayer2}, {player1name}'s score is: {scoreplayer1}")
    elif choiceP1 == "scissors" and choiceP2 == "paper":
        scoreplayer1 +=1
        print(f"{player1name} wins, {player1name}'s score is: {scoreplayer1}, {player2name}'s score is: {scoreplayer2}")
    elif choiceP1 == "paper" and choiceP2 == "scissors":
        scoreplayer2 +=1
        print(f"{player1name} wins, {player1name}'s score is: {scoreplayer1}, {player2name}'s score is: {scoreplayer2}")
        
#A message before next round
    print("\nGood game!")
    
#Checking final results after 3 rounds loop, 
if scoreplayer1 > scoreplayer2 :
    print(f"\n{player1name} wins!")
elif scoreplayer2 > scoreplayer1:
    print (f"\n{player2name} wins!")
else:
    print ("\nIt's a Draw!")
    
#Final message
print("\nThank you for playing")
    