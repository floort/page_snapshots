#!/usr/bin/env python

import os
import urllib2

REPO_PATH = "/home/floort/devel/page_snapshots/"
DELAY = 30*60 # 30 minutes
MONITOR = (
    # ("url", "target_path"),
    ("https://www.google.com/intl/nl/+/policy/", "files/googleplus_nl.html"),
    ("https://www.dropbox.com/terms", "files/dropbox_en.html"),
    ("http://www.skype.com/intl/nl/legal/privacy/general/", "files/skype_nl.html"),
)

# Get all the pages
for page in MONITOR:
    page_content = urllib2.urlopen(page[0]).read()
    open(page[1], "w").write(page_content)

# Try to commit
os.system("git add .")
os.system("git commit -a -m \"Automatic update\"")
os.system("git push")



