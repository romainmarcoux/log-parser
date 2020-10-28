# log-parser

## Help

log-parser.py --help

usage: parse_log.py [-h] [-f FIELDS [FIELDS ...]] [-g FIELD REGEX] [-n] log [log ...]

positional arguments:
  log

optional arguments:
  -h, --help            show this help message and exit
  -f FIELDS [FIELDS ...], --fields FIELDS [FIELDS ...]
                        list des champs a afficher, par defaut tous
  -g FIELD REGEX, --grep FIELD REGEX
                        n'afficher que les logs ou le champ FIELD correspond a REGEX
  -n, --field-names     afficher les noms des champs pour chaque log

## Example :

### Logs of Fortinet FortiGate firewall

**Source** :

> "itime=1601541343","date=2020-10-01","time=10:38:55","devid=FGxxxxxxxxxxx","vd=xxxx","type=""traffic""","subtype=""forward""","action=""accept""","appcat=""unscanned""","","","","","devname=xxxxx","dstcountry=""Reserved""","dstintf=""xxxx""","dstintfrole=""lan""","dstip=172.16.0.1","dstport=53","dtime=1601548735","duration=180","eventtime=1601541535","","idseq=xxxxxxxx","level=""notice""","logid=""0000000013""","logver=60","policyid=xx","policytype=""policy""","poluuid=""xxxxxx""","proto=17","rcvdbyte=117","","rcvdpkt=1","sentbyte=62","","sentpkt=1","service=""DNS""","sessionid=xxxxx","srccountry=""Reserved""","srcintf=xxxxx","srcintfrole=""undefined""","srcip=192.168.0.10","srcport=56948","trandisp=""noop""","","","","vpn=""xxxxx""","vpntype=""ipsec-dynamic"""

**Command** :

> log_parser.py example.txt -f date time srcip dstip dstport

**Result** :

> 2020-10-01 10:38:55 192.168.0.10 172.16.0.1 53
