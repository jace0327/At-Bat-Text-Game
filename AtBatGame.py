#Programmer: Jace Elliott
#Description: Game simulating baseball at bats, user enter's their RBI, and the program will compare it to a randomly generated number
#Date: 12/3/2021

from random import randint

def main():

    score = 0
    battingAvg = 0

    print("It's the bottom of the 9th, your team is down by one, with two outs and the bases are loaded. If you hit a double the game is over. Will you be the team hero?")

    battingAvg = int(input("What is your character's batting average? (0-300): "))
    
    #Trying to idiot proof the code
    if battingAvg < 0:
        print("You're not follwing directions, please enter a number above -1.")
        input("Press <enter> to restart the program")
        main()

    if battingAvg > 300:
        print("You're not following directions, please enter a number below 301.")
        input("Press <enter> to restart the program")
        main()

    #Balancing the numbers to make home runs harder to hit
    battingAvg2 = battingAvg/4
    
    #Asking the user if they are ready to start the loop
    ready = input("Is your batter ready?(y/n): ")

    while ready == "y":
        
        #There's a 1/3 chance that the batter will hit a foul ball no matter how good his batting avg stats are
        foul = randint(1,3)

        if foul == 3:
                print("Your batter hit the ball foul")
                ready = input("Is your batter ready?(y/n): ")

        else:
            #this is the number that the batting average divided by 4 is being compared to, if less than the pitch
            pitch = randint(1,301)

            #Decides if you hit home run or not
            if battingAvg2 >= pitch:
                print("You hit a HR!")
                score = 4
                break

            #If not, increases the value to see if you hit a triple
            else:
                battingAvg2 = 2 * battingAvg2

            #Checks to see if you hit a triple
            if battingAvg2 >= pitch:
                print("You hit a Triple!")
                score = 3
                break

            #If not, increases the value to see if you hit a double
            else:
                battingAvg2 = 2 * battingAvg2
                    
            #Checks to see if you hit a double
            if battingAvg2 >= pitch:
                print("You hit a Double!")
                score = 2
                break
                
            #If not, increases the value to see if you hit a single
            else:
                battingAvg2 = 2 * battingAvg2
                    
            #Checks to see if you hit a single
            if battingAvg2 >= pitch:
                print("You hit a Single!")
                score = 1
                break
            #If you fail to get a base hit, then you hit a pop fly and the game is over, you lost
            else:
                print("You hit a pop fly")
                print("You're the final out and ruined the chances of a comeback for your team.")
                break

    #Checks to see if you won or tied the game
    if score >= 2:
            print("You're the team hero, you won them the game!")
        
    if score == 1:
            print("You tied the game!, if the next batter doesn't get a base hit at least you brought the game into overtime!")
         
main()
