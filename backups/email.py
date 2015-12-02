#!/usr/bin/python
# Backup script for email (IMAP) accounts

from optparse import OptionParser
import subprocess

def main():
    parser = OptionParser()
    parser.add_option("-u", "--username", action="store", type="string",
                  help="username for login", dest="username")
    parser.add_option("-p", "--password", action="store", type="string",
                  help="password for login", dest="password")
    parser.add_option("-g", "--gmail",
                  action="store_true", dest="gmail", default=False,
                  help="is this a gmail account?")
    (options, args) = parser.parse_args()
    if(options.gmail):
        subprocess.call(["gmvault", "-h"])
    else:
	print "regular email"

# do work here

if __name__ == "__main__":
    main()
