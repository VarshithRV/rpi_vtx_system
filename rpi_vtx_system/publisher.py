import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class publisher(Node):
    def __init__(self):
        super().__init__('Basic_publisher')
        self.publisher = self.create_publisher(String,"topic",10)
        timer_period = 0.5#seconds
        self.timer=self.create_timer(timer_period,self.timer_callback)
        self.i=0

    def timer_callback(self):
        msg=String()
        msg.data="Hello world %d" % self.i
        self.publisher.publish(msg)
        self.get_logger().info('"Publishing %s"' % msg.data)
        self.i+=1

def main(args=None):
    rclpy.init(args=args)
    publisher_=publisher()
    rclpy.spin(publisher_)
    publisher_.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()