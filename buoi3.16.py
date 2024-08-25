# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:44:51 2024

@author: Student
"""
a= "Dai hoc quoc gia, khu pho 6, p.Linh Trung, Q.Thu Duc,Tp.HCM "
a1 = a.split(", ")
for i in a1:
    print(i)
a2 = a.replace('P. ', '').replace('Q. ','').replace('Tp. ','').split(", ")
for u in a2:
    print(u)