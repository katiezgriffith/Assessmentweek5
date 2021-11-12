log_file = open("um-server-01.txt") #Can open file "um-server-01.txt" in Python


def sales_reports(log_file): #def is the keyword for defining function "sales_reports" followed by parameter of (log_file) and ":" signals the start of the function
    for line in log_file: #for loop that loops over every line in "log_file"
        line = line.rstrip()#returns a copy of the string with trailing characters removed
        day = line[0:3]# says day is equavalent to whatever is on the first and fourth line
        if day == "Mon":# if the day matches "Whatever day" or here "MON"
            print(line)# return that line


sales_reports(log_file) # calling the function that gives all the sales on Monday
