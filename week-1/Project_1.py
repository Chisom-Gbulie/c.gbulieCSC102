#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python program for Simple Interest

principle = float(input("Enter the principle: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time: "))

amount = principle * (1 +(rate / 100) * time)
simple interest = amount - principle
print(simple interest)


# In[ ]:


# Python program for Compund Interest

principle = float(input("Enter the principal: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time: "))
n = float(input("Enter the number of Compoundings anually: "))

amount = principle * (1 + (rate / n)) ** (n * time)
Compund Interest = amount - principle
print(Compund Interest)






# In[ ]:


pmt = float(input("Enter the Regular Payment Amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time: "))
n = float(input("Enter the number of Compoundings anually: "))
y = float(input("Enter the number of Years: "))

Accumulated Savings Plan Balance = pmt * ((1 + rate/n) ** (n * time) - 1) / (rate/n)
Annuity Plan = Accumulated Savings Plan Balance - pmt
print(Annuity Plan)


# In[ ]:





# In[ ]:





# In[ ]:




