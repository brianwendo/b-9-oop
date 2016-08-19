from student import Student

'''Create at least 10 students'''

s1 = Student('Kevin', 'Chiteri')
s2 = Student('Allan', 'Mali', 'UG')
s3 = Student('Bethwell', 'Mzungu')
s4 = Student('Gathu', 'Master', 'UG')
s5 = Student('Jane', 'Boss')
s6 = Student('Bob', 'Collymore')
s7 = Student('Emily', 'Aoko')
s8 = Student('Stan', 'Yule', 'UG')
s9 = Student('Innocent', 'Kateba' 'TZ')
s10 = Student('Winnie', 'Makeba', 'UG')

'''make at least 5 students attend class
#e.g

# You should be able to attend class on particular day'''
s1.attend_class(date='2016, 4, 22', id= s1.id, first_name=s1.fname, last_name=s1.lname, country=s1.country)
s2.attend_class(date = '2016, 4, 22', teacher='Alex', id= s2.id, first_name=s2.fname, last_name=s2.lname, country=s2.country)
s3.attend_class(date='2016, 4, 22', id= s1.id, first_name=s3.fname, last_name=s3.lname, country=s3.country)
s4.attend_class(date='2016, 4, 21', teacher='Alex', id= s4.id, first_name=s4.fname, last_name=s4.lname, country=s4.country)
s5.attend_class(date='2016, 4, 21', id= s5.id, first_name=s5.fname, last_name=s5.lname, country=s5.country)