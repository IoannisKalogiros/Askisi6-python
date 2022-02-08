import random

# Πόντοι μαύρου
pointsB = 0

# Πόντοι άσπρου
pointsW = 0

for i in range(100):

    # Κάθετες θέσεις κομματιών
    QueenV = random.randrange(1,9)
    BishopV = random.randrange(1,9)
    RookV = random.randrange(1,9)

    # Οριζόντιες θέσεις κομματιών (Αντιστοιχία στα γράμματα Α = -8 , Β = -7 , C = -6 κλπ.)
    QueenH  = random.randrange(-8,0,1)
    BishopH = random.randrange(-8,0,1)
    RookH = random.randrange(-8,0,1)

    if QueenH == RookH or QueenV == RookV:
        pointsB+=1
        pointsW+=1
    
    if QueenV == BishopV or QueenH == BishopH:
        pointsB+=1

    else:

        for j in range(8):
        
            # Αύξων θέσεις
            if QueenV + 1 < 8:
                x1= QueenV +1
            else:
                x1 = QueenV
            
            if QueenH + 1 < -1:
                y1= QueenH + 1
            else:
                y1= QueenH

            # Φθήνων θέσεις
            if QueenV - 1 > 1:
                x2= QueenV - 1
            else:
                x2= QueenV

            if QueenH - 1 > -8:
                y2= QueenH - 1
            else:
                y2= QueenH

            # Συνθήκη για όταν το πιόνι κινέται προς τα δεξιά και πάνω πχ (4,-5)-->(5,-4) ή (4,D)-->(5,E)
            if (x1 == BishopV) and (y1 == BishopV):
                pointsB+=1
                pointsW+=1

            # Συνθήκη για όταν το πιόνι κινέται προς τα αριστερά και κάτω  πχ (4,-5)-->(3,-6) ή (4,D)-->(3,C)
            elif (x2 == BishopV) and (y2 == BishopH):
                pointsB+=1
                pointsW+=1
                
            # Συνθήκη για όταν το πιόνι κινέται προς τα αριστερά και πάνω πχ (4,-5)-->(5,-6) ή (4,D)-->(5,C)
            elif (x1 == BishopV) and (y2 == BishopH):
                pointsB+=1
                pointsW+=1
            
            # Συνθήκη για όταν το πιόνι κινέται προς τα δεξιά και κάτω πχ (4,-5)-->(3,-4) ή (4,D)-->(3,E)
            elif (x2 == BishopV) and (y1 == BishopH):
                pointsB+=1
                pointsW+=1
                
print ("O mauros exei shmeiwsei ",pointsB,"pontous")
print ("O aspros exei shmeiwsei",pointsW,"pontous")