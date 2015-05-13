"""pieEngine - Pygame Engine
"""

from threading import Timer

import pygame

from pie.entity.background import BackgroundImage
from pie.entity.primitive import Fill
from pie.entity.image import Image
from pie.entity.composite import DistributedOnce, DistributedAnimated
from pie.engine import Engine


class Demo(Engine):
    def __init__(self, *args, **kwa):
        Engine.__init__(self, *args, **kwa)

        image_surf = pygame.image.load("assets/bomber10000.png").convert_alpha()
        image_surf = pygame.transform.scale(image_surf, (64,64))

        boxy = DistributedOnce(*[Image(image_surf, rect_kwa={'center':(512,256)})
                                 for _ in range(10)])

        self.add_render_plain(boxy) # Adding a group here, but pygame breaks this down in to individual sprites, therefore breaking any sub_group functionality.
        self.drag_handler.append(boxy)

        boxy = DistributedAnimated(*[Image(image_surf, rect_kwa={'center':(512,256)})
                                     for _ in range(10)])
        self.add_render_plain(boxy) # Adding a group here, but pygame breaks this down in to individual sprites, therefore breaking any sub_group functionality.
        self.drag_handler.append(boxy)



if __name__ == "__main__":
    pygame.init()


    bf = lambda: BackgroundImage(
                        pygame.image.load("assets/bg2.png").convert())


    game = Demo(pygame.display.set_mode((1024, 512),
                                         pygame.RESIZABLE), background_factory=bf)
    #t = Timer(10, game.stop)
    #t.start()

    game.start()

    #t.join()