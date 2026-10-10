from sjf_package.non_preemptive import sjf_non_preemptive
from sjf_package.preemptive import sjf_preemptive

n = int(input("Enter number of processes: "))

at = []
bt = []
for i in range(n):
    print("\nProcess P", i + 1)
    a = int(input("Enter arrival time: "))
    b = int(input("Enter burst time: "))

    at.append(a)
    bt.append(b)

sjf_non_preemptive(at, bt, n)
sjf_preemptive(at, bt, n)