import pygame

WIDTH = 480
HEIGHT = 300

GPIO_AVAILABLE = False
SOUND_ENABLED = False
COLOR_GREEN = (26, 255, 128)
COLOR_YELLOW = (150, 200, 128)
COLOR_BLUE = (10, 50, 200)
COLORS = [(26, 255, 128), (150, 200, 128), (10, 50, 200)]
COLOR_CURRENT = COLOR_GREEN
# OUTPUT_WIDTH = 320
# OUTPUT_HEIGHT = 240

#MAP_FOCUS = (-5.9347681, 54.5889076)
MAP_FOCUS = (-102.3016145, 21.8841274)

EVENTS = {
	'SONG_END': pygame.USEREVENT + 1
}

WEATHER_ICON = {
	'Clear': "F:/Java/Pip-Boy/Pip-Boy/Pip-Boy/images/sunny.png",
	'Clouds': "F:/Java/Pip-Boy/Pip-Boy/Pip-Boy/images/cloudy.png", 
	'rainy':"/images/rainy.png"
	}

ACTIONS = {
	pygame.K_F1: "module_stats",
	pygame.K_F2: "module_items",
	pygame.K_F3: "module_data",
	pygame.K_1:	"knob_1",
	pygame.K_2: "knob_2",
	pygame.K_3: "knob_3",
	pygame.K_4: "knob_4",
	pygame.K_5: "knob_5",
	pygame.K_UP: "dial_up",
	pygame.K_DOWN: "dial_down"
}

# Using GPIO.BCM as mode
GPIO_ACTIONS = {
    4: "module_stats", #GPIO 4
	14: "module_items", #GPIO 14
	15: "module_data", #GPIO 15
	17:	"knob_1", #GPIO 17
	18: "knob_2", #GPIO 18
	7: "knob_3", #GPIO 7
	22: "knob_4", #GPIO 22
	23: "knob_5", #GPIO 27
#	31: "dial_up", #GPIO 23
	27: "dial_down" #GPIO 7
}


MAP_ICONS = {
	"camp": 		pygame.image.load('images/map_icons/camp.png'),
	"factory": 		pygame.image.load('images/map_icons/factory.png'),
	"metro": 		pygame.image.load('images/map_icons/metro.png'),
	"misc": 		pygame.image.load('images/map_icons/misc.png'),
	"monument": 	pygame.image.load('images/map_icons/monument.png'),
	"vault": 		pygame.image.load('images/map_icons/vault.png'),
	"settlement": 	pygame.image.load('images/map_icons/settlement.png'),
	"ruin": 		pygame.image.load('images/map_icons/ruin.png'),
	"cave": 		pygame.image.load('images/map_icons/cave.png'),
	"landmark": 	pygame.image.load('images/map_icons/landmark.png'),
	"city": 		pygame.image.load('images/map_icons/city.png'),
	"office": 		pygame.image.load('images/map_icons/office.png'),
	"sewer": 		pygame.image.load('images/map_icons/sewer.png'),
}

AMENITIES = {
	'pub': 				MAP_ICONS['vault'],
	'nightclub': 		MAP_ICONS['vault'],
	'bar': 				MAP_ICONS['vault'],
	'fast_food': 		MAP_ICONS['sewer'],
	'cafe': 			MAP_ICONS['sewer'],
	'drinking_water': 	MAP_ICONS['sewer'],
	'restaurant': 		MAP_ICONS['settlement'],
	'cinema': 			MAP_ICONS['office'],
	'pharmacy': 		MAP_ICONS['office'],
	'school': 			MAP_ICONS['office'],
	'bank': 			MAP_ICONS['monument'],
	'townhall': 		MAP_ICONS['monument'],
	'bicycle_parking': 	MAP_ICONS['misc'],
	'place_of_worship': MAP_ICONS['misc'],
	'theatre': 			MAP_ICONS['misc'],
	'bus_station': 		MAP_ICONS['misc'],
	'parking': 			MAP_ICONS['misc'],
	'fountain': 		MAP_ICONS['misc'],
	'marketplace': 		MAP_ICONS['misc'],
	'atm': 				MAP_ICONS['misc'],
}


pygame.font.init()
FONTS = {}
topFont = pygame.font.Font('monofonto.ttf', 18)
bottomFont = pygame.font.Font('monofonto.ttf', 12)
genFont = pygame.font.Font('monofonto.ttf', 15)
"""for x in range(10, 28):
	FONTS[x] = pygame.font.Font('monofonto.ttf', x)"""