'''In this file you need to implement remote procedure call (RPC) client

* The agent_server.py has to be implemented first (at least one function is implemented and exported)
* Please implement functions in ClientAgent first, which should request remote call directly
* The PostHandler can be implement in the last step, it provides non-blocking functions, e.g. agent.post.execute_keyframes
 * Hints: [threading](https://docs.python.org/2/library/threading.html) may be needed for monitoring if the task is done
'''

import weakref

class PostHandler(object):
    '''the post hander wraps function to be excuted in parallel
    '''
    def __init__(self, obj):
        self.proxy = weakref.proxy(obj)

    def execute_keyframes(self, keyframes):
        '''non-blocking call of ClientAgent.execute_keyframes'''
        # YOUR CODE HERE

    def set_transform(self, effector_name, transform):
        '''non-blocking call of ClientAgent.set_transform'''
        # YOUR CODE HERE


class ClientAgent(object):
    '''ClientAgent request RPC service from remote server
    '''
    # YOUR CODE HERE
    def __init__(self):
        self.post = PostHandler(self)
    
    def get_angle(self, joint_name):
        '''get sensor value of given joint'''
        # YOUR CODE HERE
        try:
            self.post.proxy.get_angle(joint_name)
        except xmlrpclib.Fault as err:
        print "A fault occurred"
        print "Fault code: %d" % err.faultCode
        print "Fault string: %s" % err.faultString
    
    def set_angle(self, joint_name, angle):
        try:
            self.post.proxy.set_angle(joint_name)
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
            self.post.proxy.get_posture()
        except xmlrpclib.Fault as err:
        print "A fault occurred"
        print "Fault code: %d" % err.faultCode
        print "Fault string: %s" % err.faultString
    '''return current posture of robot'''
        # YOUR CODE HERE

    def execute_keyframes(self, keyframes):
        try:
            self.post.proxy.execute_keyframes(keyframes)
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
            self.post.proxy.get_transform(name)
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
            self.post.proxy.set_transform(effector_name,transform)
        except xmlrpclib.Fault as err:
        print "A fault occurred"
        print "Fault code: %d" % err.faultCode
        print "Fault string: %s" % err.faultString
    '''solve the inverse kinematics and control joints use the results
        '''
        # YOUR CODE HERE

if __name__ == '__main__':
    agent = ClientAgent()
    # TEST CODE HERE


