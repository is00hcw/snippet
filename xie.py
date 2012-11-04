#1.0 init
from math import pow
m = 0.2533 ,dt = 0.1
u0 = [],u1 = [], u2 = []
u0[0] = 0 ,u1[0] = 0, u2[0] = 0
du0 = [],du1 = [], du2 = []
p = [], dp = [], dp_ = []
p[0] = 0

#kk = k+2*c/dt + 4*m /pow(dt)
k = 10,k_ = 114.5
a = 10.45, b = 0.5066,   c = 0.1592

#2.0 Calculations for each etime step
def fun(i):
	#2.1
	dp_[i] = dp[i] +10.45* u1[i] + 0.5066*u2[i]
	#2.2
	du[i] = dp_[i] / k_
	#2.3
	du1[i] = 2*du[i]/dt - 2*u1[i] 
	#2.4
	#du2[i] = 4(du[i]- dt*u1[i])/pow(dt, 2) - 2u2[i]
	du2[i] = 4*(du[i]- dt*u1[i]) /pow(dt, 2) - 2*u2[i]
	#2.5
	u0[i+1] = u0[i] +  du0[i]
	u1[i+1] = u1[i] + du1[i]
	u2[i+1] = u2[i] + du2[i]
#3 循環
n = 10
for i in range(n):
	fun(i)