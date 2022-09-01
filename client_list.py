def main():
    infile = open('clients.txt','r')
    x = 1
    for line in infile:
        print(x,'. ', line.rstrip('\n'), sep='')
        x+=1
main()

        