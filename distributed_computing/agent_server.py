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
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'kinematics'))

from inverse_kinematics import InverseKinematicsAgent


class ServerAgent(InverseKinematicsAgent):
    '''ServerAgent provides RPC service
    '''
    # YOUR CODE HERE
    
    def get_angle(self, joint_name):
        '''get sensor value of given joint'''
        self.perception.join[joint_name]
        # YOUR CODE HERE
    
    def set_angle(self, joint_name, angle):
        self.target_joints[joint_name] = angle
        return 1
        '''set target angle of joint for PID controller
        '''
        # YOUR CODE HERE

    def get_posture(self):
        return self.posture
        '''return current posture of robot'''
        # YOUR CODE HERE

    def execute_keyframes(self, keyframes):
        return self.
        '''excute keyframes, note this function is blocking call,
        e.g. return until keyframes are executed
        '''
        # YOUR CODE HERE

    def get_transform(self, name):
        '''get transform with given name
        '''
        # YOUR CODE HERE

    def set_transform(self, effector_name, transform):
        '''solve the inverse kinematics and control joints use the results
        '''
        # YOUR CODE HERE
    def init_server():
        #register at dns
        server = SimpleXMLRPCServer(("localhost", 8000))
        print "Listening on port 8000..."
        server.register_function(get_angle, "get_angle")
        server.register_function(set_angle, "set_angle")
        server.register_function(get_posture, "get_posture")
        server.register_function(execute_keyframes, "execute_keyframes")
        server.register_function(get_transform, "get_transform")
        server.register_function(set_transform, "set_transform")
        server.serve_forever()
if __name__ == '__main__':
    agent = ServerAgent()
    agent.init_server()
    agent.run()

