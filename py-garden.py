class io:
	pass

class plant:
	def __init__(self, plantName, plantType, waterDuty = 0.5) -> None:
		self.name = plantName
		self.type = plantType
		self.waterDuty = waterDuty

	def set_name(self, plantName):
		self.name = plantName

	def set_type(self, plantType ):
		self.type = plantType

	def check_moisture(self):
		if self.moisture == True
		self.moisture = True