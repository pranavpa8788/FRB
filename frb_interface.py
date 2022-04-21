from sys import argv
from textwrap import dedent
import argparse

welcome_string = '''
Welcome to FRB! 
FRB stands for Freelanc Reddit Bot
FRB is a tool for both freelacners and buyers
You can use FRB is automate the task of finding sellers and buyers on your favourite subreddit
No more, of constantly refresing pages to be the first one to reach out!
You can achieve that using FRB!

NOTE: FRB is still in develolpment phase and only a limited features are available for now 
      The essential features such as background listeners are coming soon!
      If you have any issues/ideas, feel free to contribute at https://github.com/pranavpa8788/FRB

Run frb_interface.py with a -h option to see a list of available options

Thank you for using FRB
'''

options_dict = {
                '-h': 'Help; displays list of available options',
                '-l': 'Login; enter the api credentials',
                '-c': 'Configure; add/Edit/Remove subreddits, keywords, etc',
                '-d': 'Display; display the current configuration details'
                }

parser = argparse.ArgumentParser(description='Freelance Reddit Bot')

parser.add_argument('how', type=str, help='testing some shit')

args = parser.parse_args()

