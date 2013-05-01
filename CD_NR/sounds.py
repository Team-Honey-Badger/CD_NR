

import pygame,os
#s = settings.Settings()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.set_num_channels(100)

soundEffects = {}

#ambience sound effects
soundEffects['Background'] = os.path.join('ambience','Background.mp3')

#Weapon sound effects
soundEffects['RifleShot'] = os.path.join('weapons','RifleShot.wav')
soundEffects['ShotgunShot'] = os.path.join('weapons','ShotgunShot.wav')
soundEffects['ShotgunPump'] = os.path.join('weapons','ShotgunPump.wav')
soundEffects['SwordSwing'] = os.path.join('weapons','SwordSwing.wav')
soundEffects['SpearThrow'] = os.path.join('weapons','SpearThrow.wav')

#Player sound effects
soundEffects['PlayerHit'] = os.path.join('player','PlayerHit.wav')
soundEffects['PlayerDeath'] = os.path.join('player','PlayerDeath.wav')

#Monster and enemy sound effects
soundEffects['AlienScream'] = os.path.join('enemy','AlienScream.wav')
soundEffects['InsectScreech'] = os.path.join('enemy','InsectScreech.wav')
soundEffects['MonsterScreech'] = os.path.join('enemy','MonsterScreech.wav')
soundEffects['EnemyHit'] = os.path.join('enemy','EnemyHit.wav')
soundEffects['InsectPain'] = os.path.join('enemy','InsectPain.wav')

def play(soundName, volume):
	sound = pygame.mixer.Sound(os.path.join('sounds', soundEffects[soundName]))
	sound.set_volume(volume)
	sound.play(0)
	
def loop(soundName, s):
	sound = pygame.mixer.music.load(os.path.join('sounds', soundEffects[soundName]))
	pygame.mixer.music.set_volume(s.volume)
	pygame.mixer.music.play(-1)
		
