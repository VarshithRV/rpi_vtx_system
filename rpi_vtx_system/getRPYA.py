# node to get the roll pitch yaw and altitude
import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleAttitude, VehicleLocalPosition
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
import time, math, threading


class AttitudeAndPositionSubscriber(Node):
   
    def __init__(self):
        super().__init__('attitude_and_position_subscriber')
        self.altitude=float()
        self.roll=float()
        self.pitch=float()
        self.yaw=float()

        # qos profile init
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        
        # attitude sub
        self.subscription_attitude = self.create_subscription(
            VehicleAttitude,'fmu/out/vehicle_attitude',
            self.listener_callback_attitude,qos_profile=qos)
        self.subscription_attitude # prevent unused variable warning
        
        # position sub, will be used for altitude
        self.subscription_position = self.create_subscription(
           VehicleLocalPosition,'fmu/out/vehicle_local_position',
           self.listener_callback_position,qos_profile=qos)
        self.subscription_position # prevent unused variable warning

        # keep logging the RPY and altitude
        timer_period=0.05
        self.timer = self.create_timer(timer_period, self.logger)

    # function to log asynchronously
    def logger(self):
        # self.get_logger().info('Pitch: "%s", Roll: "%s", Yaw: "%s"' % (self.pitch, self.roll, self.yaw))
        self.get_logger().info("Altitude : %s"%self.altitude)
    
    
    # callback for attitude
    def listener_callback_attitude(self, msg):
        # self.get_logger().info('Pitch: "%s", Roll: "%s", Yaw: "%s"' % (msg.pitch, msg.roll, msg.yaw))
        # self.get_logger().info("Quaternion = %f" %msg.q[0])
        self.roll=math.atan2(
            2.0*(msg.q[0]*msg.q[1] + msg.q[3]*msg.q[2]), 
            msg.q[3]*msg.q[3] + msg.q[0]*msg.q[0] - 
            msg.q[1]*msg.q[1] - msg.q[2]*msg.q[2]
            )
        self.yaw=math.atan2(2.0*(
            msg.q[1]*msg.q[2] + msg.q[3]*msg.q[0]),
            msg.q[3]*msg.q[3] - msg.q[0]*msg.q[0] - 
            msg.q[1]*msg.q[1] + msg.q[2]*msg.q[2]
            )
        self.pitch = math.asin(-2.0*(msg.q[0]*msg.q[2] - msg.q[3]*msg.q[1]));

    # callback for altitude
    def listener_callback_position(self, msg):
        self.altitude=msg.z
        # self.get_logger().info('Altitude: "%s"' % self.altitude)
        # self.altitude=msg.z

def main(args=None):
   rclpy.init(args=args)
   attitude_and_position_subscriber = AttitudeAndPositionSubscriber()
   rclpy.spin(attitude_and_position_subscriber)

   attitude_and_position_subscriber.destroy_node()
   rclpy.shutdown()

if __name__ == '__main__':
   main()