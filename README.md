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
