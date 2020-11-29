import shutil
import psutil
import sockets
import emails

def check_localhost():
    localhost = socket.gethostname('localhost')
    return localhost = '127.0.0.1'


def check_disk_usage(disk):
    disk= shutil.disk_usage("/")
    disk_free = disk.free/disk.total*100
    return disk_free > 20

def check_memory_usage():
   mu = psutil.virtualmemory().available
   total = mu/(1024**2)
   return total > 500


def check_cpu_usage():
   cpu = psutil.cpu_percent(1)
   return cpu < 80

def send_email(subject):
   user = os.getenv('USER')
   sender = 'automation@example.com'
   receiver = '{}@example.com'.format(user)
   body = 'Please check your system and resolve the issue as soon as possibl
   email = emails.generate_report(sender, receiver, subject, body)
   emails.send_email(email)

if not check_cpu_usage():
     subject = 'Error - CPU usage is over 80%'
     send_email(subject)
if not check_memory_usage():
     subject = 'Error - Available disk space is less than 20%'
     send_email(subject)
if not check_disk-usage('/'):
     subject = 'Error - Available memory is less than 500MB'
     send_email(subject)
if not check_localhost():
     subject = 'Error - localhost cannot be resolved to 127.0.0.1'
     send_email(subject)





