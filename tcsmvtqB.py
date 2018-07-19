list=[]
largval=""
N=0
def val(larg):
    global largval
    largval=largval+larg;


def larg(M):
    larg=-1
    largi=0
    global N
    for i in range(0,M):
        if(int(list[i][N-1])>larg):
            larg=int(list[i][N-1])
            largi=i;
    if(larg==0):
        N=N-1
    for i in range(N,0,-1):
        list[largi][i-1]=list[largi][i-2]

    list[largi][0]="0"
    val(str(larg))





def main():
    print "Input"
    inpl1=raw_input()
    global N
    inpl1spl=inpl1.split(",")
    M=int(inpl1spl[0])
    N=int(inpl1spl[1])
    for i in range(0,M):
        inp=raw_input()
        inpspl=inp.split(",")
        list.append(inpspl)

    for i in range(0,M*N):
        larg(M)
    print "Output"
    print int(largval)



main()
