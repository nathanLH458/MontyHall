#monty hall:
import random
import sys
import csv
import time
print('Welcome to the Monty Hall problem simulator.')
print('Please choose door A , B or C')

#define doors:
door_A = 'A'
door_B = 'B'
door_C = 'C'
door_list = [door_A, door_B, door_C]
yeslist = ['Y', 'y', 'yes', 'YES', 'Yes']
nolist = ['N', 'n', 'no', 'NO', 'No']
#main() functions
def main():
    user_choice = input('Choose your door:   ')
    winner = random.choice(door_list) #calculates a random winning door
    list_without_user_choice = [door for door in door_list if door != user_choice] #needed for calculation
    door_list_without_winner = [door for door in door_list if door != winner] #needed for calculation
#user chooses his door
    def door_choice_1():
        if user_choice in door_list:
            print('You have chosen door ' + user_choice)
        else:
            print('That door is invalid.')
            input('press key to exit')
            sys.exit(0)
    door_choice_1()
#calculating function, that determines which door to switch to, if the users switches, and ultimately determines if user wins or not. + adjusts the file (to keep score)
    def monty_hall_simulated():
        if user_choice == winner:
            revealed_door = random.choice(door_list_without_winner)
            other_door_in_list = [door for door in door_list_without_winner if door != revealed_door]
            other_door = ''.join(other_door_in_list)
            time.sleep(2)
            print('The host tells you it is not door ' + str(revealed_door) + '.')
            time.sleep(2)
            does_user_switch = input('Would you like to switch to ' + str(other_door) + '? Y/N    ' )
            if does_user_switch in yeslist:
                print('You have lost. Door ' + winner + ' was the correct choice.')
            elif does_user_switch in nolist:
                print ('Congratulations, you have won! Door ' + winner + ' was the winning door.')
            else:
                print('Invalid answer...')
                input('press key to close program ')
                sys.exit(0)
        if user_choice != winner:
            revealed_door_in_list = [door for door in list_without_user_choice if door != winner]
            revealed_door = ''.join(revealed_door_in_list)
            time.sleep(2)
            print('The host tells you it is not door ' + str(revealed_door) + '.')
            time.sleep(2)
            does_user_switch = input('Would you like to switch to ' + winner + '?  Y/N   ')
            if does_user_switch in yeslist:
                print('Congratulations, you have won! Door ' + winner + ' was the winning door.')
            elif does_user_switch in nolist:
                print ('You have lost. Door ' + winner + ' was the correct choice.')
            else:
                print('Invalid answer...')
                input('press key to close program')
                sys.exit(0)
    monty_hall_simulated()
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
#make code restartable for multiple runs at a time.
    restart = input('Do you wish to restart? Y/N     ')
    if restart in yeslist:
        main()
    else:
        time.sleep(5)
        sys.exit(0)
#program run
if __name__ == '__main__':
    main()

