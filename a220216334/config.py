
# DO NOT EDIT

# Assignment for 19al63

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = ((R|T)&(~P|T))
s2 = ((R&P)&(~T|R))
s3 = ((~(~T|~P)&R)|((~T&R)&P))
s4 = (T|(~P&R))

s5 = ((S&(T|R))>>~(R|~T))
s6 = ((T>>R)>>(S|(R&~T)))
