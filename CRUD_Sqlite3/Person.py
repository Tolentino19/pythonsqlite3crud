class Person:
	def __init__(self, name, pid, birthdate, phone, address):
		self.name = name
		self.pid = pid
		self.birthdate = birthdate
		self.phone = phone
		self.address = address
	
	def __repr__(self):
		return 'Person object({}, {}, {}, {}, {})'.format(self.name, 
                                                                  self.pid, 
                                                                  self.birthdate,
                                                                  self.phone, 
                                                                  self.address)
	def __str__(self):
		return ('Name: {} \n'.format(self.name) +
                       'PID: {} \n'.format(self.pid) +
                       'Birthdate: {} \n'.format(self.birthdate) +
                       'Phone: {} \n'.format(self.phone) +
                       'Address: {}'.format(self.address))
        
