import rclpy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from rclpy.node import Node
import numpy as np
import random

class Retroalimentador(Node):

    global index 

    def __init__(self):
        super().__init__('Retroalimentador')
        self.subscription= self.create_subscription(Twist, 'IMU_info',self.listener_callback,10)
        self.publisher_ = self.create_publisher(Twist, 'response', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.matrix = np.zeros((10,6))
      

        self.index = 0

    def timer_callback(self):
        pendientes = derivadas(self.matrix, self.index)

        menores = {0:'xl menor', 1:'yl menor', 2:'zl menor', 3:'xa menor', 4:'ya menor', 5:'za menor'}
        mayores = {0:'xl mayor', 1:'yl mayor', 2:'zl mayor', 3:'xa mayor', 4:'ya mayor', 5:'za mayor'}
        
        for i in range(6):
            if (pendientes[i]<0):
                msg = Twist()
                msg.linear.x = float(random.randint(0,10))
                msg.linear.y = float(random.randint(0,10))
                msg.linear.z = float(random.randint(0,10))
                msg.angular.x = float(random.randint(0,10))
                msg.angular.y = float(random.randint(0,10))
                msg.angular.z = float(random.randint(0,10))
                self.publisher_.publish(msg)
            elif(pendientes[i]>0):
                msg = Twist()
                msg.linear.x = float(random.randint(0,10))
                msg.linear.y = float(random.randint(0,10))
                msg.linear.z = float(random.randint(0,10))
                msg.angular.x = float(random.randint(0,10))
                msg.angular.y = float(random.randint(0,10))
                msg.angular.z = float(random.randint(0,10))
                self.publisher_.publish(msg)
            else:
                pass

    def listener_callback(self,msg):
        self.index = (self.index + 1) % 5
        latest_values = np.array([msg.linear.x, msg.linear.y, msg.linear.z, msg.angular.x, msg.angular.y, msg.angular.z])
        self.matrix[self.index, :] = latest_values




def derivadas(matrix,i,k=10**-6):
    [f,c] = matrix.shape
    m=np.zeros(c)
    m=(matrix[:,i]-matrix[:,i+1])/k
    return m
    
    
                

def main(args = None):
    rclpy.init(args=args)
    Retro = Retroalimentador()
    rclpy.spin(Retro)
    Retro.destroy_node()
    rclpy.shutdown()
    


if __name__ == '__main__':
    main()
