from pacio_fridge import Fridge

def main():
    fridge = Fridge()
    
    while True:
        print("---Violetinis šaldytuvas---")
        print("0: Išeiti")
        print("1: Pridėti produktą į šaldytuvą")
        print("2: Pašalinti produktą iš šaldytuvo")
        print("3: Patikrinti produkto kiekį")
        print("4: Parodyti šaldytuvo turinį")
        print("5: Patikrinti receptą")
        
        choice = input("Pasirinkite: ")

        if choice == "0":
            break
        elif choice == "1":
            product_name = input("Kokį produktą norite pridėti?: ")
            product_quantity = float(input("Kokį kiekį norite pridėti?: "))
            valid_units = ['kg', 'g', 'l', 'ml', 'vnt']
            product_unit = input("Kiek cia to daikto? l ar kg ar vnt ar g ar ml: ")
            if product_unit not in valid_units:
                print("Blogai ivestas matavimo vienetas!")
                return
            fridge.add_product(product_name, product_quantity, product_unit)
            print(f'Sekmingai ideta {product_name} {product_quantity} {product_unit}.')
        elif choice == "3":
            product_name = input("Kokio produkto kiekį norite patikrinti?: ")
            _, product = fridge.check_product(product_name)
            if product:
                print(f"Produkto {product.name} kiekis šaldytuve: {product.quantity}")
            else:
                print("Toks produktas nerastas šaldytuve.")
        elif choice == "2":
            product_name = input("Kokį produktą norite pašalinti?: ")
            product_quantity = float(input("Kokį kiekį norite pašalinti?: "))
            fridge.remove_product(product_name, product_quantity)
            print(f'Sekmingai isimta {product_name} {product_quantity}.')
        elif choice == "4":
            fridge.print_contents()
        elif choice == "5":
            recipe = fridge.create_recipe()
            fridge.check_recipe(recipe)
        else:
            print("Neteisingas pasirinkimas. Įveskite skaičių nuo 0 iki 5.")
main()