phrases=[
    "twelve Drummers Drumming", 
    "eleven Pipers Piping", 
    "ten Lords-a-Leaping", 
    "nine Ladies Dancing", 
    "eight Maids-a-Milking", 
    "seven Swans-a-Swimming", 
    "six Geese-a-Laying", 
    "five Gold Rings", 
    "four Calling Birds", 
    "three French Hens", 
    "two Turtle Doves", 
    "a Partridge in a Pear Tree."
]
days={ 
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}
def recite(start_verse, end_verse):
    return[make_verse(pos) for pos in range(start_verse,end_verse+1)]

def make_verse(num):
    out=phrases[len(phrases)-num:]
    if len(out)>1:
        out[-1]="and a Partridge in a Pear Tree."

    return f"On the {days[num]} day of Christmas my true love gave to me: "+", ".join(out)