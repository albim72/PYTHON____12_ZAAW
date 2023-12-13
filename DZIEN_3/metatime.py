import types
import time

class Timer:
    def __init__(self,func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None
        
    def start(self):
        if self._start is not None:
            raise RuntimeError('już działa!')
        self._start = self._func()
        
    def stop(self):
        if self._start is None:
            raise RuntimeError('funkcja nie została uruchomiona!')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None
        
    def reset(self):
        self.elapsed = 0.0
        
    @property
    def running(self):
        return self._start is not None
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        
class Timed(type):
    def __new__(cls,clsname,bases,attrs):
        for name,value in attrs.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                #attrs[name] = 
                pass
            
        return super(Timed,cls).__new__(cls,clsname,bases,attrs)
        
