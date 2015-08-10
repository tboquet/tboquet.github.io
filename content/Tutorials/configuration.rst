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


This technological ecosystem needs flexible and open source tools to evolve quickly with the help of a big community and we will see how we could follow this trend using the right software setup. This could be really important if you want to be efficient on some complex problems.


OS choice
*********
I use the 14.04.3 LTS (Long Term Support) Ubuntu version because a lot of people use it. When a lot of people are using a tool, you are sure to have a lot of answers to your questions on forums and in tutorials. That's a really good thing when you want to learn by yourself.

A lot of big data, data science, machine learning (call them what you want) are also using Ubuntu and it makes it one of the OS of choice when moving from a user point of vue to a developer point of vue.

Programming languages and tools
*********************************

In this tutorial, we will use Python and R. When we say use, it's more like writing Python and R calling some low level compiled C, C++ or Fortran libraries.

**Why use Python?**

1. It's a **beautiful** and **simple** language
2. It forces you to use a specific indentation and it's good in a **learning phase** and to write **reusable code**
3. You could find a library that does **exactly what you want**
4. The machine learning community is **using it extensively**
5. The web developers community is **using it a lot too**
6. You have a Python community in each major city in the world!
7. You could build a **whole analytic pipeline** only using Python

**Why use R?**

1. It's the language used by a lot of **statisticians**
2. `Hadley Wickham`_ (Yeah, this guy)
3. It's **really quick** to do some **simple stuffs**
4. Even if you like Python so much, some packages are **1000 times more efficient in R** (because it involves a lot more C, C++ and Fortran)
5. You will see a lot of **MOOC** using R making it **easy to learn**

Other stuffs:

- SAS it's old, it's *not flexible*, it's used by banks and big corporations and **IT'S NOT FREE**
- SPSS: same thing, but used in marketing


Text editors
************

You have several good text editors and you should take a look at:

- emacs (hipster, old school #1)
- sublime text (hipster, mad jojo #2)
- vim (old school, super hero #3)
- atom (fairly new, it seems nice)

I used sublime text a lot and it's a really good editor to start with. Emacs is now my favorite, due to it's awesome features (again, it's really hipster). You could also emulate vim behavior in emacs to become a superpowered old school hipster.


Utilies and system libraries
*****************************
git, htop, compilers, BLAS

To be able to install, download and do some fancy stuffs, we need packages. To install a package, you could use the magic `sudo apt-get install name-of-your-awesome-package` like this:

```bash
sudo apt-get install htop
```
Ubuntu will ask you if you are sure you want to install it, we love htop so hit `y` and `RET` (return).
After you get back the control of your terminal, we can verify that the program is working:

```bash
htop
```

.. image:: https://avatars0.githubusercontent.com/u/2043492?v=3&s=200
   :height: 100
   :alt: Pelican


Nice! If you are in a cafe, you look like a real baddass programmer.

.. image:: https://avatars0.githubusercontent.com/u/2043492?v=3&s=200
   :height: 100
   :alt: Pelican


For some packages we need to tell Ubuntu where to search for it on the internet. Ubuntu has some repositories from which it downloads source files from. You just have to add the adresses to search for these pieces of software to download, update and upgrade them.

For this, you need to `TODO ppa`

ZSH
***

The command line tool you need. `sudo apt-get` it:

```bash
sudo apt-get zsh
```
and `git clone` the awesome *oh-my-zsh* custom config:

```bash
git clone TODO 
```

After that, you will be able to select an awesome theme. Change it in your .zshrc config that you could find in your `/home` directory (`~/`).

Emacs (+ spacemacs)
*******************

You want to know more about emacs, it's a whole world, and you could go there.




Python
-------

Python distribution
*******************

Python packages
***************

R
------

R distribution
**************

R packages
**********


Conclusion
----------

.. _`Hadley Wickham`: http://had.co.nz/
.. _`every day`: http://arxiv.org/
.. _
.. _
.. _
.. _
.. _
.. _
.. _
