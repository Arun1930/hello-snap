#!/usr/bin/env python3.5
import sys

from colorama import init
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


def main():
    cprint(
        figlet_format('Hello!', font='starwars'),
        'yellow',
        'on_red',
        attrs=['bold'])


if __name__ == "__main__":
    main()
