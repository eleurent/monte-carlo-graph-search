import matplotlib.pyplot as plt
import numpy as np
gamma = 0.8

r1 = 0
r2 = 0.5

V_star = r2 / (1 - gamma)
R = [[0]]
J = [[1]]
for h in range(1,22):
	R.append([])
	J.append([])
	for Rh1 in R[h-1]:
		# r1 = r2 * (1 - gamma**(h**3))
		for r in [r1, r2]:
			Rh = Rh1 + gamma**(h-1) * r
			R[h].append(Rh)
			if Rh + gamma ** h * V_star > V_star - gamma**h / (1 - gamma):
				J[h].append(1)
			else:
				J[h].append(0)


# print(J)
J = np.array(list(map(sum, J)))
h = np.arange(J.size)
J_sa = np.ones(J.shape)
fig, ax = plt.subplots()
# plt.plot(J)
# plt.plot(h, J_sa)
plt.plot(h, np.exp(np.log(J)/h))
plt.plot(h, np.exp(np.log(J_sa)/h))
# ax.set_yscale("log", basey=2)
plt.grid()
plt.legend(["OPD", "State-aware"])
plt.title("Near-optimality branching factor")
plt.xlabel("depth h")
plt.ylabel("Branching factor at depth h")
plt.show()
# print(np.power(J, 1/(np.arange(J.size))))
