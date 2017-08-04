import md5

ss = 1

pass_in = raw_input("\nEnter the MD5 hash: ")
print ("\n==================================")
pwfile =  raw_input("\nEnter password list: ")
pw = (pwfile)
try:

        pwfile = open(pwfile, "r")
except:
        print("-------------------------------")
    	print("\n""["+pwfile+"]""File Not Found !! \n")
        exit()

for passw in pwfile:
      filemd5 = md5.new(passw.strip()).hexdigest()
      print("Trying password > %d:> %s")%(ss, passw.strip())

      ss +=1

      if pass_in == filemd5:
              print("----------------------------------")
              print("\nMD5 found >> Password is :> %s")%(passw)
              print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
              break

else:
    print("-------------------------------------")
    print("\n password Not found in >> %s"%(pw))
    print("-------------------------------------\n")

