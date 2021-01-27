"""
nBASIC v1.0
by Gilbert TR
Coded poorly in Python
as a challenge
by the same guy
27 January, 2021
DONT LOOK AT THIS UGLY CODE
I CAN'T CODE A TRADITIONAL INTERPRETER
"""
import re, sys
debug=False
class nBASIC:
	def getOpcode(self,code,l):
		try: return code[str(l)]
		except: return None
	def getVar(self,vars,l):
		try: return vars[str(l)]
		except: return None
	def evalEq(self,code,vars,eq):
		#print(eq,file=sys.stderr)
		ops=[]
		ops.append("")
		strMode=False
		for x in eq:
			if not strMode:
				if x in "+-*/<>=": ops.append("")
				if x not in "\t ": ops.append(ops.pop()+x.lower())
			else:
				ops.append(ops.pop()+x)
			if x=='"':
				strMode=not strMode
		if ops[0].startswith('"') and ops[0].endswith('"'): res=ops[0][1:-1]
		elif self.getVar(vars,ops[0])!=None: res=self.getVar(vars,ops[0])
		else: res=float(ops[0])
		for x in ops[1:]:
			if x[0]=="+":
				if x[1:].startswith('"') and x[1:].endswith('"'): 
					res=str(res)
					res+=x[2:-1]
				elif self.getVar(vars,x[1:])!=None: res+=self.getVar(vars,x[1:])
				else: 
					try: res+=int(x[1:])
					except: res+=float(x[1:])
			elif x[0]=="-":
				if x[1:].startswith('"') and x[1:].endswith('"'): 
					res=str(res)
					res-=x[2:-1]
				elif self.getVar(vars,x[1:])!=None: res-=self.getVar(vars,x[1:])
				else: 
					try: res-=int(x[1:])
					except: res-=float(x[1:])
			elif x[0]=="*":
				if x[1:].startswith('"') and x[1:].endswith('"'): 
					res=str(res)
					res*=x[2:-1]
				elif self.getVar(vars,x[1:])!=None: res*=self.getVar(vars,x[1:])
				else: 
					try: res*=int(x[1:])
					except: res*=float(x[1:])
			elif x[0]=="/":
				if x[1:].startswith('"') and x[1:].endswith('"'): 
					res=str(res)
					res/=x[2:-1]
				elif self.getVar(vars,x[1:])!=None: res/=self.getVar(vars,x[1:])
				else: 
					try: res/=int(x[1:])    
					except: res/=float(x[1:])    
			elif x[0]=="<":
				if x[1:].startswith('"') and x[1:].endswith('"'): 
					res=str(res)
					res=res<x[2:-1]
				elif self.getVar(vars,x[1:])!=None: res=res<self.getVar(vars,x[1:])
				else: 
					try: res=res<int(x[1:])  
					except: res=res<float(x[1:])  
				res=int(res) 
			elif x[0]==">":
				if x[1:].startswith('"') and x[1:].endswith('"'): 
					res=str(res)
					res=res>x[2:-1]
				elif self.getVar(vars,x[1:])!=None: res=res>self.getVar(vars,x[1:])
				else: 
					try: res=res>int(x[1:])   
					except: res=res>float(x[1:])   
				res=int(res)
			elif x[0]=="=":
				if x[1:].startswith('"') and x[1:].endswith('"'): 
					res=str(res)
					res=res==x[2:-1]
				elif self.getVar(vars,x[1:])!=None: res=res==self.getVar(vars,x[1:])
				else: 
					try: res=res==int(x[1:])   
					except: res=res==float(x[1:])   
				res=int(res)
			if str(res)[-2:]==".0": res=int(res)
		if str(res)[-2:]==".0": res=int(res)
		if debug: print(eq+"="+str(res)+"("+str(ops)+")",file=sys.stderr)
		return res
	def runCode(self,code):
		code=code.strip().replace("\n",":").split(":")
		line={}
		vars={}
		maxLines=0
		for x in code:
			maxLines=max(int(re.findall("^[0-9]+",x)[0]),maxLines)
			line[re.findall("^[0-9]+",x)[0]]=re.split("^[0-9]+", x)[1].strip()
		code=line
		line=-1
		while True:
			line+=1
			if line>maxLines:
				break
			opcode=self.getOpcode(code,line)
			#print(opcode)
			if opcode==None:
				continue
			elif opcode.lower().startswith("print"):
				print(self.evalEq(code,vars,opcode[5:].strip()))
			elif opcode.lower().startswith("goto"):
				line=self.evalEq(code,vars,opcode[4:].strip())-1
			elif opcode.lower().startswith("input"):
				try: ui=input("? ")
				except: ui=""
				try: ui=float(ui)
				except: pass
				vars[opcode.lower()[5:].strip()]=ui
			elif opcode.lower().startswith("end"):
				sys.exit(0)
			elif opcode.lower().startswith("if"):
				temp=re.split("(?i)then",opcode[2:],re.IGNORECASE)
				if self.evalEq(code,vars,temp[0].strip()):
					line=self.evalEq(code,vars,temp[1].strip())-1
			elif opcode.lower().startswith("int"):
				vars[opcode.lower()[3:]]=int(vars[opcode.lower()[3:]])
			elif opcode.lower().startswith("rem"):
				continue
			elif re.findall("^[A-Za-z]\s*=", opcode.lower()):
				vars[opcode.lower()[0]]=self.evalEq(code,vars,re.split("^[A-Za-z]\s*=", opcode.lower())[1].strip())
			if debug: print(vars,file=sys.stderr)
basic=nBASIC()
basic.runCode(open(sys.argv[1]).read())