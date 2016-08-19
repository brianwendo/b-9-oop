from datetime import datetime
map_ ={
	'KE': 'Kenya',
	'NG': 'Nigeria',
	'UG': 'Uganda',
	'TZ': 'Tanzania'
}
class Student(object):
	#generate sequential ID
	attendance = []
	current_id = 0
	
	def __init__(self, id, fname, lname, cc='KE'):
		
		Student.current_id += 1
		
		self.id = Student.current_id
		self.fname = fname
		self.lname = lname
		self.country = map_[cc]
        #generates a list of student attendance
	
	def attend_class(self,**kwargs):
		self.loc = kwargs.setdefault('loc', 'Hogwarts')
		self.date = kwargs.setdefault('date', datetime.today().date())
		self.teacher = kwargs.setdefault('teacher', 'Alex')

		Student.attendance.append(kwargs)
		#generates a list who were present on a particular day

	def student_attendance(self, date=datetime.today().date()):
		for item in Student.attendance:
			if item['date'] == date:
				print(item)

