from threading import *

class Asyncifyer():
  def __init__(self, func, args=[]):
    self.args = args
    self.func = func
    Thread(target=self.run).start()

  def run(self):
    try:
      self.func(*self.args)
    except:
      try:
        self.func()
      except:
        print('error with func:', self.func)

  def start(self):
    self.t.start()


class ArgCaller():
  def __init__(self, func, args):
    func(*args)


class Promise():
  def __init__(self, func, args=[]):
    self.func = func
    self.result = ''
    self.error = ''
    self.t = Thread(target=self.run)
    self.condition = Condition()
    self.args = args
    self.t.start()

  def run(self):
    #add in args to be used
    try:
      self.result = self.func(*self.args)
    except:
      try:
        self.result = self.func()
      except:
        print('error')
        self.error = 'error'
        self.result = None
    finally:
      self.condition.acquire()
      self.condition.notifyAll()
      self.condition.release()


  def then(self, func):
    if(self.result==None):
      return
    def thenRun():
      self.condition.acquire()
      self.condition.wait()
      func(self.result)

    Thread(target=thenRun).start()

  #not functional yet
  def catch(self, func):
    if(self.error==None):
      return
    def catchRun():
      self.condition.acquire()
      self.condition.wait()
      func(self.error)

    Thread(target=catchRun).start()


