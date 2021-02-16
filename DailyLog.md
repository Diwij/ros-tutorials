### Jan 5, 2021

    1. Tried Packages after watching Tutorials from RSL and Guide from Ros WIKI.
       Getting some "CMAKE error" and "Invoking Cmake Failed" 
       //I am able to change my working directory to the catkin workspace its 
       Just CMAKE giving the trouble
       
    2. From the video Tutorials tried the tutorial thing with the hello world 
       and then i heard hello world along with printing my own mesaage with my 
       Name (No errors there working fine) 
       // this was done without using a catkin workspace
       
### Jan 8, 2021
    
    1. The CMAKE error was not being solved (when i checked it up most
       solutions required re-installing) when updating the workspace so i 
       used catkin_make instead to update the workspace but even that was 
       giving some errors which were easily resolved by updating a function 
       of openCV in the library which was one used in a previous version.
       Updating in to the current version did the job this was only the first 
       when i made the workspace ig the function was imread which i corrected
       mostly.
       
    2. After setting up the workspace and all I tried up with the basic
       Talker and Listener nodes, Tried the turtle sim, create packages.
    
    3. Also added the workspace to the .bashrc file but when i access the
       direcory for ros instead of going to the workspace I am re-directed 
       to the location where ROS is stored (need to check this)
       
    4. Also read a bit about dependencies when creating packages.
    
    5. Apart from this I am doing a course of it from UDEMY by Aneas Kouba
       started with the communication protocols 3 types
            * publisher-subscriber
            * client-server
            * action-action something (just a mention for now)
            
    6. Using TurtleSim and the teleop node     
    
### Jan 10,2021

    1. Understanding structure of messages sent by the publisher to the
       subscriber
       /* genereal example geometry_msgs/Twist(used in turtle sim)
          where geometry_msgs is the package where the msg is located
          and Twist is the type of msg used for communication, where
          twist defines the linear and angular velocities along the 3 Axes.*/
          
### Jan 19,2021
    1.  Understanding Subscriber/Publisher communication:
                *Firstly we declare a subscriber which declares the topics
                 of its subscription the type of msg it will recieve to the 
                 ros master node.
                *Then we declare a publisher which will have the same topic
                 as the subscrber to subscribe to and will send the msg of 
                 similiar type.
                *The ROS Master node will then let the subscriber know of the 
                 presence of a publisher with compatible topics and msgs.
                *The subscriber then sends a TCP request to the publisher to
                 create a connection and the publisher sends a response to
                 establish that connection.
                *This process happens before transmission of any DATA.
                *Once the communication is set up Transmission of msgs can 
                 take place over Topics.
                 
    2.  Once a successful Communication has been set between 2 nodes even if 
        the ROS Master node crashes the communication is not disrupted. Only 
        if the nodes are closed then restarting communication won't be possible
        without ROS Master.
        
    3.  Writing Publisher and Subscriber in Python
    

### Feb 15,2021
    1.  The codes written for publisher/subscriber for a custom talker-listener
        worked fine. A little blunder in the turtleSim velocity sender was done.
        
    2.  Wrote a custom message (CustomMsg.msg) with 4 fields (name, age, gender 
        and marks).
        
    3.  Updated CMake list and package.xml file accordingly
    
    4.  Wrote a custom Publisher and Subscriber for that message where the 
        publisher would send random marks b/w 75 and 99 to the subscriber
        with the rest of the data constant.
        
    5.  The data was sent every 5 secs i.e. the rate was set at 0.2 Hz.  
    
### Feb 16, 2021  
    1.  Started Service-Parameter (Client-Server).
    2.  service list on turtlesim
    3.  spawning turtle on turtlesim using request.
