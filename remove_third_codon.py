#usage: python3 remove_third_codon.py <in_fasta>
import sys
f=open(sys.argv[1],"r")
lines=f.readlines()
w=open(sys.argv[1]+".out","w")
for fas in lines:
    if '>' not in fas:
        ll=list(fas)
        #print(ll)
        a=0
        n=0
        lenn=len(ll)-1
        if lenn%3==0:
            while (a+2)<=lenn:
                    a+=2
                    #print(a,len(ll))
                    if a<=len(ll):
                        ll.pop(a)
                        n+=1
                    #print(ll)
            for i in ll:
                w.write(''.join(i))
                #print(''.join(i))
            #print(len(fas)//3,n)
        else:
            print('the length wrong!:',lenn)
    else:
        w.write(fas)

