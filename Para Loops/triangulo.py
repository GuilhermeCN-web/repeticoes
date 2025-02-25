tri = 1
counter = 0

while counter < 7:
    
    if counter == 0:    
        print(tri)

    if counter == 1:
        print(tri, tri)
        
    if counter == 2:
        print(tri, tri + tri, tri)
        
    if counter == 3:
        print(tri, tri * 3, tri * 3, tri)
        
    if counter == 4:
        print(tri, tri * 4, tri * 6, tri * 4, tri)
        
    if counter == 5:
        print(tri, tri * 5, tri * 10, tri * 10, tri * 5, tri)
        
    if counter == 6:
        print(tri, tri * 6, tri * 15, tri * 20, tri * 15, tri * 6, tri)
    counter += 1