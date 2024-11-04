def junior_rekrypeli():
    try:
        kokemus = int(input("Syötä kokemuksesi vuosina: "))
        vaadittu_kokemus = kokemus + 1  

        if kokemus < vaadittu_kokemus:
            print("Kokemuksesi ei riitä tähän positioon. Tarvitset lisää kokemusta.")
            
            hanki_lisaa_kokemusta = int(input("Hae töitä ja syötä hankkimasi lisäkokemus vuosina: "))
            vaadittu_kokemus = hanki_lisaa_kokemusta + 1  

            print("Et valitettavasti päässyt hankkimaan kokemusta, koska kaikki rekryt oli seniori positioita :( try harder.")

    except ValueError:
        print("Anna kokemusvuodet numeroina.")

junior_rekrypeli()
