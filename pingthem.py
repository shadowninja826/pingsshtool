import multiprocessing
import subprocess
import os

def pinger( job_q, results_q ):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break

        try:
            subprocess.check_call(['ping','-c1',ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

if __name__ == '__main__':
    pool_size = 254

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
             for i in range(pool_size) ]

    for p in pool:
        p.start()

    for i in range(1,128):
        jobs.put('192.168.150.{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()
    iplist = []
    while not results.empty():
        ip = results.get()
        print(ip)
        iplist.append(ip)
        print iplist
    iplist2 = (", ".join(iplist))
    iptxtlist = open('ipname.txt', 'a')
    ipstrlist = iplist2
    iptxtlist.write(ipstrlist)
    iptxtlist.close()

