'''In this exercise you need to use the learned classifier to recognize current posture of robot

* Tasks:
    1. load learned classifier in `PostureRecognitionAgent.__init__`
    2. recognize current posture in `PostureRecognitionAgent.recognize_posture`

* Hints:
    Let the robot execute different keyframes, and recognize these postures.

'''


from angle_interpolation import AngleInterpolationAgent

#from keyframes import __init__
from keyframes import hello, leftBellyToStand, leftBackToStand, rightBellyToStand, rightBackToStand, wipe_forehead
import pickle
from os import listdir, path
import numpy as np


class PostureRecognitionAgent(AngleInterpolationAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(PostureRecognitionAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.posture = 'unknown'
        self.posture_classifier = pickle.load(open('robot_pose.pkl')) #load classifier from file
        self.classes = listdir('robot_pose_data')

    def think(self, perception):
        self.posture = self.recognize_posture(perception)
        return super(PostureRecognitionAgent, self).think(perception)

    def recognize_posture(self, perception):
        
        posture = 'unknown'
        row=[]
        #not all of the joints needed? 
        #joints=self.joint_names:'LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'RHipYawPitch', 'RHipRoll', 'RHipPitch', 'RKneePitch', 'AngleX', 'AngleY']
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

if __name__ == '__main__':
    agent = PostureRecognitionAgent()
    #agent.keyframes = hello()
    agent.keyframes = rightBackToStand()  # CHANGE DIFFERENT KEYFRAMES
    agent.run()
