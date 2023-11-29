"""
Scenario: You need to connect to external server to share some of your application data. 
You haven't to create a new instance from the connector class Each time you need to send 
your data to the External server. 
"""


class ServerConnector:
    """Simple connector class"""
    
    _is_instance = None
    
    def __new__(cls):
        if not cls._is_instance:
            cls._is_instance = super(ServerConnector, cls).__new__(cls)
            print("Connected Successfully!")
            return cls._is_instance
        else:
            print("You're already connected!")
            return cls._is_instance
        
    def connect(self):
        pass
            

if __name__ == '__main__':
    conn1 = ServerConnector().connect() # output: Connected Successfully!
    conn2 = ServerConnector().connect() # output: You're already connected!