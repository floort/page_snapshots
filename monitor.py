#!/usr/bin/env python
###############################################################################
# Copyright (c) 2011, Floor Terra <floort@gmail.com>
# 
# Permission to use, copy, modify, and/or distribute this software for
# any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE
# FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
###############################################################################

import os
import urllib2

REPO_PATH = "/home/floort/devel/page_snapshots/"
DELAY = 30*60 # 30 minutes
MONITOR = (
    # ("url", "target_path"),
    ("https://www.google.com/intl/nl/+/policy/", "files/googleplus_nl.html"),
    ("https://www.dropbox.com/terms", "files/dropbox_en.html"),
    ("http://www.skype.com/intl/nl/legal/privacy/general/", "files/skype_nl.html"),
    ("https://twitter.com/privacy", "files/twitter_privacy.html"),
    ("http://www.facebook.com/policy.php?_fb_noscript=1", "files/facebook_privacy.html"),
)

# Get all the pages
for page in MONITOR:
    page_content = urllib2.urlopen(page[0]).read()
    open(page[1], "w").write(page_content)

# Try to commit
os.system("git add .")
os.system("git commit -a -m \"Automatic update\"")
os.system("git push")



