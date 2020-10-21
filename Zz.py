X = [3,4,1,5,1]
for i in range(len(X)) :
    if X[abs(X[i])-1] > 0 :
        X[abs(X[i])-1] = -X[abs(X[i])-1]
    else:
        print('Repeating',abs(X[i]))
              
for i in range(len(X)) :
    if X[i] > 0 :
        print('Missing',i +1)