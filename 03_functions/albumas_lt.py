""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""
#Album collection editor

album_info = {
    'Artist': 'Rammstein',
    'Album': 'Made In Germany 1995-2011',
}

def print_full_album(album_dict):
    print('\t>>>> All Albums <<<<\n')
    for key, album_info in album_dict.items():
        print(f"{key:02d} - {album_info['Artist']} - {album_info['Album']}")

def add_album(album_dict, new_album_info):
    album_dict[len(album_dict) + 1] = new_album_info
    print(f'{new_album_info["Artist"]} - {new_album_info["Album"]} was added to your Albums List')


def main(album_dict):
    while True:
        print("\t>>>> Albums collection <<<<")
        print("\t     0: Exit")
        print("\t     1: Full Albums List")
        print("\t     2: Add/Remove Albums")
        print("\t     3: Modify tracks in Album")

        choice = input("Choice: ")
        if choice == "0":
            break
        elif choice == "1":
            print_full_album(album_dict)
        elif choice == "2":
            choice = input("You want to add or remove album? (+/-)")
            if choice == "+":
                artist = input("Enter artist: ")
                album = input("Enter album: ")
                new_album_info = {'Artist': artist, 'Album': album}
                add_album(album_dict, new_album_info)
            elif choice == "-":
                # Implement remove logic if needed
                pass
            else:
                print("Wrong input please retry!")
                pass
        elif choice == "3":
            # Add logic for modifying tracks in the album
            pass
        else:
            print("Wrong! Please choose from 0-3 options only!")
            pass

main({})

add_album(album_info)