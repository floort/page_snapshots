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
    ("http://legaldoc.dl.playstation.net/ps3-eula/psn/h/h_privacy_en.html", "files/sony_psn_privacy.html"),
    ("http://www.apple.com/privacy/", "files/apple_privacy.html"),
    ("http://www.t-mobile.nl/Global/media/pdf/privacy-statement.pdf", "files/tmobile_privacy.pdf"),
    ("http://www.opta.nl/nl/disclaimer/", "files/opta_privacy.html"),
    ("https://www.sidn.nl/fileadmin/docs/PDF-files_NL/Algemene%20voorwaarden%20voor%20.nl-domeinnaamhouders.pdf", "files/sidn_algemene_voorwaarder_nl.pdf"),
    ("https://www.sidn.nl/fileadmin/docs/PDF-files_NL/Algemene_voorwaarden_.nl_Control_domeinnaamhouders.pdf", "files/sidn_algemene_voorwaarder_nl_control.pdf"),
    ("https://www.sidn.nl/fileadmin/docs/PDF-files_NL/Algemene_voorwaarden_voor_registrars.pdf", "files/sidn_algemene_voorwaarder_registrars.pdf"),
    ("https://www.sidn.nl/fileadmin/docs/PDF-files_NL/Algemene_voorwaarden_voor_affiliates.pdf", "files/sidn_algemene_voorwaarder_affiliates.pdf"),
    ("https://www.sidn.nl/fileadmin/docs/PDF-files_NL/Technische%20eisen%20voor%20registratie%20van%20.nl-domeinnamen.pdf", "files/sidn_technische_eisen.pdf"),
    ("http://www.hi.nl/Privacy.htm", "files/hi_privacy.html"),
    ("https://mtvmobile.nl/privacystatement", "files/mtvmobile_privacy.html"),
    ("http://www.hyves.nl/privacy/", "files/hyves_privacy.html"),
    ("http://www.rabomobiel.nl/rabomobiel/footer/privacy", "files/rabomobiel_privacy.html"),
    ("http://overupc.upc.nl/disclaimer-privacy/", "files/upc_privacy.html"),
    ("http://www.online.nl/voorwaarden/privacy-statement/", "files/online_privacy.html"),
    ("http://www.sizz.nl/privacy/", "files/sizz_privacy.html"),
    ("http://static.ziggo.nl:443/images/Privacybeleid%20Ziggo_tcm14-2127.pdf", "files/ziggo_privacy.pdf"),
    ("http://thuis.eneco.nl/privacystatement/", "files/eneco_privacy.html"),
    ("http://www.nuon.nl/disclaimer.jsp", "files/nuon_disclaimer.html"),
    ("http://www.essent.nl/content/sitevoorwaarden/privacyverklaring.html", "files/essent_privacy.html"),
    ("http://www.nederlandenergie.nl/algemeen/privacybeleid", "files/nem_privacy.html"),
    ("https://pim.bof.nl/over-ons/privacy-verklaring/", "files/pim_privacy.html"),
    ("http://www.linkedin.com/static?key=privacy_policy", "files/linkedin_privacy.html"),
)

# Get all the pages
for page in MONITOR:
    print page[0]
    page_content = urllib2.urlopen(page[0]).read()
    open(page[1], "w").write(page_content)

# Try to commit
os.system("git add .")
os.system("git commit -a -m \"Automatic update\"")
os.system("git push")



