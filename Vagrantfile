# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.


Vagrant.configure("2") do |config|
  #standard configuration block that's required in all vagrant files


 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.

 config.vm.box = "ubuntu/bionic64"
 #we've also left the config.vm.box setting to Ubuntu/Bionic64

 config.vm.box_version = "~> 20200304.0.0"
 #pinned it to a specific version and this is to avoid any changes/updates being made to this image breaking the steps

 config.vm.network "forwarded_port", guest: 8000, host: 8000
 #Maps a port from local machine to the machine on our server
#host machine is our laptop (whichever machine you're running the development server on)
#guest machine is the development server itself
# default ports are not automatically accessible on any guest machine so you need to add this line


#this is how you can run scripts; when you first create your server I've added some commands to the script
 config.vm.provision "shell", inline: <<-SHELL
   systemctl disable apt-daily.service #to disable the auto update which conflicts with this auto update when we first run it on Ubuntu}
   systemctl disable apt-daily.timer

   sudo apt-get update #update the local repository with all of the available packages
   sudo apt-get install -y python3-venv zip # install Python 3 virtual env and zip tool (create compressed zip files)
   touch /home/vagrant/.bash_aliases #create a bash aliases file
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then #set Python 3 to the default Python version for our vagrant user
   #every time you run Python it will automatically use Python 3 instead of the default Python 2.7 
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
 SHELL
end
