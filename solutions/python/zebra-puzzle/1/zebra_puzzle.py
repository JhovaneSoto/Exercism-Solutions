MAT=[]
def drinks_water():
    create_puzzle()
    idx=[idx for idx,row in enumerate(MAT[3]) if row==" "][0]
    return MAT[1][idx]

def owns_zebra():
    create_puzzle()
    idx=[idx for idx,row in enumerate(MAT[2]) if row==" "][0]

    return MAT[1][idx]

def create_puzzle():
    global MAT

    #COLOR, nationalities, own different pets, drink different beverages, enjoy different hobbies
    
    #There are five houses.
    MAT=[[" "]*5 for _ in range(5)]

    #The Norwegian lives in the first house.
    MAT[1][0]="Norwegian"
    MAT[0][0]="*"
    
    #The Norwegian lives next to the blue house.
    MAT[0][1]="Blue"
    
    #The person in the middle house drinks milk. 
    MAT[3][2]="Milk"

    #The green house is immediately to the right of the ivory house. 
    MAT[0][3]="Ivory"
    MAT[0][4]="Green"

    #The person in the green house drinks coffee
    MAT[3][4]="Coffee"

    #The person in the yellow house is a painter.
    MAT[0][0]="Yellow"
    MAT[4][0]="Painter"

    #The painter's house is next to the house with the horse.
    MAT[2][1]="Horse"
    
    #The Englishman lives in the red house.
    MAT[0][2]="Red"
    MAT[1][2]="English"

    #The Ukrainian drinks tea 
    MAT[1][1]="Ukrainian"
    MAT[3][1]="Tea"

    #The person who plays football drinks orange juice.
    MAT[4][3]="Football"
    MAT[3][3]="Orange Juice"

    #The Spaniard owns the dog.
    MAT[1][3]="Spaniard"
    MAT[2][3]="Dog"

    #The Japanese person plays chess.
    MAT[1][2]="Japanese"
    MAT[4][2]="Chess"
    
    #The snail owner likes to go dancing.
    MAT[2][4]="Snail"
    MAT[4][4]="Dance"

    #The person who enjoys reading lives in the house next to the person with the fox.
    MAT[2][0]="Fox"
    MAT[4][1]="Read"
    
    

    
    