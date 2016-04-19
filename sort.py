
class sortjson():

  def walk(self,d):
      path=[]
      for k,v in d.items():
          if isinstance(v, str) or isinstance(v, int) or isinstance(v, float):
            path.append(k)
            print "{}={}".format(".".join(path), v)
            path.pop()
          elif v is None:
            path.append(k)
            ## do something special
            path.pop()
          elif isinstance(v, dict):
            path.append(k)
            walk(v)
            path.pop()
          else:
            print "###Type {} not recognized: {}.{}={}".format(type(v), ".".join(path),k, v)