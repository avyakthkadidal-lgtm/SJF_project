from sjf_package.non_preemptive import sjf_non_preemptive
from sjf_package.preemptive import sjf_preemptive
from sjf_package.charts import draw_gantt, compare_modes

n = int(input("Enter number of processes: "))

at = []
bt = []
for i in range(n):
    print("\nProcess P", i + 1)
    a = int(input("Enter arrival time: "))
    b = int(input("Enter burst time: "))

    at.append(a)
    bt.append(b)

np_tl, np_wt, np_tat = sjf_non_preemptive(at, bt, n)
p_tl, p_wt, p_tat = sjf_preemptive(at, bt, n)

draw_gantt(np_tl, "Non-Preemptive SJF", "gantt_np.png")
draw_gantt(p_tl, "Preemptive SJF (SRTF)", "gantt_p.png")
compare_modes(np_wt, np_tat, p_wt, p_tat, "comparison.png")