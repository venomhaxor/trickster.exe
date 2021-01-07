import sys
import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t', help='target', dest='target')
parser.add_argument('-c', help='choice', dest='choice')
parser.add_argument('--domains', help='stdin type: domain', dest='domains', action='store_true')
parser.add_argument('--ips', help='stdin type: ip', dest='ips', action='store_true')
args = parser.parse_args()

ips = args.ips
target = args.target
choice = args.choice
domains = args.domains

data = False
if ips or domains:
    data = sys.stdin.readlines()

arged = False
if target and choice:
    arged = True

if sys.version_info < (3, 0):
    input = raw_input




def menu():
    print('''
%s1.%s Censys
%s2.%s NS lookup
%s3.%s Port scan
%s4.%s Detect CMS
%s5.%s Whois lookup
%s6.%s Detect honeypot
%s7.%s Find subdomains
%s8.%s Reverse IP lookup
%s9.%s Detect technologies
%s0.%s All''' % (white, end, white, end, white, end, white, end, white, end, white, end, white, end, white, end, white, end, white, end))


def dog(choice, target):
    if not args.target:
        banner()
    if arged:
        hq(choice, target)
    else:
        while True:
            menu()
            result = False
            choice = input('\033[1;91m>>\033[0m ')
            hq(choice)


if data:
    kind = 'domain'
    if ips:
        kind = 'ip'
    targets = extractor(data, kind)
    if choice:
        for target in targets:
            print ('%s %s' % (run, target))
            hq(choice, target)
            print (red + ('-' * 60) + end)
    else:
        for target in targets:
            sys.stdout.write(target + '\n')
else:
    try:
        dog(choice, target)
    except KeyboardInterrupt:
        quit('')
