"""
ASGI config for learn project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn.settings')

application = get_asgi_application()




# API = 

# def decorator(fun):
#     def wrapper(*args, **kwrgs):
#         result = func(n)
#     return result
#     return wrapper
    
# def retry():
#     print("second")


# @decorator(3)    
# retry()


# id,name,status,department,salary
# 1,Alice,active,HR,60000
# 2,Bob,inactive,Engineering,80000
# 3,Charlie,active,Marketing,55000
# 4,David,active,Engineering,90000
# 5,Eve,inactive,HR,62000
# 6,Frank,active,Marketing,58000

# def active_csv(csv):
#     with open(csv , 'r') as file:
#         for line in file:
#             status = line.split(',')[2]
#             if status == "active":
#                 with open(wcsv, 'w')
#     return wcsv
    
# ans = active_csv(csv)

arr=[1,2,5] 
amt = 5


def find_num_ways(arr,total_amount , amt, i):  
    
    if i > len(arr):
        return
    
    if total_amount > amt:
        return
    
    return 1 + find_num_ways(arr, arr[i] + arr[i+1], amt, i+1)
    

    
ans = find_num_ways(arr,0 , amt, 0)
print(ans)




a = [1, 2, 3]

b = [1, 2, 3]


print(a==b)
print(a is b)

Write a function to find the first non-repeating character in a string. 


str = "abaccdeedf"

def non_rep_char(str):
	char = 0
	dict_ = {}
	for i in str:
  	if i in dict_:
    	dict_[i] = 1 + dict_get(i, 0)
    else:
			dict_[i] = 1
    
  
		for i in str_:
    	dict_[i] == 1
				return i
        
        
SELECT SALARY FROM EMPLOYEE WHERE SALAERY ORDERBY DESC LIMIT 1 OFFSET 1;
