"""
Get all tikz envirements in all latex files contained in a directory.
Tikz environments begin with "\begin{tikzpicture}"
and end with"\end{tikzpicture}". They are not supposed to be
contained in each other.
"""

from glob import glob
           
def getparts(beg,end,text):
    result=[]
    i=0
    while i<len(text)-len(beg):
        if text[i:i+len(beg)]!=beg:
            i=i+1
        else:            
            i=i+len(beg)
            i0=i
            while i<len(text)-len(end):
                if text[i:i+len(end)]!=end:
                    i=i+1
                else:
                     result.append( text[i0:i])
                     i=i+len(end)
                     break            
    return result



pattern="all_tex/*.tex" 
beg=r"\begin{tikzpicture}"
end=r"\end{tikzpicture}"
sep="\n \section{} \n "
outFileName="output1.tex"

listFiles=glob(pattern)
result=[]

for aFile in listFiles:
    try:
        aFileC=open(aFile,'r')
        content=aFileC.read()
        result=result+getparts(beg,end,content) 
    except:
        print(aFile)
        
result=list(set(result))        
result1=beg+" "+(end+sep+beg).join(result)+" "+end
outFile=open(outFileName,'w')
outFile.write(result1)






 
