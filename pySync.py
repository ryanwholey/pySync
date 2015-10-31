from threading import *

class Asyncifyer():
  def __init__(self, func, args=[]):
    self.func = func
    Thread(target=self.run, args=args).start()
  def run(self, *args):
    self.func(*args)


#Promise(
#    {type:main, func: func, args:[args]}
#    {type:then, func:func}, 
#    {type:then, func:func}, 
#    {type:catch, func:func})


class Promise():
  def __init__(self, func, args=[]):
    self.func = func
    self.result = None
    self.error = None
    self.thenFunc = None
    # self.catchFunc = None
    self.condition = Condition()
    self.tMain = Thread(target=self.run, args=args).start()
    self.tThen = Thread(target=self.thenRun)
    # self.tCatch = Thread(target=self.catchRun).start()

  def run(self,*args):
    #add in args to be used
    try:
      self.result = self.func(*args)
    except:
      self.error = 'ERROR'
    finally:
      self.condition.acquire()
      self.condition.notifyAll()
      self.condition.release()

  def thenRun(self):
    self.condition.acquire()
    self.condition.wait()
    if self.result != None:
      try:
        return self.thenFunc(self.result)
      except:
        pass
    self.condition.acquire()
    self.condition.notifyAll()
    self.condition.release()

  # def catchRun(self):

  #   self.condition.acquire()
  #   self.condition.wait()
  #   if self.error != None:
  #     try:
  #       return self.catchFunc()
  #     except:
  #       pass
  #   self.condition.acquire()
  #   self.condition.notifyAll()
  #   self.condition.release()

  def then(self, func):
    self.tThen.start()
    self.thenFunc = func

  # def catch(self, func):
  #   self.tCatch.start()
  #   self.catchFunc = func





class ArgCaller():
  def __init__(self, func, args):
    func(*args)



