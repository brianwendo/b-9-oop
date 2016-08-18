from datetime import datetime
map__:{
	'KE': 'Kenya',
	'NG': 'Nigeria',
	'UG': 'Uganda',
	'TZ': 'Tanzania'
}
class Student(object):
	#generate sequential ID
	current_id = 0
    def __init__(self, id, fname, lname):
        self.__id = id
        self.fname = fname
        self.lname = lname
        self.country = map__[cc]
	
	def attend_class(self, loc = 'Hogwarts', date = datetime.day(), teacher ='Alex):
		#default values
		#loc = 'Hogwarts'
		#date = current date
		#teacher ='Alex'
		pass

s1 = Student(1, 'Kevin', 'Chiteri', 'KE')
s2 = Student(2, 'Allan', 'M', 'UG')