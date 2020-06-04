#Day 1
#Program 5

player_1 = int(input("Enter runs scored by first player in 60balls"))
player_2 = int(input("Enter runs scored by second player in 60 balls"))
player_3 = int(input("Enter runs scored by third player in 60 balls"))

#strikeRate = runs/balls *100
strike_rate_1 = (player_1/60) * 100
strike_rate_2 = (player_2/60) * 100
strike_rate_3 = (player_3/60) * 100

#runScore after 120 balls
new_run_1 = player_1 * 2
new_run_2 = player_2 * 2
new_run_3 = player_3 * 2

#maximum number of sixes each player could have hit
max_six_1 = player_1 // 6
max_six_2 = player_2 // 6
max_six_3 = player_3 // 6

#output
#strike_rate
print()
print("strike rate of 1st player is : ",strike_rate_1)
print("strike rate of 2nd player is : ",strike_rate_2)
print("strike rate of 3rd player is : ",strike_rate_3)
#runsscored in 120 balls
print()
print("runs scored by 1st player in 60 balls more is : ",new_run_1)
print("runs scored by 2nd player in 60 balls more is : ",new_run_2)
print("runs scored by 3rd player in 60 balls more is : ",new_run_3)
#Max Sixes
print()
print("Max sixes could 1st player hit = ",max_six_1)
print("Max sixes could 2nd player hit = ",max_six_2)
print("Max sixes could 3rd player hit = ",max_six_3)