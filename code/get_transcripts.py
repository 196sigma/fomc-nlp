## Reginald Edwards
##
## 22 June 2018

import urllib, os, glob

transLinkList = os.listdir("data/minutes/txt")
transLinkList2 = []
for x in transLinkList:
    transLinkList2.append(int(x.split('.txt')[0]))
transLinkList3 = []
for x in transLinkList2:
    if x>=19940402:
        transLinkList3.append(x)
transLinkList4 = []
for x in transLinkList3:
    transLinkList4.append("http://www.federalreserve.gov/monetarypolicy/files/FOMC"+str(x)+"meeting.pdf")
# ["http://www.federalreserve.gov/monetarypolicy/files/FOMC20070131meeting.pdf"]

## try all possible dates
for year in range(2007):
  for month in range(1,13):
    for day in range(1, 31):
      fomc_url = "http://www.federalreserve.gov/monetarypolicy/files/FOMC%s%s%smeeting.pdf" % (year,month,day)
for transLink in transLinkList4:
    transName = transLink.split('/')[-1]
    outfile = open("data/transcripts/"+transName, 'wb')
    outfile.write(urllib.urlopen(transLink).read())
    outfile.close()

# convert to text files
infileList = os.listdir("data/transcripts/")
for aFile in infileList:
    fileName = aFile.split('.pdf')[0]
    os.system("pdftotext -enc UTF-8 data/transcripts/"+aFile + " data/transcripts_text/"+fileName+".txt")

# convert character set
infileList = os.listdir("data/transcripts_text")

for aFile in infileList:
  outfileName = aFile.replace('txt','cleaned')
  
  os.system("iconv data/transcripts_text/"+aFile+" -f ISO-8859-1 -t UTF-8 -c -o "+ "data/transcripts_text_cleaned/" + outfileName)
