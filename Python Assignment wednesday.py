#!/usr/bin/env python
# coding: utf-8

# 1.Create a function in python to replace the text file and replace specific content of the file.

# In[1]:


def replacetext():
    f = open("example.txt" , 'r+')
    p = f.readline().split(' ')
    
    for i in range(len(p)):
        if p[i] == "placement":
            p[i] = "screening"
    f = open("example.txt", "w")
    print(" ".join(p))
    f.write(" ".join(p))
    f.close()


# In[ ]:


replacetext()


# 2. Demonstrate use of abstract class, multiple inheritance and decorator in python using examples
# 

# Abstarct Class
# An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.

# In[8]:


from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
    
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# In[14]:


R = Triangle()
R.noofsides()


# In[7]:


K = Quadrilateral()
K.noofsides()


# In[9]:


R = Pentagon()
R.noofsides()


# In[10]:


K = Hexagon()
K.noofsides()


# Multiple Inheritence¶
# When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.
# 
# Syntax:
# 
# Class Base1:
# 
#    Body of the class
# Class Base2:
# 
#  Body of the class
# Class Derived(Base1, Base2):
# 
#  Body of the class

# In[11]:


class Class1:
    def m(self):
        print("In Class1")
       
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3") 
        
class Class4(Class2, Class3):
    pass  
     
obj = Class4()
obj.m()


# Decorators
# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

# In[13]:


def function1(text):
    return text.upper()
 
def function2(text):
    return text.lower()
 
def deco(func):
    # storing the function in a variable
    g = func("""Hi, my name is Supriya.""")
    print (g)
 
deco(function1)
deco(function2)


# In[ ]:




