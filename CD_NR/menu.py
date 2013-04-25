import os, pygame, sys, settings
from pygame.locals import *
from utils import *
s = settings.Settings()

class Volume():
	def __init__(self):
		self.image,_ = load_image(os.path.join("Volume Screen.png"))
		
		self.one_rect = pygame.Rect(18,137,44,40)
		self.two_rect = pygame.Rect(77,137,44,40)
		self.three_rect = pygame.Rect(135,137,44,40)
		self.four_rect = pygame.Rect(190,137,44,40)
		self.five_rect = pygame.Rect(247,137,44,40)
		self.six_rect = pygame.Rect(303,137,44,40)
		self.seven_rect = pygame.Rect(361,137,44,40)
		self.eight_rect = pygame.Rect(420,137,44,40)
		self.nine_rect = pygame.Rect(474,137,44,40)
		self.ten_rect = pygame.Rect(534,137,44,40)
		
		self.mouse_pos = (-1,1)
		self.mousePressed = 0
		
	def mouseDown(self, pos):
		self.mouse_pos = pos

	def mouseUp(self, pos, isClicked):
		def collides_down_and_up( r ):
			return r.collidepoint( self.mouse_pos ) and r.collidepoint( pos )
		
		if(isClicked == 1):
			if collides_down_and_up (self.one_rect):
				s.volume = 0.1
				return 0.1
			elif collides_down_and_up (self.two_rect):
				s.volume = 0.2
				return 0.2
			elif collides_down_and_up (self.three_rect):
				s.volume = 0.3
				return 0.3
			elif collides_down_and_up (self.four_rect):
				s.volume = 0.4
				return 0.4
			elif collides_down_and_up (self.five_rect):
				s.volume = 0.5
				return 0.5
			elif collides_down_and_up (self.six_rect):
				s.volume = 0.6
				return 0.6
			elif collides_down_and_up (self.seven_rect):
				s.volume = 0.7
				return 0.7			
			elif collides_down_and_up (self.eight_rect):
				s.volume = 0.8
				return 0.8
			elif collides_down_and_up (self.nine_rect):
				s.volume = 0.9
				return 0.9
			elif collides_down_and_up (self.ten_rect):
				s.volume = 1.0
				return 1.0
			else:
				pass
		   
	def update(self, pos, isClicked):
		self.mouseDown(pos)
		self.mousePressed = isClicked[0]
		readyYet = self.mouseUp(pos, self.mousePressed)
		return readyYet

		
	def draw( self, screen ):
		screen.blit( self.image, ( 0,0 ) )
		pygame.display.flip()
		
class Resolution():
	def __init__(self):
		self.image,_ = load_image(os.path.join("Resolution Screen.png"))
		
		self.high = pygame.Rect(220,82,131,40)
		self.medium = pygame.Rect(220,140,131,40)
		self.low = pygame.Rect(220,195,131,40)
		
		self.resolution = None
		self.mouse_pos = (-1,1)
		self.mousePressed = 0
		
	def mouseDown(self, pos):
		self.mouse_pos = pos
	
	def mouseUp(self, pos, isClicked):
		def collides_down_and_up( r ):
			return r.collidepoint( self.mouse_pos ) and r.collidepoint( pos )
		
		if(isClicked == 1):
			if collides_down_and_up(self.high):
				s.resolution = 1600,800
				s.scalar = 2
				return "high"
			elif collides_down_and_up(self.medium):
				s.resolution = 1200,600
				s.scalar = 1.5
				return "medium"
			elif collides_down_and_up(self.low):
				s.resolution = 800,400
				s.scalar = 1
				return "low"
			else:
				pass
		   
	def update(self, pos, isClicked):
		self.mouseDown(pos)
		self.mousePressed = isClicked[0]
		readyYet = self.mouseUp(pos, self.mousePressed)
		return readyYet

		
	def draw( self, screen ):
		screen.blit( self.image, ( 0,0 ) )
		pygame.display.flip()
		
