SCRIPT NAME: infiles.py
WRITTEN BY: KISHORE
DATE: DECEMBER 2017

CONTENTS:
   dir : infiles-master
 	  L file: infiles.py
 	  L file: README.txt
 	  L file: LICENSE
 	  L dir : searchlog
		     L file: readme.txt
  
USAGE: FOR COMMAND LINE USE (BASH OR PYTHON3)

VALIDATED: The script infiles.py is written in Python3 and tested successfully in a linux system (Ubuntu). 

OBJECTIVE: To look for keywords or strings inside UNICODE files in the filesystem.

DOWNLOADING (recommended):
 Download the zip file. 
 Extract.
 Run the program from the downloaded infiles directory (as pwd).

RUNNING the Program:
1) Use python3 to execute the program.
2) On execution the user is promted for:
	
	search-path: 
	search-key:
	
3) Upon entering the 2 parametes, the program will scan the entire directory tree of the 'search-path'
   and look for the 'search-key'  inside the encountered UNICODE files in the directory tree, 
   and create a search logfile in the directory ------->>> ./searchlog/ <<<------------
   
   NOTE: If the (a)"search-path" is invalid, or 
   		(b)"searchlog" (directory) does not exist in working directory (infiles.py script: line 29) 
         	!!!ERROR will result.
         Correct it (a) by entering a valid Absolute search-path.
         Correct it (b) by creating a directory in the pwd and name it 'searchlog'
      
4) On completion of execution, the program generates the following data:
	
	TOTAL FILES ATTEMPTS = "This value is the total number of files scan attempts-UNICODE and non-UNICODE files"
	MATCH in 'x' files ('x' is the number of files in which there was a positive hit')
	EXCEPTION (NON-UNICODE FILES) = "This value is the number of non-UNOCODE files"
	LOG WRITTEN:	"Absolute path of the Search log FILE"
	
5) Open the LOG WRITTEN file to find the 'search-key' matches.
   The file contains data in following format:
   	
   	file name (where match is found)
   	the line in which there is a match
   	the Path of the file
   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TROUBLESHOOT

A) message: !!!ERROR CODE: [searchlog]
   solution: CREATE A FOLDER in the current working directory and name it: searchlog
	(This folder will store the search logs for each time the infiles.py is run)

B) If using WINDOWS OS then EDIT LINE 29 replace ./searchlog/ with .\searchlog\ 
   Make sure the current working directory contain a folder named searchlog 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
