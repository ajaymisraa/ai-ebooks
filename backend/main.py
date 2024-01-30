from outline import *
from pdf import *

topic = "The Complete History of the Duke vs. UNC Rivalry"
audience = "everyone and basketball fans"
publisher = "Misra Publishing"
chaptercount = 5
sectioncount = 3

coverimg = cover(topic, audience)
outlines = outline(topic, audience, chaptercount, sectioncount)
ebook_json = content(topic, audience, outlines)

print(ebook_json)

print(f"Book created- {create_ebook(coverimg, ebook_json, publisher)}")