process <- c("NB"
             ,"
	I[1] ~ dnegbin(initDis,i0)
  beta <- exp(-R0/N0)
	pSI[1] <- 1 - exp(I[1]*log(beta))
  "
             , 
             #  "for(t in 2:numobs){
             "I[t] ~ dnegbin(pSI[t-1],S[t-1])
  pSI[t] <- 1 - exp(I[t]*log(beta))
"
             #  }"
)