import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
import random


class Acelerometro(Node):
    
    def __init__(self):
        super().__init__('acelerometro')
        self.publisher_ = self.create_publisher(Twist, 'topic', 10)
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):
        msg = Twist()
        msg.linear.x=float(random.randint(0,10))
        msg.linear.y=float(random.randint(0,10))
        msg.linear.z=float(random.randint(0,10))

        msg.angular.x=float(random.randint(0,10))
        msg.angular.y=float(random.randint(0,10))
        msg.angular.z=float(random.randint(0,10))

        self.publisher_.publish(msg)
    


def main(args = None):
    rclpy.init(args=args)
    nodo = Acelerometro()
    rclpy.spin(nodo)
    #nodo.destroy_node()
    rclpy.shutdown()
    


if __name__ == '__main__':
    main()
