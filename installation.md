
  <h2>Installing Virtualbox on Windows 10</h2>
  A virtualbox (VB) gives you the ability to install several operating systems (OS) in your device. You need to download the latest version that is compatible with your device and it setup. [Download Link.](https://www.oracle.com/virtualization/technologies/vm/virtualbox.html)


  <h2>Installing Ubunto on VB</h2>
  Ubunto is the operating system that we will be using, it is linux based and you can download the Ubunto Desktop 20.04 from [here.](https://ubuntu.com/#download) Then we open the virtualbox,  choose new and type Ubunto. We will refer to the OS file that we just downloaded in the installation steps.
 I followed the steps from [this website](https://brb.nci.nih.gov/seqtools/installUbuntu.html) and have Ubunto running as showen in the picture below:  
 
![enter image description here](https://github.com/Jumana5/Smart-Methods-AI-Training/blob/master/ubunto.PNG)
  <h2>Installing ROS on Ubuntu</h2>
  Following the steps from [this Udemy Course.](https://www.udemy.com/course/ros-basics-program-robots/learn/lecture/8892584#overview) , I installed the ROS Noetic which is the version that is  compatible with Ubunto 20.04. 
  The refernce to the installation steps is [here.](http://wiki.ros.org/noetic/Installation/Ubuntu) 

  <h2>Installing Python</h2>
  <p> Checking if python in the system by typing 

      python --version

  Since Ubuntu is the latest version, python is downloaded by default. Trying:

      python3 --version

  Now we need the package manager pip for python3. To install type the following lines in the terminal: 

      sudo apt update
      sudo apt install python3-pip

  </p>
  <h2>Installing OpenCV</h2>
  <p>
  OpenCV stands for Open Source Computer Vision Library, and to install this library, type in the terminal:
  

    pip3 install python-opencv

  </p>
  <h2>Installing an IDE</h2>
 <p>
  In order to write the code in a syntax friendly environment, we need to download an IDE (Interface Development Environment). Pycharm is one of the top IDEs for Python development. So to install it in UBuntu, type the following line in the terminal: 

    sudo snap install pycharm-community --classic

  </p>
  <h2>Installing GitHub Desktop on Ubunto</h2>
<p>
  Install GitHub .snap package from [Here](https://github.com/shiftkey/desktop/releases/tag/release-2.0.4-linux1)
 
 Then type in the terminal: 

      snap install ~/Downloads/GitHubDesktop-linux-2.0.4-linux1.snap --classic --dangerous

  Then install git in the system
 

     sudo-apt install git

  Last but not least, if you are using a cloned project in pycharm, you need to configure the Version Control settings.


