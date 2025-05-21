"""Looping through a list"""

# license plates
license_plates = [
    "LWO 756",
    "28C 382",
    "9LU 094",
    "ZSG 951",
    "727 37O",
    "36Q 759",
    "365 IHN",
    "PCA 515",
    "113 244",
    "037 FKO",
    "TCY 180",
    "791 BOX",
    "376 922",
    "XFH 488",
    "217 WJW",
    "3A3 786",
    "G73 0DT",
    "017 OYJ",
    "KCO 301",
    "2Y9 904",
]

subjects = [
    "Rosa Mena",
    "Raquel Segovia",
    "Israel Zedillo",
    "Marcela Solorio",
    "Catalina Cardenas",
    "Bruno Bétancourt",
    "Salma Perales",
    "Débora Serrato",
    "Claudia Griego",
    "Patricia Ruelas",
    "Jesús Lovato",
    "Mauro Estrada",
]

#
# Time to assign

# Dont's
to_authorize = min(len(subjects), len(license_plates))
for application in range(to_authorize):
    print(f"[x] {subjects[application]}, license plate {license_plates[application]}")

# Do's
for subject, plate in zip(subjects, license_plates):
    print(f"[√] {subject}, license plate {plate}")


# /eof
