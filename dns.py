#!/usr/bin/env python
# Coded By: Dwirn
# Twitter: @dwirn1337
# Telegram: @dwirn1337
# Github: github.com/dwirn1337
# WhatsApp: +55 11 94380-9900


from os import system
from sys import argv
from socket import gethostbyname

try:
    from dns import resolver, reversename
except:
    system("pip install dnspython3")
    from dns import resolver, reversename

def main(url):
    ids = [
           'A','NS','MD','MF','CNAME','MB','MG','MR','NULL','WKS','HINFO','MINFO',
           'MX','TXT','RP','AFSDB','X25','ISDN','RT','NSAP','NSAP-PTR','SIG','PX',
           'KEY','GPOS','AAAA','LOC','NXT','SRV','NAPTR','KX','CERT','A6','DNAME',
           'OPT','APL','SSHFP','IPSECKEY','RRSIG','NSEC','DNSKEY','DHCID','CSYNC',
           'DS','NSEC3','NSEC3PARAM','TLSA','HIP','CDNSKEY','CDS','TKEY','UNSPEC',
           'EUI48','EUI64','SPF','TSIG','IXFR','AXFR','MAILB','MAILA','ANY','URI',
           'CAA','TA','DLV','PTR'
          ]

    if url1.startswith("http://") == True:
        host = url1[7:]
    elif url1.startswith("https://") == True:
        host = url1[8:]
    else:
        host = url1

    print ("\n\033[1;32m[+] Buscando DNS . . .\033[0m")

    for a in ids:
        try:
            res = resolver.Resolver()

            res.nameservers = ['8.8.8.8', '8.8.4.4']
            answers = res.query(host, a)

            for rdata in answers:
                print("\033[1;32m[+] (" + a + ") \033[1;37m{}\033[0;0m".format(rdata.to_text()))

        except Exception as xrxr:
            continue

    try:
        if host[1].isdigit():
            ip = host
        else:
            ip = gethostbyname(host)

        print ("\033[1;32m[+] (reverse)\033[0m {}".format(str(ip)))

    except:
        pass

if __name__ == '__main__':
    try:
        url1 = argv[1]

        main(url1)

    except:
        print("[+] Use: {} <url>".format(argv[0]))
