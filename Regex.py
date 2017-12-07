import re

phregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
'''mo = phregex.search('Hello PatiDar My numebr is 561-443-3423 and 435-324-2345')

print("Your number is " + mo.group()) '''


arearegex = re.compile(r'(\d\d\d)?-\d\d\d-\d\d\d\d')
'''print(arearegex.search('561-443-3423 and 324-2345').group(2))'''

asterikregex = re.compile(r'\W+')
'''print(asterikregex.search('Hello 12334 Hello 34224234'))
print(asterikregex.findall('Hello 12334 Hello 34224234')) '''

insenseregex = re.compile(r'RoBoCOP',re.I)
'''print(insenseregex.search('ROBOCOP'))'''

agentnamerex = re.compile(r'Agent (\w)')
'''print(agentnamerex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))'''

testrex = re.compile(r'[a-zA-Z0-9]+@[a-z]+\.[a-z]+')
'''print(testrex.search(r'help@nostarch.com'))'''

urlrex = re.compile(r'^http(s)?://\w+')
'''print(urlrex.search(r'https://abc.com '))'''

daterex = re.compile(r'\d{2}[-/]\d{2}[-/]\d{4}')
# daterex = re.compile(r'[012][0-9]|[3][01]/|-[0][0-9]|[1][12]/|-\d{4}')
# print(daterex.search('31-12-2015').group())
# print(len(daterex.findall('31-12-2015 21-11-2394')))

'''print(daterex.sub(daterex.search('31-12-2015').group(0),r'hello its 05-12-2017'))'''

def formatdate(search):
    print(search)
    daterex = re.compile(r'\d{2}([-/])\d{2}([-/])\d{4}')
    length = len(daterex.findall(search))
    for i in range(0,length):
        date = daterex.findall(search)[i]
       # a=re.sub('[/-]','',daterex.findall(search)[i])
        change = daterex.sub(r'',search)
        print(change)


# formatdate('Hello It\'s 05-12-2017 and tomorrow it\'ll be 06/12/2017')

def formatpara(para):
    paraspacerex = re.compile(r'/s{2,}')
    pararepeatrex = re.compile(r'\b(\w+)(\s+\1\b)+',re.I)
    paraexclarex  = re.compile(r'(!)+')
    print(re.sub(pararepeatrex,r'\1',para))
    print(re.sub(paraexclarex, '!', para))
    print(paraexclarex.search(para))


# formatpara("Hello hello Shubham   Shubham!!! ")

def passwordsecure(password):
    passwordrex = re.compile(r'[a-zA-Z0-9]{8,}')
    print(passwordrex.match(password))

# passwordsecure('Ab14234')

numberex = re.compile(r'(^\d{1,3}$)(,\d{3})+$')
# print(numberex.search('6,368,745'))

nakamatorex = re.compile(r'^[A-Z](\w)*\sNakamoto$')
# print(nakamatorex.search('Robocop Nakamoto'))

somerex = re.compile(r'(Alice|Bob|Carol)\s',re.I)
# print(somerex.search('Alice '))

def striprex(input,replacement):
    if  replacement:
        rex = re.compile(replacement)
        print(re.sub(rex,'',input))
    else:

        print(re.sub(re.compile(r'^\s+|\s+$'), '', input))
# striprex('    Hello $Pati Pati   Hello    ','')

lookaheadrex = re.compile(r'(?<!bat)man')
# print(lookaheadrex.search('batman and batwoman'))

telephonerex = re.compile(r'^(7|8|9)(\d{9})$')
# print(rex.search('852347890'))

emailhackrex =re.compile(r'(<)([A-Za-z])([A-Za-z-._0-9]+)@[A-Za-z]+\.[A-Za-z]{1,3}(>)')
# print(emailhackrex.search(r'<vineet@gmail]com>').group())

noncapture = re.compile(r'(?:ab)(c)')
# print(noncapture.search('abc').group(1))

hexrex = rex = re.compile(r'(?<!^)(#)([0-9A-F]{3})|((#)[0-9A-F]{6})', re.I)
# print(hexrex.search('{ \n color: #FfFdF8; background-color:#aef;'))






