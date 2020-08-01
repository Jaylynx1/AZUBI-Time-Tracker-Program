# AZUBI-Time-Tracker-Program



Contributors: David Gebe, Elvin Assiam, Ebo Ghartey
	
 
  
  
  Program Implementation:
The purpose of the program is to calculate hours worked by a user and multiply the worked hours by 5 to get the total salary/wage.
 
Trying to put the User's convenience first, we decided to make room for 2 functions
	
The first allows the user to enter his/her start work date and end work date manually in case the user wants to calculate based on historical data.

The second allows the user to simply initiate the program when he is about to start work by typing 'start' and typing 'stop' when he/she is done working, leaving the program to automatically calculate total working hours and total salary earned

A constant feature of both functions is to write to a csv file when the program is done executing and calculating
where it stores the data in 3 field names: Time Started, Time Ended and Total Money earned

Program Design:
 
The program is basically 3 separate functions

1. Time_Tracker() :
which is the main function that is called to initiate the program. 
it encapsulates the 2 other functions (Manual_Track() and Auto_Track())
Upon being called, the user is prompted to choose if he/she wants to manually enter the dates for the program to run, or if the user seeks to have the program track the working hours automatically by simply typing 'start' when the said user is about to start work and typing 'stop' when the said user is done working
 
 2. Manual_Track():
This function is found in the body of the main function (Time_Tracker())
Allowing the user to manually enter the start work date and end work date, the function uses the datetime library to convert dates inputted into a constant format to allow the calculation of the time difference to get the total time worked (Which includes days depending on the input by the user) and stored in the local variable Diff_seconds 
The difference calculated is then converted to seconds using the .seconds method and then divided by 3600 (total number of seconds in an hour) to convert it to total hours worked and stored in the local variable Hours. The variable Money then stores the total money earned which is simple the product of total hours worked (Hours) and 5 (the hourly pay).
 
After the calculations are done, the user has his total hours worked and total money earned displayed then the program writes the output to a csv file with the field names Time Started, Time Ended and Total Money earned.
 
3. Auto_Track():
This function is also found in the body of the main function (Time_Tracker())
The function prompts the user to simply type 'start' when the user is about to start work and type 'stop' when the user is done working.
The function uses the time library to track the system current time using the .time method and the time periods are stored in local variables start and stop for calculations later on.
To get the total hours worked, the difference of the variables start and stop are calculated and the result is divided by 3600. This result is stored in the Hours variable and then multiplied by 5 to get the total money earned
After the calculations are done, the user has his total hours worked and total money earned displayed then the program writes the output to a csv file with the field names Time Started, Time Ended and Total Money earned.

Program dependencies
 
The Time Tracker program depends primarily on the User's input
Whether the user seeks to calculate based on historical data by manually entering the dates (Manual_Track) or use the system's date (Auto_Track) 
 
The program also relies heavily on the following libraries:
-datetime : to store the date in a constant formate and allow operations to calculate time difference and convertion
-time : to track and calculate system date and enable operations (calculating the time difference)
-csv : in order to write to .csv files and store output



Team
 
The team comprises of David Selorm Gebe, Elvin Assiam and Ebo Ghartey-Koomson
 
Roles:
Proof reader and program editor - Elvin Assiam

Lead programmer and project manager - David Selorm Gebe

Program editor and evaluator - Ebo Ghartey-Koomson
