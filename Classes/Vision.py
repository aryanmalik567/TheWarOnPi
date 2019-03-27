from pixy import *
from ctypes import *
import time as t

number = 2
class Blocks(Structure):
    _fields_ = [("type", c_uint),
                ("signature", c_uint),
                ("x", c_uint),
                ("y", c_uint),
                ("width", c_uint),
                ("height", c_uint),
                ("angle", c_uint)]

class Vision():
    def __init__(self):
        pixy_init()
        self.blocks = BlockArray(number)
        frame = 0
    def get_block(self):
        blocks = self.blocks
        count = pixy_get_blocks(number, self.blocks)
        return [(blocks[index].type, blocks[index].signature,
                 blocks[index].x, blocks[index].y, blocks[index].width,
                 blocks[index].height) for index in range(0,count)
                 ]