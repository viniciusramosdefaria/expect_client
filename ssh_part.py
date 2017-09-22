import pexpect
import os
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
            child.setwinsize(400, 400)
            i = child.expect(['.*]#', '.*assword:'])

            if i == 0:
                print('Connection to {} successful'.format(self.host))
            elif i == 1:

                child.sendline(self.password)
                status = child.expect(['Permission .*', '.*\$'])

                if status == 0:
                    print('Permission denied on host. Can\'t login')
                    sys.exit(0)

                elif status == 1:
                    child.sendline('sudo su -')
                    child.expect(['.*:.*'])
                    child.sendline(self.password)
                    child.expect('.*#.*')

            return child

        except Exception as e:
            print(e)
            print('Possible timeout occurred')

