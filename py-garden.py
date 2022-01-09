

class plant:
	def __init__(self, plantName, plantType, waterDuty = 0.5):
		self.name = plantName
		self.type = plantType
		self.waterDuty = waterDuty

	def setName(self, plantName):
		self.name = plantName

	def setType(self, plantType ):
		self.type = plantType
	
	def setMoistureIO(self, source):
		self.moistureSource = source

	def checkMoisture(self):
		try:
			if self.moistureSource != None:
				if self.moistureSource == True:
					self.moisture = True
				else:
					self.moisture = False
			return self.moisture
		except:
			print("No Moisture sensor found. Set moisture source with setMoistureIO()")

	def printStatus(self):
		print("Name:", self.name)
		print("Type:", self.type)
		print("Moisture:", self.checkMoisture())


plant1 = plant("pep1" , "Jalapeno")
#plant1.setMoistureIO(True)

plant1.printStatus()