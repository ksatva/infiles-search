SCRIPT NAME: infiles.py
WRITTEN BY: KISHORE
DATE: DECEMBER 2017

FOR COMMAND LINE USE
VALIDATED: The script infiles.py is written in Python3 and tested successfully in a linux system (Ubuntu). 

OBJECTIVE: To look for keywords or strings inside UNICODE files in the filesystem.

RUNNING the Program:
1) Use python3 to execute the program.
2) On execution the user is promted for:
	
	search-path: 
	search-key:
	Enter Absolute Directory Path to store Search log: 
	
3) Upon entering the 3 parametes, the program will scan the entire directory tree of the 'search-path'
   and look for the 'search-key'  inside the encountered UNICODE files in the directory tree, 
   and create a search logfile in the entered path.
   
   NOTE: If the "search-path" or "Enter Absolute Directory Path to store Search log:" does not exist !!!ERROR will result.
         Correct it by entering a valid Absolute Path.
      
4) On completion of execution, the program generates the following data:
	
	TOTAL FILES ATTEMPTS = "This value is the total number of files scan attempts-UNICODE and non-UNICODE files"
	MATCH in 'x' files ('x' is the number of files in which there was a positive hit')
	EXCEPTION (NON-UNICODE FILES) = "This value is the number of non-UNOCODE files"
	RECORD WRITTEN:	"Path and Name of the Search Record log FILE"
	
5) Open the RECORD WRITTEN file to find the matches.
   The file contains data in following format:
   	
   	file name (where match is found)
   	the line in which there is a match
   	the Path of the file
   

END NOTE: To run from linux system terminal, enter the directory containing script infiles.py,
	  and use following commands:
		
		python infiles.py
		
	  OR, to make the file executable use
		
		chmod +x infiles.py
 	  
 	  then run using 
		
		./infiles.py
   	
   	

THANK YOU
BEST REGARDS
KISHORE 
   	
   	
   	
	
	
