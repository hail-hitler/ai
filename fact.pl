factorial(0,1).
factorial(N,X):- 
    factorial(N1,X1), 
    N is N1+1, 
    X is X1*N.
