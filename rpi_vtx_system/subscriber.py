import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class subscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        # create the subscription
        self.subscription = self.create_subscription(String, "topic", self.subscription_cb, 10)
        self.subscription
    def subscription_cb(self, msg):
        self.get_logger().info("I heard %s" %msg.data)

def main(args=None):
    rclpy.init(args=args)
    subscriber1=subscriber()
    rclpy.spin(subscriber1)
    subscriber1.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
