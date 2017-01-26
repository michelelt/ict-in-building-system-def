#!/usr/bin/env python2
# -*- coding: utf-8 -*-

##this class simulate a single artificial dimmerable lighting system##

import paho.mqtt.client as mqtt
import json

WND_VAL = 0
WND_CNT = 2
TAB_VAL = 1
TAB_CNT = 3


class Artificial_light:
    
    def __init__(self, alid, name):
        self.name = name
        self.alid = alid
        self.artificial_light=250 #expressed in lumen
        self.max_lumen = 2700
        
    def get_lux (self):
        return self.artificial_light
        
    def update_lux(self,value):
        new_value = self.artificial_light + value
        if new_value > self.max_lumen or new_value < 0:
            return
        else:   
            self.artificial_light += value
            
    def set_lux (self):
        self.artificial_light = 740