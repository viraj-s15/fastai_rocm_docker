from numba import jit, cuda
import numpy as np
from timeit import default_timer as timer   
  
def func(a):                                
    for i in range(100000000):
        a[i]+= 1      
  
@jit(target_backend='cuda')                         
def func2(a):
    for i in range(100000000):
        a[i]+= 1
if __name__=="__main__":
    n = 100000000                            
    a = np.ones(n, dtype = np.float64)
      
    start = timer()
    func(a)
    print("without GPU:", timer()-start)    
      
    start = timer()
    func2(a)
    print("with GPU:", timer()-start)
