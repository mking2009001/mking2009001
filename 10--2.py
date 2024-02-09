a=int(input('10 lik sanoq sistemadagi son kiriting:'))
son_2lik=[]
while True:
    if a<=0:
        break
    if a==1:
        son_2lik.append('1')
        break
    son_2lik.append(a%2)
    a=a//2
    if a==1:
        son_2lik.append(a)
        break
son_2= list(reversed(son_2lik))
af= "".join(map(str, son_2))
print(f"2 lik sanoq sistemasida {af} ga teng")
