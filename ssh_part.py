import pexpect
import os
import time
import sys


class Connection:

    def __init__(self, username, host, password, options):
        self.host = host
        self.username = username
        self.password = password
        self.options = options

    def connect(self):
        try:
            os.environ["TERM"] = "dumb"
            spawn_string = "".join(('ssh ', self.options, self.username, '@', self.host))
            child = pexpect.spawn(spawn_string)
            fout = open('log.txt', 'wb')
            child.logfile_read = fout
            i = child.expect(['.*]#', '.*assword:'])

            time.sleep(1)

            if i == 0:
                print('Connection to {} successful'.format(self.host))
            elif i == 1:

                child.sendline(self.password)
                time.sleep(1)
                status = child.expect(['Permission .*', '.*\$'])
                time.sleep(1)

                if status == 0:
                    print('Permission denied on host. Can\'t login')
                    sys.exit(0)

                elif status == 1:
                    child.sendline('sudo su -')
                    time.sleep(1)
                    child.expect(['.*:.*'])
                    time.sleep(1)
                    child.sendline(self.password)
                    time.sleep(1)
                    child.expect('.*#.*')
                    time.sleep(1)

            return child

        except Exception as e:
            print(e)
            print('Possible timeout occurred')

