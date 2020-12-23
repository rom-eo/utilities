"""
Removes column i from a latex table
"""

def remCol(text,i):
	lines=text.split(r"\hline")
	#print("len(lines)=",len(lines))
	table=[line.split("&") for line in lines]
	for line in table:
		if len(line)>i:
			line.pop(i-1)
	newTable=["&".join(line) for line in table]
	newTable="\hline".join(newTable)
	return newTable
	
	
def example():
	return r"""\begin{tabular}{|l||l||l||l||l||l|}
\hline
Week&Date &Chapter &Section&&Comments\\%Assignments
\hline
\hline
1&	Th 01/9&1&1&&Character building\\
\hline
1&	T 01/14&1&1,3&&\\
\hline
2&	Th 01/16&1&4&&\\
\hline
3&	T 01/21&1&5,6&&\\
\hline
3&	Th 01/23&1&&&Review\\%
\hline
4&	T 01/28& &&&Test 1\\
\hline
4&	Th 01/30&1&7&&\\
\hline
5&	T 02/04&2&1&&\\
\hline
5&	Th 02/06&2&2,3&&\\
\hline
6&	T 02/11&2&4&&\\
\hline
6&	Th 02/13&1,2&&&Review\\
\hline
7&	T 02/18&&&&Test 2\\
\hline
7&	Th 02/21&2&5&&\\
\hline
8&	T 02/25&2&6&&\\
\hline
8&	Th 02/26&3&1&&\\
\hline
9&	T 03/04&&&& %\textcolor{red}
{Spring Vacation}\\
\hline
9&	Th 03/06&&&&%\textcolor{red}
{Spring Vacation}\\
\hline
10&	T 03/11&3 &1&&\\
\hline
10&	Th 03/13&3&2&& \\
\hline
11&	T 03/18&3&2&&\\
\hline
11&	Th 03/20&3&3&& \\
\hline
12&	T 03/25&3&3&&\\
\hline
12&	Th 03/27&3&4&&\\
\hline
13&	T 04/01&3&4&&\\
\hline
13&	Th 04/03&3&4&&\\
\hline
14&	T 04/08&3&&&Review\\
\hline
14&	Th 04/10&&&&Test 3\\
\hline
15&	T 04/15&3&5&&\\
\hline
15&	Th 04/17&4&1&&\\
\hline
16&	T 04/21&4&2&& \\
\hline
16&	Th 04/23&&&&Review\\
\hline
16&	Th 04/28&&&&Review\\
\hline
17&	T 04/30&&&& \\
\hline
\end{tabular}""" 

print(remCol(example(),2))
 

          
