import rclpy
import rclpy.client
import rclpy.publisher
from rclpy.node import Node
from .topic_service import Publisher, Subscriber, Client

class RCLPY_Handler:
    def __init__(self, node : str):
        rclpy.init()
        self.node = Node(node)
        self.connected = False

    def log(self, msg : str):
        self.node.get_logger().info(msg)

    def connect(self, rate: int = 5):
        self.connected = True
        self.log("rclpy connected!")
        rclpy.spin(self.node)

    def disconnect(self):
        if self.connected:
            self.log("Shutting down rclpy ...")
            self.node.destroy_node()
            rclpy.shutdown()
            self.connected = False

    def create_topic_publisher(self, topic: Publisher):
        topic.set_publisher(self.node.create_publisher(topic.get_type(), topic.get_name(), 10))
        
    def publish_topic(self, topic: Publisher, data):
        try:
            topic.get_publisher().publish(data)
        except Exception as e:
            self.log("Failed to publish to topic: " + topic.get_name())
            self.log(f"ERROR: {e}")

    def create_topic_subscriber(self, topic: Subscriber, function=None):
        if function == None:
            function = topic.set_data
        self.node.create_subscription(topic.get_type(), topic.get_name(), function, 10)

    def create_service_client(self, topic: Client):
        topic.set_client(self.node.create_client(topic.get_type(), topic.get_name()))

    def send_service_request(self, service: Client, data, timeout=30):
        try:
            srv = service.get_name()
            client = service.get_client()

            self.log(f"waiting for ROS service: {srv}")
            client.wait_for_service(timeout_sec=timeout)
            self.log(f"ROS service is up: {srv}")
            call_srv = client.call_async(data)
            return call_srv.result()
        except Exception as e:
            self.log("Failed to request service: " + srv)
            self.log(f"ERROR: {e}")