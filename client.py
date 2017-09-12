import ssh_part
import command_list
import command_file

if __name__ == '__main__':

    command_line = command_file.CommandFile()
    args = command_line.args
    list_of_commands = command_line.generate_list()
    connection = ssh_part.Connection(args.u, args.i, args.p, '-L 8080:localhost:8080 ')
    command_exec = command_list.Command(list_of_commands, connection.connect())
    command_exec.execute_command()
    command_exec.exit_machine()
