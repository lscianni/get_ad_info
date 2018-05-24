#!/usr/bin/env python
# -*- conding:utf-8 -*-
#

from ldap3 import  Server, Connection, ALL, NTLM
from sys import argv
from getpass import getpass

def get_args():
    try:
        get_args.username = argv[1]
        get_args.ad_server = argv[2]
        get_args.domain = argv[3]
        get_args.passwd = getpass()
        
    except IndexError:
        print('usage: ad_get_info.py username server domain')
        
def ad_get_info():
    get_args()
    server = Server(get_args.ad_server, get_info=ALL)
    conn = Connection(server, user='%s\\%s' % (get_args.domain, get_args.username), password=get_args.passwd, authentication=NTLM)
    conn.bind()
    print(conn)
    print(server.info)
    print(server.schema)
    conn.unbind()
    
if __name__ == '__main__':
    ad_get_info()
