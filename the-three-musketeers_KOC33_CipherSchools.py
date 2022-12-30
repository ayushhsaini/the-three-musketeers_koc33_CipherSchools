
def romantointeger(t):
        conversions = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        number = 0
   
        for char in t:
            number += conversions[char]
        print(number)
      

q = str(input("enter the roman number: "))
solution = romantointeger(q)

 

        

        

        
