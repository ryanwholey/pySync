import time
import requests

from threading import Thread
from pySync import Promise, Asyncifyer, ArgCaller


################ PROMISE ###############
# remove ''' from below and at the end of 
# the block to run example code
'''

# - LIB - 
def getFromAmazon():
  response = requests.get('http://www.amazon.com')
  return response

def getFrom(a,b,c):
  url = a
  url += b
  url += c
  response = requests.get(url)
  print(response)

def d(r):
  print(r)
  return

#below is an example for a 'pseudo-promise' with and without arguments
print('before')
Promise(getFromAmazon).then(d)
Promise(getFrom,['http://www','.ama','zon.com']).then(d);
print('after')


'''
################ ASYNC #############
# remove ''' from below and at the end of 
# the block to run example code
'''
print('ASYNC THREADING EXAMPLE')

# - LIB - 
def getFromAmazon():
  response = requests.get('http://www.amazon.com')
  print(response)


#below is an example of a blocking call
print('- non threaded -')
print('before') # > before
getFromAmazon() # > <code from amazon>
print('after')  # > after

print('###############################')
print('- threaded -')
#below we utilize multithreading to create an async call
t = Thread(target=getFromAmazon)

print('before') # > before
t.start()       # > after
print('after')  # > <code from amazon>
'''

############# ASYNCIFY #################
# remove ''' from below and at the end of 
# the block to run example code
'''
print('ASYNCIFY EXAMPLE')

# - LIB - 
def getFromAmazon():
  response = requests.get('http://www.amazon.com')
  print(response)

def wait_two(n=2):
  time.sleep(n)
  print('you waited', n,'seconds')


#below is an example of a function that now runs async
print('before')
Asyncifyer(wait_two)
print('after')

#we can pass it arguments if we format them in an
#array after the function argument
Asyncifyer(wait_two,[3])

# > before
# > after
# > you waited 2 seconds
# > you waited 3 seconds

'''

################ PROMISE ##################
'''
#note: catch block doesnt work yet
#note: then & catch should both return instance of Promise
print('ASYNC THREADING EXAMPLE')
# - LIB - 
def getFromAmazon():
  return requests.get('http://amazon.com')

def getFromHomestar():
  return requests.get('http://homestarrunner.com')

def getFrom(site, *args):
  return requests.get(site)

def p(d):
  print(d.url)
  #we can print the full response below if we want
  # for data in d:
  #   print(data)

# we make three requests, amazon although called first
# returns last because of it's size.
# the data returned from the promise is passed into
# the then block, we can pass in a predefined function
# to then handle returned data. (e.g. send data to client)
print('before')
Promise(getFromAmazon).then(p)
Promise(getFromHomestar).then(p)
Promise(getFrom, ['https://github.com']).then(p)
print('after')

# > before
# > after
# > http://homestarrunner.com/
# > https://github.com/
# > http://www.amazon.com/

'''



