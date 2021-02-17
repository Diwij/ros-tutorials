# ros-tutorials

## Commands used by now:
   *  roscore - used to start master node 
   *  roscd - takes you to the working workspace declared last in the .bashrc 
   *  rosls - provides list of all programs in the particular location  
   *  create_pkg - used to create packages  
   *  rosrun - running ros nodes  
   *  rosnode - used to get certain information about particular nodes  
   *  rosnode cleanup - used to cleanup residual nodes still in memory  
          eg: rosnode cleanup  
   *  rosnode list - gives the list of all the active nodes  
          eg: rosnode list 
   *  rostopic list - gives the list of all topics being used by the active nodes  
          eg: rostopic list   
   *  rosnode info - provides info such as publishers, subscribers and services to a particular node  
          eg: rosnode info /turtlesim 
          
          
         rostopic info:
         
         ![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-01-17%2020-48-19.png "TurtleSim info")
   *  rostopic info - provides the subscribers and publishers to a given topic  
          eg: rostopic info /turtle1/cmd_vel  
   *  rosmsg show - used to show contents used by a specific message  
          eg: rosmsg show geometry_msgs/Twist
              
              
         
         rosmsg show:
         
         ![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-01-17%2020-45-01.png "Twist msg")
   *  rostopic echo - Displayes the published message on a specific topic
          eg: rostopic echo /turtle1/cmd_vel   
   
   *  rosservice list - Used to list all the active services.  
   *  rossrv show /(name of service)
   *  rossrv info /(name of service)
   *  rosservice call /(name of service) (args of service).
                            

### TurtleSim:
   * rosrun turtlesim turtlesim_node - to run the turtle sim node    
   * rosrun turtlesim turtle_teleop_key - to take commands from keyboard arrow keys
   * turtle_node is the subscriber and turtle_teleop_key is the publisher
   * if we do rosnode info /turtlesim:  
                * we can see the topic of communication between them is cmd_vel  
                * the msg sent in the topic is of type Twist under the package geometry_msgs  
                * if you locate to the msg in the ros folder u can see the input of the msg  
                * where it has 2 vector3 inputs (linear and angular)  
                * where vector3 is itself a msg comprising of:  
                    float64 x  
                    float64 y  
                    float64 z  
  * rosmsg show geometry_msgs/Twist would give the info of a specific msg in this case (Twist)  
      or rosmsg show standard_msgs/String  
  * To publish a msg on a topic using cmd line : 
      rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2, 4, 0]' '[0, 0, 3]'  
                
                
Turtle moving for 3 seconds by default:  

![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-01-17%2021-12-58.png "Moving Turtle")  

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
                 assign an ID tag to each node with the given name*/
                 
        
        * Publishing ROS message:
        
        
### Ex Code for python:
          #!/usr/bin/python
          import rospy
          from std_msgs.msg import String

          def talker():
              #create a new publisher. we specify the topic name, then type of message then the queue size
              new_pub = rospy.Publisher('chatter', String, queue_size=10)
              #we need to initialize the node
              # In ROS, nodes are uniquely named. If two nodes with the same
              # node are launched, the previous one is kicked off. The
              # anonymous=True flag means that rospy will choose a unique
              # name for our 'talker' node 
              rospy.init_node('talker', anonymous=True)
              #set the loop rate
              rate = rospy.Rate(1) # 1hz
              #keep publishing until a Ctrl-C is pressed
    
              while not rospy.is_shutdown():
                hello_str = "hello Diwij have a Good DAY" 
                rospy.loginfo(hello_str)
                new_pub.publish(hello_str)
                rate.sleep()

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
          #!/usr/bin/python
          import rospy
          from std_msgs.msg import String

          def chatter_callback(message):
              #get_caller_id(): Get fully resolved name of local node
              rospy.loginfo(rospy.get_caller_id() + " I heard %s", message.data)
    
          def listener():

            # In ROS, nodes are uniquely named. If two nodes with the same
            # node are launched, the previous one is kicked off. The
            # anonymous=True flag means that rospy will choose a unique
            # name for our 'listener' node so that multiple listeners can
            # run simultaneously.
            rospy.init_node('listener', anonymous=True)

            rospy.Subscriber("chatter", String, chatter_callback)

            # spin() simply keeps python from exiting until this node is stopped
            rospy.spin()

          if __name__ == '__main__':
              listener()

### Writing a Custom Message:    
  * go to your Catkin workspace and navigate to your workspace beginner_tutorials or  
    in my case ros_essentials_cpp
  * in the src folder create a folder with the name msg  
  * Open VSCode and navigate to the folder and create a file with the extension .msg
  * To see the structure of how a msg looks start roscore and type for eg: rosmsg show Twist
    this will display the components of the Twist msg similiarly you can create your own.  
    
  * The Custom message looks like this:
  
    ![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-02-16%2015-39-07.png)
  
  * For this custom message i had a Publisher:
  
    ![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-02-16%2015-39-31.png)  
  
  * Similairly a Subscriber:
  
    ![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-02-16%2015-39-03.png)
            
            
## Service and Parameters (Client-Server):
   * Unlike Publisher&Subscriber communication which is continuous Service is a One time communication
      which consists of a Client and a Server.
   * The Client would send a request to the server for a particular Action and the server would Respond.
   * The Communication is completely synchronous!
   * It is Bi-directional communication unlike Topics which is One-way.
    
    
### Ros-Services and TurtleSim:
   * Start roscore
   * Run TurtleSim
   * Type rosservice list to see lit of running services.
   * Just like "rosnode info /" we can do rosservice info /name_of_service to get info about the service.  
   * eg: rosservice info /spawn (This is one of the services available when you run TurtleSim).
   
   
   ![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-02-16%2016-32-00.png)   
   
   
   * What Info we get:  
        * The Service is provided by the Node turtlesim.    
        * It is available on the following URI (Uniform resource identifier).  
        * The message exchanged is of type spawn.(But if we do rosmsg show turtlesim/spawn we get nothing).    
        * In case of service we have a request and a response so we have a service message and a  
          response message .  
        * Args are the arguments contained in the request message.  
        
        
  * In place of rosmsg show to get info of the service and request message we can do:      
    
       rossrv info turtlesim/Spawn    
       or  
       rossrv show turtlesim/Spawn
          
      ![](https://github.com/Diwij/ros-tutorials/blob/main/Images/Screenshot%20from%202021-02-16%2016-55-47.png)   
              * The first 3 fields returned are the position of the new turtle to be spawned in the request message.  
              * Name is the name specified by the user of the turtle as request.  
              * The Name field in the last is the name of the turtle returned by the Server.  
              
  * To use a service available we need to call the service suing rosservice call /name_of_service args.  
    eg: rosservice call /spawn 5 6 0 Turtle2 // Here 5&6 are the x & y coordinates in the turtleSim window,  
    0 is the spawn angle about z-axis, Turtle2 is the name of the turtle to be spawned sent by the request.  
    
    The value returned after sending the request is name: "Turtle2".
         
    
