
class Art:
  def __init__(self):
    self.names = None
    print('Art initialized')
    
  def print(self,args):
   print(f"Art: {args}")
  
  def set(self,names):
   self.names = names
  