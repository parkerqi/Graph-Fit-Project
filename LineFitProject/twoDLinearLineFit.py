import numpy as np
import matplotlib.pyplot as plt
class LineFit:
  
  #init method or constructor 
  def __init__(self, x1, y1): 
    self.x = x1 
    self.y = y1 

  def findReg(self):
    global x, y
    try:
      #create matrix a = [1, x1], [1, x2]....
      a = np.array([[1 for i in range(len(self.x))], self.x]).T
      #create matrix b = [y1], [y2]....
      b = np.array(self.y).T
      #find a transpose times a and b transpose times b
      ATA = np.dot(a.T, a)
      ATb = np.dot(a.T, b)
      # solve ATAx=ATb
      xhat = np.linalg.solve(ATA, ATb).tolist()
      return self.graphDraw(xhat)
    except ValueError:
      print('Please check your input again')
      return
    except:
      print('Unexpected Error')
      return
      
  def graphDraw(self, a):
    # draw regline 
    x1 = np.linspace(0, np.amax(self.x)*1.2, 1000)
    plt.plot(x1, a[0] + a[1]*x1)
    # setting plot style 
    plt.style.use('fivethirtyeight') 
    plt.title('y = ' + np.format_float_positional(a[1], precision=3) + 'x + ' + np.format_float_positional(a[0], precision=3))
    # plotting points 
    plt.scatter(self.x, self.y) 
    plt.show()
