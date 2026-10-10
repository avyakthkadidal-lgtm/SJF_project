def sjf_non_preemptive(at, bt, n):
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n
    done = [False] * n

    time = 0
    count = 0
    order = []

    # this is the main loop that continues until all processes are completed
    while count < n:
        shortest = -1

         #this is the loop that finds the process with the shortest burst time that has arrived and is not done yet
        for i in range(n):
            if at[i] <= time and not done[i]:                                  #this checks if the process has arrived and is not done yet
                if shortest == -1 or bt[i] < bt[shortest]:                     #this checks if the current process has a shorter burst time than the previously found shortest process
                    shortest = i

        if shortest == -1:                                                     #this checks if no process has arrived yet or all processes are done
            time += 1
            continue

       #this is the part where the process with the shortest burst time is executed
        i = shortest
        start = time
        time += bt[i]

        #this calculates the completion time, turnaround time, and waiting time for the process that was just executed
        ct[i] = time
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        done[i] = True
        count += 1

        order.append((i, start, time))

    print("\nNON-PREEMPTIVE SJF")
    print("Execution order:", end=" ") #what this does is it prints the execution order of the processes in the order they were executed

    for p in order:
        print("P" + str(p[0] + 1), end=" ") 
    print()

    print("\nPID\tAT\tBT\tCT\tTAT\tWT") 

    for i in range(n):
        print(f"P{i+1}\t{at[i]}\t{bt[i]}\t"
              f"{ct[i]}\t{tat[i]}\t{wt[i]}")

    print("Average Waiting Time:", sum(wt) / n)
    print("Average Turnaround Time:", sum(tat) / n)