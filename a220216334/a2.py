
# This is your unique solution file

from config import *
from lib204 import semantic_interface

# Assignment for 19al63

# Note: All of these answers are almost certainly wrong

a2q12 = [ [s1, s4], [s2, s3] ]

a2q13 = {
    P: True,
    R: False,
    T: True
}

a2s5nnf = [
    [((S&(T|R))>>~(R|~T)), 'starting formula'],
    [(~(S&(T|R))|~(R|~T)),'replace implication'],
    [((~S|~(T|R))|(~R&T)),'de Morgans on both parts of equation'],
    [((~S|(~T&~R))|(~R&T)),'de Morgans one more time']
]

a2s6nnf = [
    [((T>>R)>>(S|(R&~T))), 'starting formula'],
    [(~(T>>R)|(S|(R&~T))),'replace implication'],
    [(~(~T|R)|(S|(R&~T))),'replace implication again'],
    [((T&~R)|(S|(R&~T))),'de Morgans']
]

a2s5cnf = [
    [((S&(T|R))>>~(R|~T)), 'Starting formula'],
    [((~S|(~T&~R))|(~R&T)),'Using NNF, steps above'],
    [(((~S|~T)&(~S|~R))|(~R&T)),'Distribution'],
    [(((~S|~T)|(~R&T))&((~S|~R)|(~R&T))),'Distribution'],
    [((~R|(~S|~T))&(T|(~S|~T))&(~R|(~S|~R))&(T|(~S|~R))),'Distribution'],
    [((~R|~S|~T)&(T|~S|~T)&(~R|~S|~R)&(T|~S|~R)),'Remove brackets, only disjuncts left, therefor CNF']
]

a2s6cnf = [
    [((T>>R)>>(S|(R&~T))), 'starting formula'],
    [((T&~R)|(S|(R&~T))),'Using NNF, steps above'],
    [((T&~R)|((S|R)&(S|~T))),'distribution'],
    [((T|((S|R)&(S|~T)))&(~R|((S|R)&(S|~T)))),'distribution'],
    [((T|(S|R))&(T|(S|~T))&(~R|(S|R))&(~R|(S|~T))),'distribution'],
    [((T|S|R)&(T|S|~T)&(~R|S|R)&(~R|S|~T)),'Remove brackets, only disjuncts left, therefor CNF']
]

a2s5tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s5tseitin.tseitin(S | R, 'x1') # just an example
x2 = a2s5tseitin.tseitin(S & x1, 'x2')
x3 = a2s5tseitin.tseitin(T, 'x3')
x4 = a2s5tseitin.tseitin(~x3, 'x4')
x5 = a2s5tseitin.tseitin(R | x4, 'x5')
x6 = a2s5tseitin.tseitin(~x5, 'x6')
x7 = a2s5tseitin.tseitin(x2 >> x6, 'x7')
a2s5tseitin.finalize(x7) # make sure you update the variable!

a2s6tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s6tseitin.tseitin(T >> R, 'x1') # just an example
x2 = a2s6tseitin.tseitin(T, 'x2')
x3 = a2s6tseitin.tseitin(~x2, 'x3')
x4 = a2s6tseitin.tseitin(R & x4, 'x4')
x5 = a2s6tseitin.tseitin(S | x4, 'x5')
x6 = a2s6tseitin.tseitin(x1 >> x5, 'x6')
a2s6tseitin.finalize(x6) # make sure you update the variable!

