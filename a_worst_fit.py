import objects as obs
from functions import Load_Data as load

def worst_fit():
    f_n = ["blow.txt", "memo.ry"]
    J_ar = load(f_n[0], obs.Job)        #Array of Jobs or job array
    M_ar = load(f_n[1], obs.Memory)     #Array of Memory or Memory array
    
    r = [len(J_ar)]                     #r for results
    jobs = len(J_ar)

    print(100*"=")
    print("Worst Fit algorithm : \n")

    #r = print_simulation(J_ar, M_ar)

    r = immidiate_simulation(J_ar, M_ar)

    print("Time to complete all tasks -> " + str(r[0]) + " units of time")
    throughput = "{:.2f}".format(jobs/r[0])
    print("Therefore Throughput is " + str(throughput) + " jobs/unit of time")

    print()
    print("Memory Utilization :")
    for x in M_ar:
        print("\tMemory Block " + str(x.block) + " is used " + str(x.used) + " times")

    u_c = c = 0
    print()
    print("Percentage Usage : ")
    maax = max(M_ar, key=lambda M_ar: M_ar.used)
    while(True):
        if u_c == maax.used+1:
            break
        c = 0
        for x in M_ar:
            if u_c == x.used:
                c+=1

        percent = (c / len(M_ar))*100
        if percent == 0:
            percent = int(percent)
        print("\t" + str(percent) + " % of Partitions was used " + str(u_c) + " times")
        u_c+=1

    print()
    print("The length of queue at time zero -> " + str(r[3]))

    print()
    ave_w = "{:.2f}".format(r[2]/len(M_ar))
    print("Average waiting time for jobs -> " + str(ave_w))

    print()
    print("Total Fragmentation -> " + str(r[1]))

    
    print(100*"=")

def immidiate_simulation(J_ar, M_ar):
    results = []
    time = stop = t_frag = wait = queue_l = 0

    #finding outliers
    maax = max(M_ar, key=lambda M_ar: M_ar.size)
    
    for x in J_ar:
        if x.size > maax.size:
            J_ar.remove(x)

    M_ar = sorted(M_ar, key=lambda M_ar: M_ar.size, reverse=True)

    #simulation
    while(len(J_ar) != 0):
        #stop = 0
        for x in J_ar:
            if x.active == 0:
                for y in M_ar:
                    if y.current is None:
                        if y.size > x.size:
                            y.current = x
                            x.active = 1
                            y.used+=1
                            wait+=time
                            dif = y.size - x.size
                            t_frag+=dif
                            break
                        #else:
                        #    stop = 1
            #if stop == 1:
            #    break
        if time == 0:
            queue_l = sum(x.active == 0 for x in J_ar)

        for x in M_ar:
            if x.current is not None:
                x.current.time-=1
                if x.current.time == 0:
                    J_ar.remove(x.current)
                    x.current = None
        time+=1
    
    results.append(time)
    results.append(t_frag)
    results.append(wait)
    results.append(queue_l)

    return results


def print_simulation(J_ar, M_ar):
    results = []
    time = stop = t_frag = wait = 0

    #finding outliers
    maax = max(M_ar, key=lambda M_ar: M_ar.size)
    
    for x in J_ar:
        if x.size > maax.size:
            J_ar.remove(x)

    M_ar = sorted(M_ar, key=lambda M_ar: M_ar.size, reverse=True)

    #simulation
    while(len(J_ar) != 0):
        #stop = 0
        print(100*"-")
        print("time: " + str(time) + " -> Jobs Remaining" + str(len(J_ar)))
        for x in J_ar:
            if x.active == 0:
                for y in M_ar:
                    if y.current is None:
                        if y.size > x.size:
                            y.current = x
                            x.active = 1
                            wait+=time
                            print(time)
                            dif = y.size - x.size
                            print(dif)
                            t_frag+=dif
                            break
                        #else:
                        #    stop = 1
            #if stop == 1:
            #    break

        if time == 0:
            queue_l = sum(x.active == 0 for x in J_ar)

        for x in M_ar:
            if x.current is not None:
                print(x.p() + " -> " + x.current.p())
                x.current.time-=1
                if x.current.time == 0:
                    print(str(x.current.number) + " is done executing")
                    J_ar.remove(x.current)
                    x.current = None
            else:
                print(x.p() + " -> no jobs" )  
        time+=1
        print(100*"-")

    results.append(time)
    results.append(t_frag)
    results.append(wait)
    results.append(queue_l)

    return results





