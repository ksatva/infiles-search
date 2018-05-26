#!/usr/bin/python3
#Filename: infiles.py
#Objective: To search for a word/string inside UNICODE files (txt, py, log, c... etc.)

import os ,time

def infiles():
   print('\n[START]...............I shall look search-key inside UNICODE files only.....')
   print('search-path : ',end='')
   path = input()
   
   if not os.path.exists(path):
   	print('!!! warning ENTER VALID PATH...')
   	print('search-path : ',end='')
   	path = input()
   	if not os.path.exists(path):
           return '!!!ERROR: INVALID PATH (run again and enter valid path)'
   
   print('search-key : ',end='')
   key = input()
   
   
   
   # fUNCTION: Writing search record to a file 'filepath' 
   def outputfile():
      filename = str(int(time.time()))+'infiles'+'.txt'
        
      # Enter THE PATH FOR RECORD WRITING (invalid path will lead to !!!ERROR...)
      filepath = input('Enter Absolute Directory Path to store Search log: ')
        
      #ENTER PATH for a permanent log directory and COMMENT OUT line 19, UNCOMMENT line 22
      #filepath ='...Enter "directory path" for Search log file....' 
        
      if not os.path.exists(filepath):
         print('!!! warning ENTER VALID DIRECTORY PATH...')
         filepath = input('Enter Absolute Directory Path to store Search log: ')
         if not os.path.exists(filepath):
            return -1
   
      filepath = filepath+filename
      return filepath
     
   
   filepath = outputfile()
   print('Creating search log %s'%filepath)
   try:
      outputdatafile =open(filepath, 'a')
      outputdatafile.write(('search-path: '+path+'\n'+'search-key: '+key+'\n\n'))
   
      fcount=count=exception=0
      print('\nsearching for "%s"...'%key)
     
      for f,s,files in os.walk(path):
        
         for file in files:	
            pathTemp = (f+'/'+file)
            #print(pathTemp)	
            #count+=1
            #path = f+'/'+str(file[count])
            #print(path)
            try:
               fileTemp = open(pathTemp)
               fcount+=1
               #print(fileTemp)
               for line in fileTemp:
                  fileLine = fileTemp.readline()
                  #print(fileLine) 					
                  if key in fileLine:
                     count+=1
                        
                     writestring = '\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...HIT...~~~~~~\n\
    Found in: %s\n\
    %s\n\
    Path: %s\n\
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n'%(file,  fileLine,  pathTemp)
                        
                     outputdatafile.write(writestring)
                     break
                        
               fileTemp.close()
            except:
               exception+=1
               

      outputdatafile.close()
      print('TOTAL FILES ATTEMPTS = %d'%fcount)
      print('MATCH in %d files'%count)
      print('EXCEPTION (NON-UNICODE FILES)= %d'%exception)
      print('RECORD WRITTEN: %s'%filepath)
   
   except:
      print('\n!!!ERROR: CANNOT CREATE RECORD FILE (Invalid path for log file LINE 19)!!!')
      
  
if __name__ == '__main__':
   infiles() 
   print('\n................search complete-infiles [END]\n')
   
   



#...WRITTEN BY KISHORE. DATE: DECEMBER 2017   