class ScreenSize():
	def __init__(self):
		self.image,_ = load_image(os.path.join("Screen Size.png"))
		
		self.mouse_pos = (-1,1)
		self.mousePressed = 0
		
		self.fullscreen = pygame.Rect(217,22,136,34)
		self.windowed = pygame.Rect(211,197,150,31)
		
	def mouseDown(self, pos):
		self.mouse_pos = pos
	
	def mouseUp(self, pos, isClicked):
		def collides_down_and_up( r ):
			return r.collidepoint( self.mouse_pos ) and r.collidepoint( pos )
		
		if(isClicked == 1):
			if collides_down_and_up(self.fullscreen):
				s.fullscreen = 1
				return 1
			elif collides_down_and_up(self.windowed):
				s.fullscreen = 0
				return 0
			else:
				pass
		   
	def update(self, pos, isClicked):
		self.mouseDown(pos)
		self.mousePressed = isClicked[0]
		readyYet = self.mouseUp(pos, self.mousePressed)
		return readyYet

		
	def draw( self, screen ):
		screen.blit( self.image, ( 0,0 ) )
		pygame.display.flip()
		
class Mode():
	def __init__(self):
		self.image,_ = load_image(os.path.join("Mode Screen.png"))
		
		self.storyMode = pygame.Rect(205,12,177,42)
		self.customMode = pygame.Rect(198,208,208,45)
		
		self.mouse_pos = (-1,1)
		self.mousePressed = 0
		
	def mouseDown(self, pos):
		self.mouse_pos = pos
	
	def mouseUp(self, pos, isClicked):
		def collides_down_and_up( r ):
			return r.collidepoint( self.mouse_pos ) and r.collidepoint( pos )
		
		if(isClicked == 1):
			if collides_down_and_up(self.storyMode):
				s.mapsFolder = "storyMaps"
				return 1
			elif collides_down_and_up(self.customMode):
				s.mapsFolder = "customMaps"
				return 0
			else:
				pass
		   
	def update(self, pos, isClicked):
		self.mouseDown(pos)
		self.mousePressed = isClicked[0]
		readyYet = self.mouseUp(pos, self.mousePressed)
		return readyYet

		
	def draw( self, screen ):
		screen.blit( self.image, ( 0,0 ) )
		pygame.display.flip()

def main():
	configure = open("settings.txt","wb")
	pygame.init()
	screen = pygame.display.set_mode( [600,300] )
	pygame.display.set_caption("configure screen")
	VolumeScreen = Volume()
	ResolutionScreen = Resolution()
	ScreenChoice = ScreenSize()
	ModeChoice = Mode()
	
	walkthrough = 0
	
	active = True
	while active:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			

			mousePOS = pygame.mouse.get_pos()
			mouseClick = pygame.mouse.get_pressed()
			
			if (walkthrough == 0):
				VolumeScreen.draw(screen)
				volLevel = VolumeScreen.update(mousePOS, mouseClick)
				if (volLevel != None):
					configure.write(str(volLevel))
					walkthrough = 1
					configure.write(' ')
					
			
			elif (walkthrough == 1):
				ResolutionScreen.draw(screen)
				resol = ResolutionScreen.update(mousePOS, mouseClick)
				if (resol != None):
					configure.write(str(resol))
					walkthrough = 2
					configure.write(' ')
					
			elif (walkthrough == 2):
				ScreenChoice.draw(screen)
				choice = ScreenChoice.update(mousePOS, mouseClick)
				if (choice != None):
					configure.write(str(choice))
					walkthrough = 3
					configure.write(' ')
					
			elif (walkthrough == 3):
				ModeChoice.draw(screen)
				choice = ModeChoice.update(mousePOS, mouseClick)
				if (choice != None):
					configure.write(str(choice))
					walkthrough = 4
					configure.write(' ')
					
			elif (walkthrough == 4):
				configure.close()
				pygame.quit()
				#sys.exit()
				active = False
			

main()