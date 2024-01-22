# create simple subscriber to subscribe to the topic command
# when a message is received it turns the gpio pin 10 to 1 and 9 to 0
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'command', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        GPIO.output(10, 1)
        GPIO.output(9, 0)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()
    # turn off gpio pins
    GPIO.output(10, 0)
    GPIO.output(9, 0)
    # cleanup gpio
    GPIO.cleanup()

# run main function
if __name__ == '__main__':
    main()