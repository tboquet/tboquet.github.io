A full data science configuration
#################################


:date: 2015-08-06 8:28
:category: Tutorials 
:tags: ubuntu, python, R 
:summary: Tools for data science 
:status: draft

Introduction
------------

Machine learning and data science are moving fast because we have more data and more opportunities to extract value from it. Researchers in the industry and the academia are finding new solutions to theoritical and applied problems `every day`_.

.. image:: https://avatars0.githubusercontent.com/u/2043492?v=3&s=200
   :height: 100
   :alt: Pelican


This technological ecosystem needs flexible and open source tools to evolve quickly with the help of a big community and we will see how we could follow this trend using the right software setup. This could be really important if you want to be efficient on complex (and even simple) problems.


OS choice
*********
I use the 14.04.3 LTS (Long Term Support) Ubuntu version because it's the most popular. When a lot of people are using a tool, you are sure to have a lot of answers to your questions on forums and in tutorials. That's a really good thing when you want to learn by yourself.

A lot of big data, data science, machine learning (call them what you want) are also using Ubuntu and it makes it one of the OS of choice when moving from a user point of vue to a developer point of vue.

Because we will use Docker and a realease is coming on Windows and OSX we will see that you don't need to install it on your hard drive.

Programming languages and tools
*********************************

The languages to work with data that you will see the most right now are Python and R. First, it's important to mention that these 2 languages are powerfull thanks to their very good package management systems and the community that supports all of these open source tools. Then, it's worth mentionning that a lot of packages are wrappers around C, C++, fortran or other languages softwares. It's an important point because these Python packages have to access compiled code or compile the code before they can be used.

This requirement leads to a lot of troubles with dependencies and compilers. 

For this reason, Anaconda is a good point to start installing easily already compiled packages.

My choice is to use Docker containers to always have a clean environment for my different projects.
This makes the need to install an eavy configuration on another computer or a server disapear.
With a well designed container, you just have to download it, run it and launch a Jupyter notebook to be ready to code.

Wrap up:
--------

**Why use Python?**

1. It's an **easy to read** and **simple** language
2. The syntax forces you to follow an interesting style
3. You could find a library that does **exactly what you want**
4. The machine learning community is **using it extensively**
5. The web developers community is **using it a lot too**
6. You have a Python community in each major city in the world
7. You could build a **whole analytic pipeline** only using Python
8. A lot of automation platforms support Python

**Why use R?**

1. It's the language used by a lot of **statisticians**
2. `Hadley Wickham`_
3. It's **really quick** to do some **simple stuffs**
4. Even if you like Python a lot, some packages are **more efficient in R**
5. You will see a lot of **MOOC** using R making it **easy to learn**


**Why use Docker**

1. Each time you rebuild a container, you have a clean configuration.
2. It's portable if you use a container located on Docker hub.
3. You can setup a new computer or server having Docker installed in 3 lines of code.
4. Much more complex setups could be built with Docker


Other stuffs:

- SAS: it's old, it's *not flexible*, it's used by banks and big corporations and **IT'S NOT FREE**
- SPSS: same thing, but used in marketing


Text editors
************

You have several good text editors and you should take a look at:

- emacs
- sublime text
- vim
- atom

I have used sublime text a lot and it's a really good editor to start with. The Spacemacs distribution of Emacs is now my favorite because it can emulate vim's behaviour.



.. _`Hadley Wickham`: http://had.co.nz/
.. _`every day`: http://arxiv.org/
