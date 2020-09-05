st={'One','red','eARth',-9,'+4',22/4}
st.add('sky')
st.add('five hundred')
print(st)
st
print(type(st))

A={1,2,3,4,5}
B={5,6,7}
#union of two sets
print(A|B)

C=(A|B)
A.union(B)==B.union(A)
print(C)

print(A.intersection(B)) #intersection
print(A&B)

print(A-B) #difference
print(A.difference(B))
