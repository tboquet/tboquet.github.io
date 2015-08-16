Ubuntu installation and configuration
#####################################


:date: 2015-08-06 8:28
:category: Tutorials 
:tags: ubuntu, setup, installation 
:summary: Install and configure your system 


Prerequisite
------------
You will need a 2gb usb key and 35 minutes to complete this tutorial and enjoy Ubuntu.

Introduction
------------

If you are here you maybe want to install a new OS but first you maybe want to know if is complicated and how long it will take.
We will go through:

1. The installation of the OS (15 minutes)
2. A few command line tools that you will use (10 minutes)
3. The customization of some elements in Ubuntu (10 minutes)

Within 35 minutes, you should be able to run your new OS with a descent customization and know some fancy command line tools to install new software on your machine.


Installation
--------------

For this part, I have aggregated quickly some tutorials ([1]_, [2]_). I'll try to be explicit, and if it's not enough, the sources are at the end of the article for more details.

1. create an usb bootable stick
2. erase it all and allocate some space for the important part of the os
3. put some infos and click on some buttons
4. look at the progress bar and reboot
5. enjoy Ubuntu

Bootable usb stick
*******************

(For this part I will assume that you are running Windows)

First you have to download the latest `Ubuntu iso image`_ and the `Pendrive Linux universal USB installer`_.
When you have both files run the Pendrive installer and follow these instructions:
Before going further note that this operation will format your usb key and you need to save your files.

1. Select the **Ubuntu** from the dropdown list

.. image:: images/mcplaceholdermin.jpg 
   :height: 300
   :alt: Pelican
   :align: center

2. Click **browse** and open the ISO file you just downloaded

.. image:: images/mcplaceholdermin.jpg
   :height: 300
   :alt: Pelican
   :align: center


3. Choose your USB drive and click on **create**

.. image:: images/mcplaceholdermin.jpg
   :height: 300
   :alt: Pelican
   :align: center



Installation
*************

In this section, you have 2 options:

- Format your disk and install Ubuntu
- Install Ubuntu alongside with Windows

Choose the first option if you really need Windows for some applications and if you have enough storage (minimum 500 gigabytes on your primary disk or 2 separate disks).


Only Ubuntu
````````````

Now is the time to clean up your disk and install your new OS.
If you have some personal files hidden somewhere, now is the good time to save them on a external hard drive or another usb stick.

When it's done we begin by giving the system some basic information. At the fourth step you will have to choose an installation method:

.. image:: images/ubuntu_tuto/KURnS.png
   :height: 400
   :alt: Installation method
   :align: center


We will manually allocate some space for some parts of the OS to have enough space for large folders (like several loaded virtual environments in Python).
To do so, select **something else** and click on continue.








Infos
*****



Reboot
*******

Enjoy
******

You should be able to see this screen:


Explore your new environment a bit and search on the internet if you want some information.

Command line tools
------------------

First you should learn how to install new programs from the command line.
It will be important because a lot of tools have to be installed this way.

Press `CTL-ALT-T` to open a new terminal.

.. image:: images/mcplaceholdermin.jpg 
   :height: 300
   :alt: Pelican
   :align: center

 
(or press the `CMD` key and type 'terminal')

.. image:: images/mcplaceholdermin.jpg
   :height: 300
   :alt: Pelican
   :align: center


(or click on the 'search your computer' button situated at the top left corner of your screen)

.. image:: images/mcplaceholdermin.jpg
   :height: 300
   :alt: Pelican
   :align: center



When you have your terminal opened 

.. [1] I took the steps from `Ubuntu's tutorial`_ for the usb stick part.
.. [2] The images in the installation steps are from this question from askubuntu_.

.. _`Ubuntu's tutorial`: http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows
.. _`Pendrive Linux universal USB installer`: http://www.pendrivelinux.com/downloads/Universal-USB-Installer/Universal-USB-Installer-1.9.6.1.exe
.. _`Ubuntu iso image`: http://www.ubuntu.com/download/desktop
.. _askubuntu: http://askubuntu.com/questions/343268/how-to-use-manual-partitioning-during-installation
