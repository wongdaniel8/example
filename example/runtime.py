import matplotlib.pyplot as plt
import algs
import numpy as np

xvals = []
assignments= []
conditionals= []
assignmentsQ = []
conditionalsQ = []
for i in range(0, 1000, 100):
    xvals.append(i)
    iterassign = []
    itercond = []
    iterassignQ = []
    itercondQ = []
    for j in range(0, 10):
        x = np.random.rand(i)

        sort = algs.bubblesort(x)
        iterassign.append(sort[1])
        itercond.append(sort[2])

        sort = algs.quicksort(x, 0, len(x) - 1)
        iterassignQ.append(sort[1])
        itercondQ.append(sort[2])

    assignments.append(np.average(iterassign))
    conditionals.append(np.average(itercond))
    assignmentsQ.append(np.average(iterassignQ))
    conditionalsQ.append(np.average(itercondQ))

print("N2", [i**2 for i in range(0, 1000, 100)])
print("bubble assignments" , assignments)
print("NlogN", [i * np.log(i) for i in range(0, 1000, 100)])
print("quicksort assignments", assignmentsQ)
plt.xlabel("list length")
plt.ylabel("# of assignments")
plt.plot(xvals, [i**2 for i in range(0, 1000, 100)], label = "N^2")
plt.plot(xvals, assignments, label = "bubblesort")
plt.plot(xvals, [15 *i * np.log(i) for i in range(0, 1000, 100)], label = "15Nln(N)")
plt.plot(xvals, assignmentsQ, label = "quicksort")
plt.legend()
plt.show()


print("bubble conditionals", conditionals)
print("wuicksort conditionals", conditionalsQ)
plt.xlabel("list length")
plt.ylabel("# of conditionals")
plt.plot(xvals, [i**2 for i in range(0, 1000, 100)], label = "N^2")
plt.plot(xvals, conditionals, label = "bubblesort")
plt.plot(xvals, [15 * i * np.log(i) for i in range(0, 1000, 100)], label = "15Nln(N)")
plt.plot(xvals, conditionalsQ, label = "quicksort")
plt.legend()
plt.show()
