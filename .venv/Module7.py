#Dictionary 1 dictCourseNum_RoomNum, Key = Course Number : Values = Room Numbers
dictCourseNum_RoomNum = {"CSC101" : "3004", "CSC102" : "4501", "CSC103" : "6755", "NET110" : "1244",
                         "COM241" : "1411"}

#Dictionary 2 dictCourseNum_Instructor, Key = Course Number : Values = Instructor Last Name
dictCourseNum_Instructor = {"CSC101" : "Haynes", "CSC102" : "Alvarado", "CSC103" : "Rich", "NET110" : "Burke",
                         "COM241" : "Lee"}

#Dictionary 3 dictCourseNum_meetTime, Key = Course Number : Values = Meeting Time
dictCourseNum_meetTime = {"CSC101" : "8:00 a.m.", "CSC102" : "9:00 a.m.", "CSC103" : "10:00 a.m.",
                          "NET110" : "11:00 a.m.", "COM241" : "1:00 p.m."}

#Prompt user to enter the course number
userEnterCourseNumber = input("Enter Course Number to see Room Number, Instructor, and Meeting Time\n")

#Verify key exists with the .get method
getCourseNumKey = dictCourseNum_RoomNum.get(userEnterCourseNumber)

#If the result of the .get method is None, Print "The Course Number is Not Found"
if getCourseNumKey == None:
    print("Course Number not Found")

#If the result of the .get method is not None, print the result
else:
    print(userEnterCourseNumber + " meets in Room #" + getCourseNumKey + ", is instructed by Professor " +
          dictCourseNum_Instructor[userEnterCourseNumber] + ", and meets at " +
          dictCourseNum_meetTime[userEnterCourseNumber])