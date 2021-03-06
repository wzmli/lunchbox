import numpy as np
from pymc3 import Model, Uniform, Binomial, find_MAP, NUTS, sample, Slice, traceplot, summary
from scipy import optimize

# Parameters
effprop = 0.1
beta = 0.0005
N = 100000
i0 = 1
numobs = 10
reporting = 0.8

# Set up seed
np.random.seed(111)

S,I,R,Iobs,Psi = (np.zeros(numobs) for i in range(5))

# Initial 
N0 = effprop*N
I[0] = i0
S[0] = N0 - i0
R[0] = N-N0
Psi[0] = 1 - (1-beta)**I[0]
Iobs[0] = np.random.binomial(I[0],reporting,1)

for t in range(1,numobs-1):
  I[t] = np.random.binomial(S[t-1],Psi[t-1],1)
  S[t] = S[t-1] - I[t]
  R[t] = R[t-1] + I[t-1]
  Psi[t] = 1 - (1-beta)**I[t]
  Iobs[t] = np.random.binomial(I[t],reporting,1) 


Iobs1 = Iobs[0]
Iobs2 = Iobs[1]
Iobs3 = Iobs[2]
Iobs4 = Iobs[3]
Iobs5 = Iobs[4]  
Iobs6 = Iobs[5]
Iobs7 = Iobs[6]
Iobs8 = Iobs[7]
Iobs9 = Iobs[8]
Iobs10 = Iobs[9] 

basic_model = Model()

with basic_model:
    # Priors for unknown model parameters
    effprop = Uniform("effprop", lower=0 , upper=1)
    beta = Uniform("beta", lower=0, upper=0.02)
    reporting = Uniform("reporting", lower=0, upper=1)

    N0 = Binomial("N0",n=N,p=effprop)
    I1 = 1
    S1 = N0 - I1
    Psi12 = 1 - (1-beta)**I1
    # Likelihood (sampling distribution) of observations unfolding the for loop 
    obs1 = Binomial("obs1",n=I1,p=reporting,observed=Iobs1)
    

    I2 = Binomial("I2",n=S1,p=Psi12) 
    S2 = S1 - I1
    Psi23 = 1 - (1-beta)**I2
    obs2 = Binomial("obs2",n=I2,p=reporting,observed=Iobs2)

    
    I3 = Binomial("I3",n=S2,p=Psi23) 
    S3 = S2 - I3
    Psi34 = 1 - (1-beta)**I3
    obs3 = Binomial("obs3",n=I3,p=reporting,observed=Iobs3) 
    
    I4 = Binomial("I4",n=S3,p=Psi34) 
    S4 = S3 - I4
    Psi45 = 1 - (1-beta)**I4
    obs4 = Binomial("obs4",n=I4,p=reporting,observed=Iobs4) 
    
    I5 = Binomial("I5",n=S4,p=Psi45) 
    S5 = S4 - I5
    Psi56 = 1 - (1-beta)**I5
    obs5 = Binomial("obs5",n=I5,p=reporting,observed=Iobs5) 

    I6 = Binomial("I6",n=S5,p=Psi56) 
    S6 = S5 - I6
    Psi67 = 1 - (1-beta)**I6
    obs6 = Binomial("obs6",n=I6,p=reporting,observed=Iobs6) 
    
    I7 = Binomial("I7",n=S6,p=Psi67) 
    S7 = S6 - I7
    Psi78 = 1 - (1-beta)**I7
    obs7 = Binomial("obs7",n=I7,p=reporting,observed=Iobs7) 
    
    I8 = Binomial("I8",n=S7,p=Psi78) 
    S8 = S7 - I8
    Psi89 = 1 - (1-beta)**I8
    obs8 = Binomial("obs8",n=I8,p=reporting,observed=Iobs8)
    
    I9 = Binomial("I9",n=S8,p=Psi89) 
    S9 = S8 - I9
    Psi910 = 1 - (1-beta)**I9
    obs9 = Binomial("obs9",n=I9,p=reporting,observed=Iobs9)
    
    I10 = Binomial("I10",n=S9,p=Psi910) 
    S10 = S9 - I10
    Psi1011 = 1 - (1-beta)**I10
    obs10 = Binomial("obs10",n=I10,p=reporting,observed=Iobs10)

# map_estimate = find_MAP(model=basic_model)
# print(map_estimate)

aa = dict(N0=10000,I2=I[1],I3=I[2],I4=I[3],I5=I[4],I6=I[5],I7=I[6],I8=I[7],I9=I[8],I10=I[9],beta=0.0005,reporting=0.7,effprop=0.1)
print(aa)
with basic_model:

    # obtain starting values via MAP
    # start = find_MAP(fmin=optimize.fmin_powell)
    start = aa

    # instantiate sampler
    step = Slice(vars=[N0,I2,I3,I4,I5,I6,I7,I8,I9,I10,effprop,reporting,beta]) 

    # draw 1000 posterior samples
    trace = sample(1000, step=step, start=start) 
    
summary(trace)
