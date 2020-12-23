"""
Helps translate a text by giving which words are used the most often
Common phrases (up to  depth words) are presented.
"""
def helper(filePath,depth=5): 
	aFile=open(filePath,'r')
	aFile=aFile.read()
	aFile=aFile.split()
	
	length=len(aFile)
	aList=[{} for _ in range(1,depth+1)]
	for i in range(length-depth+1):
	  for j in range( depth) :
	       text=" ".join(aFile[i:i+j+1])
	       if text in aList[j]:
	         aList[j][text]=aList[j][text]+1
	       else:
	         aList[j][text]=1
	print("success phase 1")
	print(i)
	for j in range(length-i) :
	       print(j,i+j)
	       text=" ".join(aFile[i:i+j+1])
	       if text in aList[j]:
	         aList[j][text]=aList[j][text]+1
	       else:
	         aList[j][text]=1
	         
	aList2=[sorted([[aDict[x],x] for x in aDict],reverse=True) for aDict in aList]
	return aList2 

         
         

       
    
