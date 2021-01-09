# ros-tutorials

## Commands used by now:
         * roscore - used to start master node
         * roscd - takes you to the working workspace declared last in the .bashrc
         * rosls - provides list of all programs in the particular location
         * create_pkg - used to create packages 
         * rosrun - running ros nodes
         * rosnode - used to get certain information about particular nodes
         * rosnode cleanup - used to cleanup residual nodes still in memory
         * rosnode list - gives the list of all the active nodes
         * rostopic list - gives the list of all topics being used by the active nodes
         * rosnode info - provides info such as publishers and subscribers to a particular node
         
         

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
            
           
            
