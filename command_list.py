import time


class Command:

    def __init__(self, command, child):
        self.command = command
        self.command_child = child

    def execute_command(self):

        try:
            for i in self.command:
                self.command_child.sendline(i)
                time.sleep(1)
                self.command_child.expect('.*#.*')

        except Exception as e:
            print(e)

    def exit_machine(self):
        self.command_child.sendline('exit')

