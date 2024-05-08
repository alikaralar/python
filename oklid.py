klavuz = """
                          00                                                     
                          00                                                     
                          00                                                     
             Y2 ----------00----00                                               
                          00    00000                                            
                          00    0   000                                          
                          00    0     0000                                       
                          00    0        000                                     
                          00    0           000                                  
                          00    0             000                                
                          00    0                000                             
                          00    0                  0000                          
                          00    0                     000                        
                          00    0                       0000                     
             Y1 ----------00----00000000000000000000000000000                    
                          00    |                           |                     
                     0000000000000000000000000000000000000000000000              
                          00    |                           |                     
                          00    X1                          X2          
"""
print(klavuz)

koordinat = list(map(int, input("Lütfen koordinatlari (x2 x1 y2 y1) giriniz: ").split()))

points = [(koordinat[0],koordinat[1]), (koordinat[2],koordinat[3])]


distances = []
for i in points:
    distances.append(i[0]-i[1])
distance = ((pow(distances[0],2)) + (pow(distances[1],2))) ** (0.5)
print("Minimum Öklid Mesafesi: ", distance)
    

