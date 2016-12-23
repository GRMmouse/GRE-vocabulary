import re
import urllib

# Globals are evil.
URL = "https://www.merriam-webster.com/dictionary/"
REG = r'<span class="intro-colon">:</span>\xc2\xa0 (.*?)</span></p></li>'
PAT = re.compile(REG)
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ;,."
# Globals are evil.

def getDefs(word):
    print "Opening page %s"%(URL+word)
    page = urllib.urlopen(URL+word)
    print "Reading..."
    html = page.read()
    print "Parsing..."
    imglist = re.findall(PAT,html)
    result = set()
    for word in imglist:
        temp = ""
        flag = True
        andFlag = 0
        spaceFlag = False
        for c in word:
            if andFlag >0:
                andFlag -=1
                continue
            elif c == "<":
                flag = False
                continue
            elif c == ">":
                flag = True
                continue
            elif c == "&":
                andFlag = 2
            elif c == " ":
                if not spaceFlag:
                    spaceFlag = True
                    temp += c
                continue
            if flag and (c in chars):
                spaceFlag = False
                temp+=c
        result.add(temp.strip())
    return result
   
def lookUp(word):
    print "*"*80
    result1 = getDefs(word)
    counter = 0
    print "The meaning of %s is:"%word
    for meaning in result1:
            counter += 1
            print "%d. %s"%(counter, meaning)
    print "*"*80

def test():
    lookUp("abatement")
    lookUp("abate")
    lookUp("adjourn")
