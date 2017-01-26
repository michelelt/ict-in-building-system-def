#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random

class Natural_light :
    
    def __init__(self):
#        self.natural_light = random.randint(0, 1200)
        self.natural_light = 40000
        
    def get_lux(self):
        return self.natural_light
    
    def set_lux(self):
        self.natural_light = eval(input('Insert the lux value'))
        return
