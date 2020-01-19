'''In this file you need to implement remote procedure call (RPC) client

* The agent_server.py has to be implemented first (at least one function is implemented and exported)
* Please implement functions in ClientAgent first, which should request remote call directly
* The PostHandler can be implement in the last step, it provides non-blocking functions, e.g. agent.post.execute_keyframes
 * Hints: [threading](https://docs.python.org/2/library/threading.html) may be needed for monitoring if the task is done
'''

import weakref
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

import pickle
import os
import sys
import threading
import numpy as np
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'joint_control'))
from keyframes import hello

class PostHandler(object):
    '''the post hander wraps function to be excuted in parallel
    '''
    def __init__(self, obj):
        self.proxy = weakref.proxy(obj)

    def execute_keyframes(self, keyframes):
        '''non-blocking call of ClientAgent.execute_keyframes'''
        thread = threading.Thread(target=self.proxy.execute_keyframes, args=[keyframes])
        thread.start
        # YOUR CODE HERE

    def set_transform(self, effector_name, transform):
        '''non-blocking call of ClientAgent.set_transform'''
        thread = threading.Thread(target=self.proxy.set_transfrom, args=[effector_name, transform])
        thread.start
        # YOUR CODE HERE


class ClientAgent(object):
    '''ClientAgent request RPC service from remote server
    '''
    # YOUR CODE HERE
    def __init__(self):
        self.post = PostHandler(self)
        self.proxy = xmlrpclib.ServerProxy('http://localhost:2212')
    
    def get_angle(self, joint_name):
        '''get sensor value of given joint'''
        # YOUR CODE HERE
        try:
            return self.proxy.get_angle(joint_name)
        except xmlrpclib.Fault as err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString
    
    def set_angle(self, joint_name, angle):
        try:
            self.proxy.set_angle(joint_name, angle)
        except xmlrpclib.Fault as err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString
    
        '''set target angle of joint for PID controller
        '''
        # YOUR CODE HERE

    def get_posture(self):
        #return value!
        try:
            return self.proxy.get_posture()
        except xmlrpclib.Fault as err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString
    '''return current posture of robot'''
        # YOUR CODE HERE

    def execute_keyframes(self, keyframes):
        try:
            self.proxy.execute_keyframes(keyframes)
        except xmlrpclib.Fault as err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString
    
        '''excute keyframes, note this function is blocking call,
        e.g. return until keyframes are executed
        '''
        # YOUR CODE HERE

    def get_transform(self, name):
        try:
            return self.proxy.get_transform(name)
        except xmlrpclib.Fault as err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString
    '''get transform with given name
        '''
        # YOUR CODE HERE

    def set_transform(self, effector_name, transform):
        #return
        try:
            self.proxy.set_transform(effector_name,transform)
        except xmlrpclib.Fault as err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString
    '''solve the inverse kinematics and control joints use the results
        '''
        # YOUR CODE HERE

if __name__ == '__main__':
    agent = ClientAgent()
    #oncomment different line if you want to test
    T


    #test get and set angle
    #print agent.get_angle('HeadYaw')
    agent.set_angle('HeadPitch', 9.4)
    #print agent.get_angle('HeadYaw')
    #test posture recog
    #print ("get_posture returns:",agent.get_posture())
    
    #print ("executing keyframe 'hello' ")
    #agent.execute_keyframes(hello())
    #print ("get_posture returns:",agent.get_posture())
    #test tranform
    #print ("get_transform returns:",agent.get_transform('RHipPitch'))

    #transform = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    #agent.set_transform('HeadPitch', transform)

    #posthandler= PostHandler(agent)
    #print "keyframe: v2"
    #posthandler.execute_keyframes(hello())

    #print "set tranform: v2"
    #posthandler.set_transform('RHipPitch', transform)

    #@ TODO


    #test set transform and post handlermust be implemented and test together with bugfixes!!!!


    # TEST CODE HERE


