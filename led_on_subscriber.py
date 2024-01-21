import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# create minimal subscriber node
class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'command', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    # callback function for subscriber
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)