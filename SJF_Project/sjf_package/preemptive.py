def sjf_preemptive(at, bt, n):
    rt = bt.copy()
    ct = [0] * n 
    wt = [0] * n
    tat = [0] * n

    time = 0
    count = 0
    order = []
    last = -1

    #loop for the number of processes that have completed execution
    while count < n: 
        shortest = -1

        #loop for the number of processes to find the process with the shortest remaining time that has arrived and is not done yet
        for i in range(n): 
            if at[i] <= time and rt[i] > 0:
                if shortest == -1 or rt[i] < rt[shortest]:
                    shortest = i

        if shortest == -1:
            time += 1
            last = -1
            continue

        #condition to check if the last process executed is different from the current shortest process, if so, append the current shortest process to the order list with its start and end time. If the last process executed is the same as the current shortest process, update the end time of the last process in the order list.
        if last != shortest:
            order.append((shortest, time, time + 1))

        else:
            p, start, end = order[-1]
            order[-1] = (p, start, time + 1)

      #this is the part where the process with the shortest remaining time is executed for one time unit, and the remaining time of that process is decremented by 1. The current time is incremented by 1, and the last executed process is updated to the current shortest process. If the remaining time of the current shortest process becomes 0, it means that the process has completed execution, and its completion time, turnaround time, and waiting time are calculated. The count of completed processes is also incremented by 1.
        rt[shortest] -= 1
        time += 1
        last = shortest

        #this checks if the remaining time of the current shortest process is 0, which means that the process has completed execution. If so, it calculates the completion time, turnaround time, and waiting time for that process and increments the count of completed processes by 1.
        if rt[shortest] == 0:
            ct[shortest] = time
            tat[shortest] = ct[shortest] - at[shortest]
            wt[shortest] = tat[shortest] - bt[shortest]
            count += 1

    print("\nPREEMPTIVE SJF (SRTF)")
    print("Execution order:", end=" ")

    for p in order:
        print("P" + str(p[0] + 1), end=" ")
    print()

    print("\nPID\tAT\tBT\tCT\tTAT\tWT")

    for i in range(n):
        print(f"P{i+1}\t{at[i]}\t{bt[i]}\t"
              f"{ct[i]}\t{tat[i]}\t{wt[i]}")

    print("Average Waiting Time:", sum(wt) / n)
    print("Average Turnaround Time:", sum(tat) / n)