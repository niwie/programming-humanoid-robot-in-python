'''In this file you need to implement remote procedure call (RPC) server

* There are different RPC libraries for python, such as xmlrpclib, json-rpc. You are free to choose.
* The following functions have to be implemented and exported:
 * get_angle
 * set_angle
 * get_posture
 * execute_keyframes
 * get_transform
 * set_transform
* You can test RPC server with ipython before implementing agent_client.py
'''

# add PYTHONPATH
import os
import sys
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import pickle
import threading
import numpy as np
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'kinematics'))

#sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'joint_control'))

from inverse_kinematics import InverseKinematicsAgent


class ServerAgent(InverseKinematicsAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(ServerAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        
        p=os.path.abspath(os.path.join(__file__ ,"../.."))+'/joint_control/'
        self.posture = 'unknown'
        self.posture_classifier = pickle.load(open(p+'robot_pose.pkl'))  
        self.classes = os.listdir(p+'robot_pose_data')
    '''ServerAgent provides RPC service
    '''
    # YOUR CODE HERE
    
    def think(self, perception):
        self.posture = self.recognize_posture(perception)
        target_joints = self.angle_interpolation(self.keyframes, perception)
        self.target_joints.update(target_joints)
        return super(ServerAgent, self).think(perception)

    def recognize_posture(self, perception):
        
        posture = 'unknown'
        row=[]
        
        joints=['LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch']
        #append features
        for joint in joints:
            row.append(perception.joint[joint])
        #append x and y values
        row.append(perception.imu[0])
        row.append(perception.imu[1])

        data = []
        data.append(row)
        data = np.array(data)
        numeric_label=self.posture_classifier.predict(data)[0]
        posture=self.classes[numeric_label] #from perception predict posture
        #print (posture) 
        return posture




    def get_angle(self, joint_name):
        '''get sensor value of given joint'''
        return self.perception.joint.get(joint_name)
        #return self.perception.joint[joint_name]
        # YOUR CODE HERE
    
    def set_angle(self, joint_name, angle):
        if joint_name in self.perception.joint:
            self.target_joints[joint_name] = angle
        else:
            return "joint not in self.perception.joints"
        #return 1
        #errorcode should be thrown by rpchandler
        '''set target angle of joint for PID controller
        '''
        # YOUR CODE HERE

    def get_posture(self):
        return self.recognize_posture(self.perception)
        #self.posture=self.whatever().recognize_posture(self.perception)
        #return ("Posture", self.posture)
        

        '''return current posture of robot'''
        # YOUR CODE HERE

    def execute_keyframes(self, keyframes):
        #self.keyframes = pickle.loads(self.p+keyframes)
        
        self.keyframes=keyframes
        '''excute keyframes, note this function is blocking call,
        e.g. return until keyframes are executed
        '''
        # YOUR CODE HERE

    def get_transform(self, name):
        '''get transform with given name
        '''
        #return self.transforms[name]
        return self.local_trans(name,self.perception.joint[name])
        # YOUR CODE HERE

    def set_transform(self, effector_name, transform):
        '''solve the inverse kinematics and control joints use the results
        '''
        #return self.local_trans(name,self.perception.joint[name])
        self.set_transform(effector_name,transform)
        # YOUR CODE HERE



if __name__ == '__main__':

    agent = ServerAgent()
    server = SimpleXMLRPCServer(("localhost", 2212),allow_none=True)
    server.register_introspection_functions()
    server.register_instance(agent)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    #server.serve_forever()
    print ("Server on port 2212")
    agent.run()








#just there to copy and paste if needed:

    #server = SimpleXMLRPCServer(("localhost", 8000))
    #print "Listening on port 8000..."
    #server.register_function(get_angle, "get_angle")
    #server.register_function(set_angle, "set_angle")
    #server.register_function(get_posture, "get_posture")
    #server.register_function(execute_keyframes, "execute_keyframes")
    #server.register_function(get_transform, "get_transform")
    #server.register_function(set_transform, "set_transform")
    #server.serve_forever()
    

