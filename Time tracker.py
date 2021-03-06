def Time_Tracker():
        def Manual_Track():
                import datetime
                import time
                from datetime import timedelta
                import csv
                datetimeFormat = '%Y-%m-%d %H:%M'
                print("Please enter date and time in format = 'year-month-day time' \n For example = '2016-04-16 13:00'")
                start_work = input("Please enter START DATE and TIME: ")
                stop_work = input("Please enter END DATE and TIME: ")
                StopHours = (datetime.datetime.strptime(stop_work, datetimeFormat))
                StartHours = (datetime.datetime.strptime(start_work, datetimeFormat))
                Diff_seconds = (StopHours - StartHours).seconds
                Hours = round((Diff_seconds/3600),2)
                Money = round((Hours * 5),2)
                print(f"Your total hours worked is: {Hours} hours")
                print(f"Based on that, you have made ${Money}")

                with open('time_track_info.csv', mode='w') as csv_file:
                        fieldnames = ['Time Started', 'Time Ended', 'Number of hours spent','Total money earned $']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow({'Time Started': (start_work), 'Time Ended':(stop_work) , 'Number of hours spent': Hours, 'Total money earned $': Money})
        def Auto_Track():
                import time
                import csv
                user_input = input("Type 'start' to start timer")
                start = time.time()
                print (f'You started work at {time.ctime(int(start))}')
                user_input = input("Type 'stop' to stop timer")
                if (user_input == 'stop'):
                        stop = time.time()
                        print(f'You ended work at {time.ctime(int(stop))}')
                        Hours = round(((stop - start)/3600),2)
                        Money = round((Hours * 5),2)
                        print(f"Your total hours worked is: {Hours} hours")
                        print(f"Based on that, you have made ${round(Money,2)}")
                with open('time_track_info.csv', mode='w') as csv_file:
                        fieldnames = ['Time Started', 'Time Ended ', 'Number of hours spent','Total money earned $']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow({'Time Started': time.ctime(int(start)), 'Time Ended ':time.ctime(int(stop)) , 'Number of hours spent': Hours, 'Total money earned $': Money})
        print("Hello and welcome")
        user_input = input("Would you like to MANUALLY ENTER your TIME STAMP to calculate your hourly pay?(Y/N)")
        if user_input == ("Y"):
                Manual_Track()
        else:
                user_input = input("Would you like to START WORK and have your hours AUTOMATICALLY tracked to calculate your pay?(Y/N)")
                if user_input == ("Y"):
                        Auto_Track()
