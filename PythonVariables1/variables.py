# Assigning Varibales
 
name = "Mwanzia Kimwele"    # String
name

age = 20                    # Integer
age

male = True                 # Boolean
male


yea_of_birth = 1999 - age     # Operations
yea_of_birth

interests = [               # List
            'Web design', 
            'Media', 
            "sports" ] 
interests

summary = {                 # Dictionary
    "Name":       name,
    "Age":        age,
    "Birth year": birth_year,
    "Height":     height,
    "Interests":  interests,
}
summary

# Scope
# =======

# Local Scope
def scope():
    campus = "TRC"
              # Returns
print(campus) # NameError: name 'campus' is not defined


# Global Scope
school = "Zetech"

def scope():
    global school   # Keyword 'global'
    school = "Zetech"

scope()
print(School)       # Returns "Zetech"

# Without key word
School = "Zetech"

def scope():
    School = "Zetech"

scope()
print(School)       # Returns "Zetech"
