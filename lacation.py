def tranarray(arr11):
    arr22=[[0 for j in range(3)]for i in range(3)]
    arr22[0][0]=arr11[2][0]
    arr22[0][1]=arr11[1][0]
    arr22[0][2]=arr11[0][0]
    arr22[1][0]=arr11[2][1]
    arr22[1][1]=arr11[1][1]
    arr22[1][2]=arr11[0][1]
    arr22[2][0]=arr11[2][2]
    arr22[2][1]=arr11[1][2]
    arr22[2][2]=arr11[0][2]
    return arr22

def createarray(array,i,j):
    arr=[[0 for ii in range(3)]for jj in range(3)]
    arr[0][0]=array[i-1][j-1]
    arr[0][1]=array[i-1][j]
    arr[0][2]=array[i-1][j+1]
    arr[1][0]=array[i][j-1]
    arr[1][1]=array[i][j]
    arr[1][2]=array[i][j+1]
    arr[2][0]=array[i+1][j-1]
    arr[2][1]=array[i+1][j]
    arr[2][2]=array[i+1][j+1]
    return arr

(N,M)= (int(x) for x in raw_input().split())
arr=[[0 for j in range(N)]for i in range(M)]
for i in range(N):
    arr[i]=list(str(x) for x in raw_input())
arr33=[[0 for j in range(3)]for i in range(3)]
for i in range(3):
    arr33[i]=list(x for x in raw_input())
arrtest=arr33
arr1=arr33
arr2=tranarray(arr1)
arr3=tranarray(arr2)
arr4=tranarray(arr3)
for i in range(1,N-1):
    for j in range(1,M-1):
        arrtest=createarray(arr,i,j)
        if arrtest == arr1 or arrtest == arr2 or arrtest==arr3 or arrtest==arr4:
            print i+1,j+1
