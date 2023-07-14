# Write a program that extracts links from a given text. The text will come in the form of strings, each representing a
# sentence. You need to extract only the valid links from it. Example:
# "www.internet.com"
# The Sub-Domain must always be "www". The Domain name can consist of English alphabet letters (uppercase and lowercase),
# digits, and dashes ("–"). The Domain extension consists of one or more domain blocks, a domain block consists of a dot
# followed by one or more lowercase English alphabet letters, a Domain extension must have at least one domain block in
# order to be valid. The Sub-Domain and Domain name must be separated by a single dot. Any link that does NOT follow the
# specified above rules should be treated as invalid.
# Example incorrect links:
# • "ww.justASite.bg"
# • "lel.awesome.com"
# • "www.weird_site.hit.bg"
# • "www.no-symb#^ols-allow%ed.com"
# • "www.mark.12"
# • "www.web-site."
# • "www.example-site._*^#"
# Example of correct links:
# • "Some textwww.softuni.bg"
# • "Just a link in a www.sea-of-text.bg-swimming around"
# • "Instruments www.Instruments.rom.com.trombone2000 Instrument here"
# • "All your ice cream flavors-www.scream.for.ice.cream(We also have squirrels)"
# The output is all valid links you have found, printed – each on a new line.
#
# Input1:
# Join WebStars now for free, at www.web-stars.com
# You can also support our partners:
# Internet - www.internet.com
# WebSpiders - www.webspiders101.com
# Sentinel - www.sentinel.-ko
#
# Output1:
# www.web-stars.com
# www.internet.com
# www.webspiders101.com
#
# Input2:
# Need information about cheap hotels in London?
# You can check us at www.london-hotels.co.uk !
# We provide the best services in London.
# Here are some reviews in some blogs:
# London Hotels are awesome! - www.indigo.bloggers.com
# I am very satisfied with their services - ww.ivan.bg
# Best Hotel Services! - www.rebel21.sedecrem.moc
#
# Output2:
# www.london-hotels.co.uk
# www.indigo.bloggers.com
# www.rebel21.sedecrem.moc

import re

valid_urls = []
pattern = "(w{3}\.[a-zA-Z0-9-\.]+\.[a-z]+)"
line = input()

while line:
    matches = re.search(pattern, line)

    if matches:
        valid_urls.append((matches.group(1)))

    line = input()

for valid_url in valid_urls:
    print(valid_url)
