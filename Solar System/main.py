import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
	AU = 149.6e6 * 1000 #Astronomical Unit m
	G = 6.67428e-11 #Exceleration of gravity
	SCALE = 250 / AU # 1AU = 100 pixels/ change to reduce space between planets
	TIMESTEP = 3600*24 # 1 day

	def __init__(self, x, y, radius, colour, mass):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.mass = mass

		self.orbit = []
		self.sun = False
		self.distance_to_sun = 0

		self.x_vel = 0
		self.y_vel = 0

	def draw(self, win):
		x = self.x * self.SCALE + WIDTH / 2
		y = self.y * self.SCALE + HEIGHT / 2

		if len(self.orbit) > 2:
			updated_points = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + WIDTH / 2
				y = y * self.SCALE + HEIGHT / 2
				updated_points.append((x, y))

			pygame.draw.lines(win, self.colour, False, updated_points, 2)

		pygame.draw.circle(win, self.colour, (x,y), self.radius)

		if not self.sun:
			distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
			win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_width() / 2))

	def attraction(self, other):
		"""Calculating distance between objects"""
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

		"""Checking if the object not the sun"""
		if other.sun:
			self.distance_to_sun = distance

		"""Calculating force into the x and y"""
		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force

		return force_x, force_y

	def update_position(self, planets):
		tottal_fx = tottal_fy = 0
		for planet in planets:
			"""Checking if it is execly out planet"""
			if self == planet:
				continue

			fx, fy = self.attraction(planet)
			tottal_fx += fx
			tottal_fy += fy

		"""Finding the velocity"""
		self.x_vel += tottal_fx / self.mass * self.TIMESTEP
		self.y_vel += tottal_fy / self.mass * self.TIMESTEP

		"""Finding the x y by Velocity"""
		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP

		self.orbit.append((self.x, self.y))

def main():
	run = True
	clock = pygame.time.Clock()

	sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
	sun.sun = True

	earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
	earth.y_vel = 29.783 * 1000

	mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
	mars.y_vel = 24.077 * 1000

	mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**24)
	mercury.y_vel = -47.4 * 1000

	venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
	venus.y_vel = -35.02 * 1000

	planets = [sun, mercury, venus, earth, mars]

	while run:
		clock.tick(60)
		WIN.fill((0,0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for planet in planets:
			planet.update_position(planets)
			planet.draw(WIN)

		pygame.display.update()

	pygame.quit()


main()