#!/usr/bin/env python2

import json

import paho.mqtt.client as mqtt

import time

ip = "localhost"
WND_VAL = 0
WND_CNT = 2
TAB_VAL = 1
TAB_CNT = 3
port = 1883
number_of_sensors=0
threshold = 6000 #lumen converted
meas = {}

def analisys_for_nl(meas, sid, position, value):
    if position == 'w':
        meas[str(sid)][WND_VAL] = value
        meas[str(sid)][WND_CNT] +=1
def analisys_for_al(meas, sid, position, value):
    print value
    if value < threshold:
        #check in class if it is possible
        meas[str(sid)][TAB_VAL] = 20 #increment of 20 lumen
        meas[str(sid)][TAB_CNT] += 1
    else: #decrement if there are too much lumen on table 
        meas[str(sid)][TAB_VAL] = -20 #increment of 20 lumen
        meas[str(sid)][TAB_CNT] += 1

def broker_connection(ip, port):
    def on_connect (client, userdata, rc):
        print "Controller connected with result code " + str(rc)

    def on_subscribe(self, client, userdata, mid):
        print "Controller subscripted"       

    def on_publish(client, userdata, mid):
#        print "OP ->  " + str(mid) + " <-"
        return          

    def on_message(client, userdata, msg):
#        print str(msg.topic) + " controller"
        m = json.loads(msg.payload) # {u'position': u'w', u'id': u's1', u'value': 304}
        print str(m['position'])+" - "+ str(m['value']) +  " controller"

        if m['position'] == 'w':
            analisys_for_nl(meas, m['id'], m['position'], int(m['value']))
        else :
            lumen_value =  int(m['value']) + meas[m['id']][WND_VAL]
            analisys_for_al(meas, m['id'], m['position'], lumen_value) 
        
        sendable = True
        for key in meas.keys():
            if meas[key][WND_CNT] == 0 or meas[key][TAB_CNT] == 0:
                sendable = False
        
        
        if sendable == True:
            msg = json.dumps(meas)
#            print msg
            for key in meas.keys():
                meas[key][WND_CNT] = 0 
                meas[key][TAB_CNT] = 0
            my_client.publish("/room1/commands/", msg)
            time.sleep(1)
        return

        
    client = mqtt.Client("controller")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

    client.connect(ip, port)
    
    return client

def sensor_subscriptions():
    global number_of_sensors
    my_client.subscribe("/s1/w/value/")
    my_client.subscribe("/s1/t/value/")
    number_of_sensors +=1

def initialize_data():
    for i in range (1,number_of_sensors+1):
        l = [0,0,0,0] # wnd val, t val, wnd count, table count -> format
        meas['s'+str(i)] = l

if __name__ == "__main__":
    my_client = broker_connection(ip,port)   
    sensor_subscriptions()
    initialize_data()
    
    
    my_client.loop_forever()
    
    
    

    
