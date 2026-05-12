import subprocess

ip = "192.168.1.100"

command = [ "sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP" ]

subprocess.run(command) print("Firewall rollback completed")
