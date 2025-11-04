from pico2d import *
import game_framework
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 20.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class BIRD:
    image = None
    def __init__(self):
        self.x = random.randint(200, 1400)
        self.y = random.randint(300, 500)
        self.frame = 0
        self.face_dir = 1 #1오-1왼
        self.dir = 1  #1오-1왼

        if BIRD.image == None:
            BIRD.image = load_image('bird_animation.png')

    def draw(self):
        if int(self.frame) < 5:
            self.image.clip_draw(int(self.frame) * 181, 338, 185, 168, self.x, self.y)
        elif int(self.frame) < 10:
            self.image.clip_draw((int(self.frame) - 5) * 181 , 169, 185, 168, self.x, self.y)
        else:
            self.image.clip_draw((int(self.frame) - 10) * 181 , 0, 185, 168, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        pass