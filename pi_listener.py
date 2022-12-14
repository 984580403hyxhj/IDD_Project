from subprocess import Popen, PIPE

stdout, stderr = Popen(['ssh', 'pi@192.168.31.95', 'xjz20000320', 'ls'], stdout=PIPE).communicate()
print(stdout)



