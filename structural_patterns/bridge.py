"""
Scenario: You have two APIs for drawing a circle with different implementation.
util the Bridge design pattern to use the two of APIs classes in independent class
"""


from abc import ABC, abstractmethod


class Draw(ABC):
    
    @abstractmethod
    def draw_circle(self):
        pass


class DrawingAPIOne(Draw):
	"""Implementation-specific abstraction: concrete class one"""
	def draw_circle(self, x: float, y: float, radius: float) -> None:
		print(f"API 1 drawing a circle at ({x}, {y} with radius {radius}!)")


class DrawingAPITwo(Draw):
	"""Implementation-specific abstraction: concrete class two"""
	def draw_circle(self, x: float, y: float, radius: float) -> None:
		print(f"API 2 drawing a circle at ({x}, {y} with radius {radius}!)")

class Circle:
	"""Implementation-independent abstraction: for example, there could be a rectangle class!"""

	def __init__(self, x: float, y: float, radius: float, drawing_api: object) -> None:
		"""Initialize the necessary attributes"""
		self._x: float = x
		self._y: float = y
		self._radius: float = radius
		self._drawing_api: DrawingAPIOne or DrawingAPITwo = drawing_api

	def draw(self) -> None:
		"""Implementation-specific abstraction taken care of by another class: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent) -> None:
		"""Implementation-independent"""
		self._radius *= percent


if __name__ == '__main__':
    circle1: Circle = Circle(1, 2, 3, DrawingAPIOne()) # Build the first Circle object using API One
    circle1.draw() # Draw a circle

    circle2: Circle = Circle(2, 3, 4, DrawingAPITwo()) # Build the second Circle object using API Two
    circle2.draw() # Draw a circle

