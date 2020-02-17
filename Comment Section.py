comment = []

def AddEdge(end, to):
	comment.append( (end, to) )

def PrintDeep(point,depth):
	for a,b in comment:
		if(point == a):
			indent = "\t"*depth; print(indent, end="")
			print(a,"-->",b)
			PrintDeep(b,depth+1)

AddEdge('a', 'b')
AddEdge('b', 'c')
AddEdge('b', 'd')
AddEdge('b', 'e')
AddEdge('c', 'e')
AddEdge('c', 'f')
AddEdge('d', 'g')
AddEdge('g', 'h')
AddEdge('h', 'j')
AddEdge('h', 'k')
AddEdge('h','l')

PrintDeep('a',0)