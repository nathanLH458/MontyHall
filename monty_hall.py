#monty hall:
import random
import sys
import csv

print('Welcome to the Monty Hall problem simulator.')
print('Please choose door A , B or C')

#define doors:
door_A = 'A'
door_B = 'B'
door_C = 'C'
door_list = [door_A, door_B, door_C]
#choose winner out of these doors:
winner = random.choice(door_list)
#create a list with the losing doors. Needed for random when original pick is winning door.
door_list_without_winner = [door for door in door_list if door != winner]
#Begin: player chooses a door.
user_choice = input('Choose your door:   ')
#Make a list without the user_choice in it. Needed for when original pick is losing door.
list_without_user_choice = [door for door in door_list if door != user_choice]

#Function that prints confirmation of chosen door. If door chosen is not possible, code stops.
def door_choice_1():
    if user_choice in door_list:
        print('You have chosen door ' + user_choice)
    else:
        print('That door is invalid.')
        sys.exit('Invalid door...')
#Main function, that determines which door to switch to, if the users switches, and ultimately determines if user wins or not. + adjusts the file (to keep score)
def monty_hall_simulated():
    if user_choice == winner:
        revealed_door = random.choice(door_list_without_winner)
        other_door_in_list = [door for door in door_list_without_winner if door != revealed_door]
        other_door = ''.join(other_door_in_list)
        print('It is not ' + revealed_door + '.')
        does_user_switch = input('Would you like to switch to ' + str(other_door) + '? Y/N    ' )
        if does_user_switch == 'Y':
            print('You have lost. Door ' + winner + ' was the correct choice.')
        elif does_user_switch == 'N':
            print ('Congratulations, you have won! Door ' + winner + ' was the winning door.')
        else:
            sys.exit('Invalid answer...')
    if user_choice != winner:
        revealed_door_in_list = [door for door in list_without_user_choice if door != winner]
        revealed_door = ''.join(revealed_door_in_list)
        print('It is not ' + str(revealed_door) + '.')
        does_user_switch = input('Would you like to switch to ' + winner + '?  Y/N   ')
        if does_user_switch == 'Y':
            print('Congratulations, you have won! Door ' + winner + ' was the winning door.')
        elif does_user_switch == 'N':
            print ('You have lost. Door ' + winner + ' was the correct choice.')
        else:
            sys.exit('Invalid answer...')
    #Reads existing data in the file, so it doesnt reset every run.
    def data_reading():
        winning_and_losing_data = []
        with open('data_monty_hall.csv', newline='') as simulation_data:
            data = csv.reader(simulation_data, delimiter = '=')
            for line in data:
                winning_and_losing_data.append(line)
        return winning_and_losing_data
    data_reading()
    data_winning = data_reading()[0] #is used for writing: ['Wins', int]
    data_losing = data_reading()[1] #is used for writing: ['Losses', int]
    #sorts data (isolates the integers for wins and losses from csv file)
    def data_sorting():
        wins_string = data_winning[-1]
        losses_string = data_losing[-1]
        wins = int(wins_string)
        losses = int(losses_string)
        return [wins, losses]
    data_sorting()
    #adjusts the data: adds a loss or a win depending on the outcome of the experiment
    def data_adjuster():
        if user_choice == winner:
            losses_adjusted = data_sorting()[-1] + 1
            return [data_sorting()[0], losses_adjusted]
        if user_choice != winner:
            wins_adjusted = data_sorting()[0] + 1
            return [wins_adjusted, data_sorting()[-1]]
    data_adjuster()
    #edits the csv file with the new data given.
    def data_writer():
        definite_data = [[data_winning[0], data_adjuster()[0]], [data_losing[0], data_adjuster()[1]]]
        with open('data_monty_hall.csv', 'w', newline='') as simulation_data:
            datawriter = csv.writer(simulation_data,delimiter= '=')
            datawriter.writerow(definite_data[0])
            datawriter.writerow(definite_data[-1])
    data_writer()
#program run
if __name__ == '__main__':
     door_choice_1()
     monty_hall_simulated()

#want to make this code restartable. Is work in progress.
