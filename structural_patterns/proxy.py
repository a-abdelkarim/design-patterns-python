import time

class Producer:
	"""Define the 'resource-intensive' object to instantiate!"""
	def produce(self):
		print("Producer is working hard!")

	def meet(self):
		print("Producer has time to meet you now!")


class Proxy:
	""""Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
	def __init__(self):  
		self.occupied = False
		self.producer = None

	def produce(self):
		"""Check if Producer is available"""
		print("Artist checking if Producer is available ...")

		if not self.occupied:
			#If the producer is available, create a producer object!
			self.producer = Producer()
			time.sleep(2)

			#Make the producer meet the guest!
			self.producer.meet()
			
		else:
			#Otherwise, don't instantiate a producer 
			time.sleep(2)
			print("Producer is busy!")


if __name__ == '__main__':
    p = Proxy() #Instantiate a Proxy
    p.produce() #Make the proxy: Artist produce until Producer is available
    p.occupied = True #Change the state to 'occupied'
    p.produce() #Make the Producer produce 
