# CP-score
If you use this piece of code, you can cite the following publication,
>Shen, X., Han, Y., Li, W., Wong, K. C., & Peng, C. (2021). Finding core–periphery structures in large networks. Physica A: Statistical Mechanics and its Applications, 581, 126224.

**Test**
```
gamma = 1

P_start = timeit.default_timer()
my_pairidnum, my_corenessnum = algo(dt,gamma) #gama=5.0
P_end = timeit.default_timer()
print('MY Run time: ', P_end - P_start)
#np.set_printoptions(threshold=20000)
print('my_pairidnum=',my_pairidnum)
print('my_corenessnum=',my_corenessnum)
print('CPscore=',CPscore(dt, my_pairidnum, my_corenessnum, gamma=gamma))
```
```
def myread(netpath):
    with open(netpath) as f:
        read_data=f.read()
        fo=read_data.split()
        fo = [ int(x) for x in fo ]
        length=len(fo) 
       
        returnMat = [[0 for x in range(max(fo)+1)] for y in range(max(fo)+1)] 
        
        temp=0
        while(temp<length):
            returnMat[fo[temp]][fo[temp+1]]=1
            returnMat[fo[temp+1]][fo[temp]]=1 
            temp+=2     
            
        #print(returnMat)
    f.closed
    return returnMat,max(fo)  

netpath='path of your network'
(dt0,graphsize)=myread(netpath)
dt0=np.array(dt0)

dt = dt0[:graphsize,:graphsize]
dt.shape
```
