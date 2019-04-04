from Matrix import Matrix as matrix

m1 = matrix(1,2,3,4,5,6,7,8,9)
m2 = matrix(1,2,3,4,5,6,7,8,9)

##########SUM#########
print("m3 = m1 + m2")
m3 = m1 + m2
m1.print_matrix(m3)

print("m1 += m2")
m1 += m2
m1.print_matrix(m1)

print("m4 = m1 + 2")
m4 = m1 + 2
m1.print_matrix(m4)

print("m4 = 2 + m1")
m4 = m1 + 2
m1.print_matrix(m4)

#######PRODUCT########
print("m4 = m1 @ m2")
m5 = m1 @ m2
m1.print_matrix(m5)

print("m1 @= m2")
m2 @= m1
m1.print_matrix(m2)

######SUBTRACTION#####
print("m5 = m1 - m2")
m6 = m1 - m2
m1.print_matrix(m6)

print("m1 -= m2")
m1 -= m2
m1.print_matrix(m1)
