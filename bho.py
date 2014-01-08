DISPIDSig = {}
DISPID = {}
def loadDISPIDSig():
	for line in file(r"small_DWebBrowserEvents.txt",'r'):
		line = line.split(" ")
		DISPIDSig[line[1]] = line[0]
		
def loadDISPID():
	for line in file(r"DWebBrowserEvents.txt",'r'):
		line = line.split(" ")
		DISPID[line[1]] = line[0]
		
loadDISPIDSig()		
loadDISPID()	
ea = 0
places = {}
for value in DISPIDSig.keys():
	print "Searching for %s" % value,
	while(1):	
		ea = FindImmediate(ea, SEARCH_DOWN | SEARCH_NEXT | SEARCH_NOSHOW, int(value))
		ea = ea[0]
		if ea == BADADDR:
			break	
		if GetMnem(ea) == "cmp":
			funcStart = GetFunctionAttr(ea,FUNCATTR_START)
			if funcStart != BADADDR:
				if not places.has_key(funcStart):
					places[funcStart] = 0
				places[funcStart] += 1
	ea = 0	

max = 0
invokeAddr = 0
for k,v in places.iteritems():
	if k != 0 and max < v:
		max = v
		invokeAddr = k
	print "Potential Invoke function 0x%x :  appearance %d" % (k,v)

print "Suggeste address of Invoke function : 0x%x " % invokeAddr
		
def bho_invoke(ea):
	funcStart = ea
	funcEnd = GetFunctionAttr(ea,FUNCATTR_END)
	for value,idName in DISPID.iteritems():
		while(1):	
			ea = FindImmediate(ea, SEARCH_DOWN | SEARCH_NEXT | SEARCH_NOSHOW, int(value))
			ea = ea[0]
			if ea == BADADDR or ea > funcEnd:
				break
			if GetMnem(ea) == "cmp":
				print "Found %s at: %x" %(idName,ea)
				MakeComm(ea,idName)
		ea = funcStart
