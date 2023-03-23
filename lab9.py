'''
lab9
define class
'''

#2.1
class my_stat():
    def cal_sigma(self,m,n):
        result = 0
        for i in range(n,m+1):
            result=result+i
        
        return(result)

#2.2
    def cal_pi(self,m,n):
        result = 1
        for i in range(n,m+1):
            result=result*i
        
        return(result)
#2.3
    def cal_f(self,m):
         if m==0:
           return 1
         else:
            return m*self.cal_f(m-1)
#2.4
    def cal_p(self,m,n):
        return self.cal_f(m)/self.cal_f(m-n)