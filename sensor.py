#!/usr/bin/env python2
# -*- coding: utf-8 -*-

random = 1
inline = 0
import natural_light as nl
import artificial_light as al
import paho.mqtt.client as mqtt
import json

class Sensor:
    
    def __init__(self, sid, position, distance, light):
        self.sid = sid
        self.position = position
        self.distance = distance #from wnd or from AL 
        if position == "w" : #the sensor sense the natural linght
            self.light_source = light
        else :
            self.light_source = light
    
        
    def read_lux(self, mode):
        if self.position == "w":
            if mode == 1 : #preset_value
                return self.light_source.get_lux()
            else:
                return self.light_source.set_lux(2) #user inserction
                
        if self.position == "t":
            return float(self.light_source.get_lux() / (self.distance*self.distance))

    
#a = al.Artificial_light("a", "a")
#a.update_lux(20)
#print a.get_lux()
    
    