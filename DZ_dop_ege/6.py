k=0
for x in range(0,11):
    for y in range(0,11):
        m=7*25**5+y*25**4+2*25**3+3*25**2+x*25+5 + 6*11**4+7*11**3+x*11**2+9*11+y
        if m%131==0:
            print(m//131)
#552647