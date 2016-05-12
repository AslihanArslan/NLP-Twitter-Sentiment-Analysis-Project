
import nltk
import re

text_file = open("/home/aslihan/Desktop/NLP/mydata2.txt", "r")
asli=text_file.readlines()

before_normalize=' '.join(asli)
before_normalize=re.sub(' +',' ',before_normalize)
#print (before_normalize)

print ("##################################################")

aaa=before_normalize.split(" ")
#print (aaa)
for i in range(len(aaa)):
    ####### HTTPLERİ TEMİZLEME
    if aaa[i].find("http")!= -1:
        if aaa[i].startswith("http"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""
        else :
            aaa[i]="" 
    ####### � TEMİZLEME           
    elif aaa[i].find("�")!=-1:
        if aaa[i].startswith("�"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("�","") 
        else :
                aaa[i]=aaa[i].replace("�","")
    ####### ☀ TEMİZLEME 
    elif aaa[i].find("☀")!=-1:
        if aaa[i].startswith("☀"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("☀","") 
        else :
                aaa[i]=aaa[i].replace("☀","") 
                                  
    ####### @ TEMİZLEME           
    elif aaa[i].find("@")!=-1:
        if aaa[i].startswith("@"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]="" 
        if aaa[i].startswith("@ "):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""         
        elif (aaa[i].startswith("(@") or aaa[i].startswith("( @")):  
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""                    
       
        else :
            aaa[i]=""         
   
    ####### RT TEMİZLEME
    elif aaa[i].find("RT")!=-1:        
        if aaa[i].startswith("RT"):  
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""       
        else :
            aaa[i]="" 
                    
    ####### # TEMİZLEME
    elif aaa[i].find("#")!=-1:        
        if aaa[i].startswith("#"):  
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""       
        else :
            aaa[i]=""
    
    ####### " TEMİZLEME
    elif aaa[i].find('"')!=-1:   
        if aaa[i].startswith('"'): 
            if aaa[i].endswith(":"):
                aaa[i]=""
            else :
                aaa[i]=aaa[i].replace('"',"")  
        else :
                aaa[i]=aaa[i].replace('"',"")
                
                
    ####### ✌ TEMİZLEME 
    elif aaa[i].find("✌")!=-1:
        if aaa[i].startswith("✌"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("✌","") 
        else :
                aaa[i]=aaa[i].replace("✌","") 
    ####### ✌ TEMİZLEME 
    elif aaa[i].find("✌")!=-1:
        if aaa[i].startswith("✌"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("✌","") 
        else :
                aaa[i]=aaa[i].replace("✌","")             
    
    ####### "☔️" TEMİZLEME 
    elif aaa[i].find("☔️")!=-1:
        if aaa[i].startswith("☔️"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("☔️","") 
        else :
                aaa[i]=aaa[i].replace("☔️","")                         
                        
    ####### . TEMİZLEME
    elif aaa[i].find(".")!= -1:
        if aaa[i].startswith("."):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=""
        elif aaa[i].endswith("."):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace(".","")       
        else :
            aaa[i]=aaa[i].replace(".","")    
    
    ####### ! TEMİZLEME
    elif aaa[i].find("!")!= -1:
        if aaa[i].startswith("!"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace("!","")
        elif aaa[i].endswith("!"):
            aaa[i]=aaa[i].replace("!","")
        else:
            aaa[i]=aaa[i].replace("!","")      
    ####### ? TEMİZLEME
    elif aaa[i].find('?')!=-1:   
        if aaa[i].startswith("?"): 
            aaa[i]=aaa[i].replace("?","") 
        elif aaa[i].endswith("?"): 
            aaa[i]=aaa[i].replace("?","")  
        else: 
            aaa[i]=aaa[i].replace("?","") 
            
    ####### , TEMİZLEME
    elif aaa[i].find(',')!=-1:   
        if aaa[i].startswith(","): 
            aaa[i]=aaa[i].replace(",","") 
        elif aaa[i].endswith(","): 
            aaa[i]=aaa[i].replace(",","")  
        else: 
            aaa[i]=aaa[i].replace(",","")  
    ####### \ TEMİZLEME
    elif aaa[i].find("'\'")!=-1: 
        if aaa[i].startswith("'\'"):
            aaa[i]=aaa[i].replace(aaa[i],"") 
        elif aaa[i].endswith("'\'"): 
            aaa[i]=aaa[i].replace(aaa[i],"\n")  
        else: 
            aaa[i]=aaa[i].replace(aaa[i],"")                      
    ####### w/ TEMİZLEME
    elif aaa[i].find("w/")!=-1: 
        if aaa[i].startswith("w/"):
            aaa[i]=aaa[i].replace(aaa[i],"") 
        elif aaa[i].endswith("'w/'"): 
            aaa[i]=aaa[i].replace(aaa[i],"\n")  
        else: 
            aaa[i]=aaa[i].replace(aaa[i],"") 
    ####### ” TEMİZLEME
    elif aaa[i].find("”")!=-1: 
        if aaa[i].startswith("”"):
            aaa[i]=aaa[i].replace("”","") 
        elif aaa[i].endswith("”"): 
            aaa[i]=aaa[i].replace("”","\n")  
        else: 
            aaa[i]=aaa[i].replace("”","")                
    ####### “ TEMİZLEME
    elif aaa[i].find("“")!=-1: 
        if aaa[i].startswith("“"):
            if aaa[i].endswith("”"): 
                if aaa[i].endswith("\n"):
                    aaa[i]=aaa[i].replace("”","\n") 
                    aaa[i]=aaa[i].replace("“","")
                else:
                    aaa[i]=aaa[i].replace("”","") 
                    aaa[i]=aaa[i].replace("“","")
            else:
                aaa[i]=aaa[i].replace("”","")               
       
        else: 
            aaa[i]=aaa[i].replace("“","")
    
    ####### ; TEMİZLEME
    elif aaa[i].find(";")!=-1: 
        if aaa[i].startswith(";"):
            aaa[i]=aaa[i].replace(";","") 
        elif aaa[i].endswith(";"):
            if aaa[i].endswith("\n"):
                aaa[i]=aaa[i].replace(";","\n") 
            else:
                aaa[i]=aaa[i].replace(";","")  
        else: 
            aaa[i]=aaa[i].replace(";","")
    
    ####### - TEMİZLEME
    elif aaa[i].find("-")!=-1: 
        if aaa[i].startswith("-"):
            aaa[i]=aaa[i].replace("-"," ") 
        elif aaa[i].endswith("-"): 
            aaa[i]=aaa[i].replace("-","\n")  
        else: 
            aaa[i]=aaa[i].replace("-"," ")                 
    
    ####### ' TEMİZLEME
    elif aaa[i].find("'")!=-1: 
        if aaa[i].startswith("'"):
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("'","\n")
            else:    
                aaa[i]=aaa[i].replace("'","") 
        elif aaa[i].endswith("'"): 
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("'","\n")  
        else: 
            aaa[i]=aaa[i].replace("'","")
    ####### … TEMİZLEME
    elif aaa[i].find("…")!=-1: 
        if aaa[i].startswith("…"):
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("…","\n")
            else:    
                aaa[i]=aaa[i].replace("…","") 
        elif aaa[i].endswith("…"): 
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace("…","\n")
            else:
                aaa[i]=aaa[i].replace("…","")     
        else: 
            aaa[i]=aaa[i].replace("…","")                     
    
    ####### ) TEMİZLEME
    elif aaa[i].find(")")!=-1: 
        if aaa[i].startswith(")"):
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace(aaa[i],"\n")
            else:    
                aaa[i]=aaa[i].replace(")","") 
        elif aaa[i].endswith(")"): 
            if aaa[i].endswith("\n"): 
                aaa[i]=aaa[i].replace(aaa[i],"\n")
            else:
                aaa[i]=aaa[i].replace(")","")     
        else: 
            aaa[i]=aaa[i].replace(")","")      
    ####### emoji shortcut TEMİZLEME
    elif aaa[i].find(":")!=-1:
        if aaa[i].startswith(":"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace(":","") 
        elif aaa[i].endswith(":"):
            if aaa[i].endswith("\n"):
                aaa[i]="\n"
            else :
                aaa[i]=aaa[i].replace(":","")
        else :
             aaa[i]=aaa[i].replace(":","")              
      
    ''' 
    
   
    '''       
        
after_normalize=' '.join(aaa)
after_normalize=re.sub(' +',' ',after_normalize)
print (after_normalize)
text_file2 = open("/home/aslihan/Desktop/NLP/myclean.txt", "w")
text_file2.write(after_normalize)
text_file2.close()
print("########################################")

print (type(after_normalize))


    
   
    
  
    
    

