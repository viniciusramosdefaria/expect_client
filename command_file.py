import argparse
import csv


class CommandFile:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', type=str, help='File with the list of commands', required=False)
        parser.add_argument('-u', type=str, help='Username', required=True)
        parser.add_argument('-i', type=str, help='IP', required=True)
        parser.add_argument('-p', type=str, help='Password', required=False)
        parser.add_argument('-I', type=int, help='Interactive', required=False)
        self.args = parser.parse_args()

    def generate_list(self):
        f_commands = open(self.args.f, 'r')
        reader_commands = csv.reader(f_commands, delimiter='\n')
        list_of_commands = []
        for line in reader_commands:
            list_of_commands.append(line[0])

        return list_of_commands

    def get_args(self):
        return self.args
