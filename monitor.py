#!/usr/bin/env python

import sys
import urllib2
import datetime
import sha
import time

DELAY = 30*60 # 30 minutes
old_digest = ""


while True:
    page = urllib2.urlopen(sys.argv[1]).read()
    digest = sha.sha(page).hexdigest()
    if digest != old_digest:
        print "%s - Change in page (SHA = %s)" % (datetime.datetime.utcnow(), digest)
        f = open(str(datetime.datetime.utcnow()),"w")
        f.write(page)
        f.close()
        old_digest = digest
    time.sleep(DELAY)



