def main () :
  a,b =  [int(i) for i in input().split()]
    if a<b:
        print(a<b)
    elif a>b :
        print(a>b)
    else :
        print(a==b)

if__name__=='__main__':
main()
