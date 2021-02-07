# ros-tutorials

## Commands used by now:
         *  roscore - used to start master node  
         *  roscd - takes you to the working workspace declared last in the .bashrc 
         *  rosls - provides list of all programs in the particular location  
         *  create_pkg - used to create packages  
         *  rosrun - running ros nodes  
         *  rosnode - used to get certain information about particular nodes  
         *  rosnode cleanup - used to cleanup residual nodes still in memory  
                              rosnode cleanup  
         *  rosnode list - gives the list of all the active nodes  
                           eg: rosnode list  
         *  rostopic list - gives the list of all topics being used by the active nodes  
                            eg: rostopic list   
         *  rosnode info - provides info such as publishers, subscribers and services to a particular node  
                           eg: rosnode info /turtlesim  
         *  rostopic info - provides the subscribers and publishers to a given topic  
                            eg: rostopic info /turtle1/cmd_vel  
         *  rosmsg show - used to show contents used by a specific message  
                          eg: rosmsg show geometry_msgs/Twist
         *  rostopic echo - Displayes the published message on a specific topic
                            eg: rostopic echo /turtle1/cmd_vel                   
                            

### TurtleSim:
        * rosrun turtlesim turtlesim_node - to run the turtle sim node    
        * rosrun turtlesim turtle_teleop_key - to take commands from keyboard arrow keys
        * turtle_node is the subscriber and turtle_teleop_key is the publisher
        * if we do rosnode info /turtlesim:
                * we can see the topic of communication between them is cmd_vel
                * the msg sent in the topic is of type Twist under the package geometry_msgs
                * if you locate to the msg in the ros folder u can see the input of the msg
                  where it has 2 vector3 inputs (linear and angular)
                  where vector3 is itself a msg comprising of:
                        float64 x
                        float64 y
                        float64 z
        * rosmsg show geometry_msgs/Twist would give the info of a specific msg in this case (Twist)
          or rosmsg show standard_msgs/String
        * To publish a msg on a topic using cmd line : 
                              rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2, 4, 0]' '[0, 0, 3]'
          or : rostopic pub -r 10 /turtle1/cmd_vel geometry_msgs/Twist '{linear: {x: 1, y: 2, z: 0}, angular: {x: 0, y: 0, z: 1}}' 
          where '-r 10' is to repeat the operation 10 times.
        
#### RQT Graph:
        * use command rosrun rqt_graph rqt_graph while keeping turtlesim_node and teleop_key open
          // it gives a nice summary of the communication going on.
        * on running rosrun rqt_plot rqt_plot I get an error saying Aborted (core dumped)
          // Ideally it should return an x-y plotting of the turtle co-ordinates once the 
           "/turtle1/pose/x and /turtle1/pose/y" are provided as topics to the graph.
           
           
### Tips to Write a Publisher in ROS Topics:
        * Determine a Name for the Topic to Publish.
        * Determine type of msgs the Topic will Publish.
        * Determine the Frequency (how many msgs to publish per second).
        * Create a publisher object with chosen parameters.
        * Keep publishing the topic msgs at the selected Frequency.
        
        
### Tips to Write a Subscriber in ROS Topics:
        * Identify name of the topic to listen to (must match with the publisher).
        * Identift type of msg to be recieved (must match with the publisher).
        * Define a callback func. that is executed whenever a new msg is recieved.
        * Start listening for topic msgs.
        * Spin to listen forever (in C++).
        
        
## Writing Publisher node in Python:
        * To create a publisher node we first need a publisher Object using the cmd:
                rospy.publisher('topic name', Type of topic name, queue_size = x)
                        /* where x is an integer and queue_size is a buffer to store msgs
                           until the subscriber is ready to pull msgs from publisher.*/
                           (Higher value of x requires high memory storage)
        * Create and initialize a ROS Node:
                rospy.init_node('Name of Node', anonymous=True)
                        /* where anonymous=True signifies each Node with the given 
                           name would be unique and the Master would automatically
                           assign an ID tag to each node with the given name
                 
        
        * Publishing ROS message:
        
        
### Ex Code for python:
            import rospy
            from std_msgs.msg import String
            
            def talker():
                pub = rospy.publisher('chatter', String, queue_size = 10) # object pub created
                rospy.init_node('talker', anonymous=True)
                 rate = rospy.Rate(10) #10hz
                i = 0
                while not rospy.is_shutdown():              # while ROS is still running
                     hello_str = "hello world %s",%i     # creatig a msg
                     rospy.logininfo(hello_str)
                     pub.publish(hello_str)              # publishing the msg to pub using the publish method
                     rate.sleep()                        # rate.sleep is 1/Rate (in this case 0.1 since freq is 10 hz)
                     i=i+1
                     
            if __name__ == '__main__':
                try:
                        talker()
                except rospy.ROSInterruptException:
                        pass
                                
                        

## Writing Subscriber node in Python:
        
        * Create and initialize the Subscriber node:
                rospy.init_node('node name', anonymous=True)
                
        * Create a Subscriber Object:
                rospy.Subscriber("chatter", String, callback function)
        
        * Create a Subscriber callback function:
                def chatter_callback(message): # It takes the message recieved as parameter
                
        * Start Listening:
                rospy.spin()
                
        * Subscribing ROS message:
        `       
        
### Ex Code for Subscriber in python:
            import rospy
            from std_msgs.msg import String
                        
            def chatter_callback(message):
                rospy.logininfo(rospy.get_caller_id() + "I heard %s", message.data)
                               
            def listener():
                rospy.init_node('listener', anonymous=True)
                rospy.Subscriber("chatter", String, chatter_callback)
                rospy.spin()
                        
            if __name__ == '__main__':
                listener()
                        
            
