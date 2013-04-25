import os, pygame

from pygame.locals import *

def load_image( name, colorkey = None ):
    '''
    Given a filename 'name' in the data directory and
    a color 'colorkey' whose RGB value (or color map index) will be treated as transparent,
    loads the image and returns a pygame.Surface.
    
    NOTE: The default 'colorkey' parameter, None, causes the image
          to be entirely opaque.
    NOTE: The special 'colorkey' value of -1 causes the top-left pixel color
          in the image to be used as the transparent color.
    '''
    
    ## Find 'name' within the 'data' directory independent of
    ## operating system path character.
    fullname = os.path.join( 'data', name )
    try:
        image = pygame.image.load( fullname )
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at( (0,0) )
        ## accelerate
        image.set_colorkey( colorkey, RLEACCEL )
    return image, image.get_rect()

