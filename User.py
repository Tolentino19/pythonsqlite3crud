class User:
	def __init__(self, uname, email, password):
		self.uname = uname
		self.email = email
		self.password = password
	
	def __repr__(self):
		return 'User object({}, {}, {}, {})'.format(self.uname, 
                                                            self.email, 
                                                            self.password)
	def __str__(self):
		return ('Username: {} \n'.format(self.uname) +
                       'E-mail: {} \n'.format(self.email) +
                       'Password: {} \n'.format(self.password))
