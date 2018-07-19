def findsubset(s):
    set=[s]
    for i in range(0,len(s)):
        tp=findsubset(s[:i]+s[i+1:])
        for sbst in tp:
            if sbst not in set:
                set.append(sbst)
    return set
def main():
    print "Input"
    inpl1=raw_input()
    inpl2=raw_input()
    inpl1spl=inpl1.split(",")
    inpl2spl=inpl2.split(",")
    N=int(inpl1spl[0])
    if(N<=300):
        num=0
        sum_val=1
        P=int(inpl1spl[1])
        if(len(inpl1spl)==2):
            Q=0
        else:
            Q=int(inpl1spl[2])
        mod=P*Q
        if(P<=50 and Q<=50):
            sub_set=findsubset(inpl2spl)
            for i in range(0,len(sub_set)):
                for j in range(0,len(sub_set[i])):
                    val=int(sub_set[i][j])
                    sum_val=sum_val*val
                if mod!=0:
                    if(sum_val%mod==0):
                        num=num+1;
                    sum_val=1
        
            print num


main()
