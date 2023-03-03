
# coding: utf-8

# In[ ]:



def update_onenode(A, k, p, c, pk, ck, i, gamma, m):
    '''
    input:
    A: adjencency metrix
    k: degree list of nodes
    p: pair id of nodes
    c: core-1, periphery-0
    pk: number of nodes in one pair
    ck: number of cores in one pair
    i: input node id
    gamma: input parameter
    m: number of edges in input graph
    
    output:
    p: pair id of nodes
    c: core-1, periphery-0
    pk: number of nodes in one pair
    ck: number of cores in one pair
    '''
    # if node i is a isolated node
    if (k[i] == 0): 
        return p, c, pk, ck
    
    #if node i is not a isolated node
    #choose one node from node i 's  neighbor
    
    # from the list of neighbors of node i to delete node i itself
    pk[p[i]] -= k[i] 
    if c[i] == 1:
        ck[p[i]] -= k[i]
        
    
    vec = A[i].astype(np.bool) # only consider those connected with Ai as candidate pairs
    A_vec = A[i,vec]
    p_vec = p[vec] # exclude self labels
    c_vec = c[vec]
    k_vec = k[vec]
    p_unq = np.unique(p_vec)
    best_p = -1
    best_c = -1
    Q = -np.inf
    for p_unq_idx in range(p_unq.shape[0]):
        # c'_i = 1, is core
        # s1 = np.sum(p_unq[p_unq_idx] == p_vec) 
        # print(s1)
        s1 = np.sum(A_vec[p_unq[p_unq_idx] == p_vec]) 
        # print(s1)
        s2 = pk[p_unq[p_unq_idx]]
        dQ = (s1 - gamma*s2*k[i]/2/m)/m
        
        # c'_i = 0, is periphery, only connect to core
        s1c = np.sum(A_vec[(p_unq[p_unq_idx] == p_vec) & (c_vec == 1)])
        s2c = ck[p_unq[p_unq_idx]]
        dQc = (s1c - gamma*s2c*k[i]/2/m)/m
        
        # print(i,p_unq[p_unq_idx],  dQ, dQc, s1, s1c, s2, s2c)
        
        if dQ > Q or dQc > Q:
            best_p = p_unq[p_unq_idx]
            if dQ > dQc:
                Q = dQ
                best_c = 1
            else:
                Q = dQc
                best_c = 0
                
            if dQ == dQc:
                best_c == np.random.randint(2)
            # best_c = 1 # test, assuming community detection

    # print(best_p, best_c) # test
    p[i] = best_p
    c[i] = best_c
    

    pk[p[i]] += k[i] 
    if c[i] == 1:
        ck[p[i]] += k[i]

    return p, c, pk, ck

def CPscore(A, p, c, gamma):
    '''
    A: adjcency metrix
    p: pair id of nodes
    c: core-1, periphery-0
   gamma: input parameter
   
   output:
   cpscore
    '''
    N = A.shape[0]
    k = np.sum(A,0)
    m = np.sum(k)


    
    pk = np.zeros(N) # number of nodes in each pair
    ck = np.zeros(N) # numbero of core in each pair
    for i in range(N):
        pk[p[i]] += k[i] 
        if c[i] == 1:
            ck[p[i]] += k[i]
            
    s1sum = 0
    s2sum = 0
    for i in range(N):
        # vec = A[i] # only consider those connected with Ai as candidate pairs
        vec = A[i].astype(np.bool) # only consider those connected with Ai as candidate pairs
        A_vec = A[i,vec]
        p_vec = p[vec] # exclude self labels
        c_vec = c[vec]
        
        if (c[i] == 1): # i is a core node
            # s1 = np.sum(p[i] == p_vec)
            # print(s1)			
            s1 = np.sum(A_vec[p[i] == p_vec]) 
            # print(s1)
            s2 = pk[p[i]]
        else: # c'_i = 1, is periphery, only connect to core
            # s1 = np.sum((p[i] == p_vec) & (c_vec == 1))
            # print(s1)
            s1 = np.sum(A_vec[(p[i] == p_vec) & (c_vec == 1)])
            # print(s1)
            s2 = ck[p[i]]
        
        s1sum += s1
        s2sum += k[i]*s2
        
    Q = (s1sum - gamma/2/m*s2sum)/2/m
    return Q
    
    

# input: adjacency matrix
# output: pairid, coreness
def algo(A,gamma = 1):
    N = A.shape[0]
    p = np.array(range(N))
    c = np.round(np.random.randint(2,size=N))
    k = np.sum(A,0)
    m = np.sum(k)
    ordernum = p + (1-c)*0.1
    
    # for i in range(N):
    
    pk = np.zeros(N) 
    ck = np.zeros(N)
    for i in range(N):
        pk[p[i]] += k[i] 
        if c[i] == 1:
            ck[p[i]] += k[i]
    
    for iter in range(10):
        
        # print(p,c)
        p_change = 0
        c_change = 0
        for i in np.random. permutation(range(N)):
        # for i in range(N):
            p_current = p[i]
            c_current = c[i]
            p, c, pk, ck = update_onenode(A, k, p, c, pk, ck, i, gamma, m)
            if (p_current != p[i]):
                p_change += 1
            if (c_current != c[i]):
                c_change += 1
        print("changes: p ", p_change," c ", c_change )
    
    p_unq, p_counts = np.unique(p, return_counts = True)
    
    # re-order pair according to its pairsize (number of nodes)
    p_unq_idx = np.argsort(-p_counts) # 默认从小到大，加负号从大到小
    p_unq = p_unq[p_unq_idx]
    
    p_order = np.zeros(p.shape, dtype = np.int)
    for i in range(p_unq.shape[0]):
        p_order[p == p_unq[i]] = i
        
    
    # return p,c
    return p_order,c







