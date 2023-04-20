# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 05
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: 
# Citations: Multiple stackoverlow posts, as well as geeksforgeeks.org; http://introtopython.org/while_input.html
# Anything else that's relevant: I could not get the loop to work, my real job prevented me from making it into office hours Wednesday. 
# cont. The instructions did not specify to pull the key only on the print of myTeams so I did not include that.

from functionPackage.teamsFunction import *

myTeams = {'Columbus':'Ohio State', 'Terre Haute':'Indiana', 'West Lafayette':'Purdue', 'Ames':'Iowa', 'Evanston':'Northwestern', 
           'State College':'Penn State', 'Madison':'Wisconsin', 'Minneapolis':'Minnesota', 'New Brunswick':'Rutgers', 'Lincoln':'Nebraska',
           'Ann Arbor':'Michigan', 'East Lansing':'Michigan State'}
print_teams(myTeams)

myTeamsList = sorted(myTeams)


inputSchool = input('Please type the name of a Big 10 School?')
print(inputSchool)
if inputSchool in myTeamsList:
    print('Found ' + inputSchool)
else:
    print('Not Found ' +inputSchool)
