import rclpy
import rclpy.client
import rclpy.publisher
import rclpy.subscription

class ROS_Service:
    def __init__(self, name : str, class_type, usage_type : str):
        self.__name = name
        self.__class_type = class_type
        self.__usage_type = usage_type

    def get_type(self):
        return self.__class_type

    def get_name(self):
        return self.__name
    
    def get_usage_type(self):
        return self.__usage_type


class Publisher(ROS_Service):
    
    def __init__(self, name: str, class_type):
        super().__init__(name, class_type, "publisher")

    def set_publisher(self, publisher : rclpy.publisher.Publisher):
        self.__publisher = publisher

    def get_publisher(self) -> rclpy.publisher.Publisher:
        return self.__publisher

class Subscriber(ROS_Service):

    def __init__(self, name: str, class_type):
        super().__init__(name, class_type, "subscriber")
        self.__data = None

    def set_subscription(self, subscription : rclpy.subscription.Subscription):
        self.__subscription = subscription

    def get_subscription(self) -> rclpy.subscription.Subscription:
        return self.__subscription

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        data = self.__data
        self.__data = None
        return data

    def get_data_last(self):
        return self.__data

class Client(ROS_Service):

    def __init__(self, name: str, class_type):
        super().__init__(name, class_type, "client")
    
    def set_client(self, client : rclpy.client.Client):
        self.__client = client

    def get_client(self) -> rclpy.client.Client:
        return self.__client
