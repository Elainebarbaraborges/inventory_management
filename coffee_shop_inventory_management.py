def pnt_itm_dtls(it, it_stk, it_prc):
    it_ttl_vl = it_stk * it_prc
    print(f"{it}: {it_stk} units x £{it_prc:.2f} = £{it_ttl_vl:.2f}")


def c_ttl_stk_vl(stk, prc):
    ttl_stk_vl = 0
    for it, it_stk in stk.items():
        if it in prc:
            it_prc = prc[it]
            ttl_stk_vl += it_stk * it_prc
        else:
            print(f"Error: Price information missing for item {it}")
    return ttl_stk_vl


def ck_stk_prc(stk, prc):
    for it, it_stk in stk.items():
        if it not in prc:
            print(f"Error: Price information missing for item {it}")


def main():
    mn = ["Latte",
          "Mate Tea",
          "Cappuccino",
          "Americano",
          "White Americano",
          "Espresso",
          "Hot Chocolate",
          "Chai Latte",
          "Mocha",
          "Macchiato",
          "Breakfast Tea",
          "Green Tea",
          "Peppermint Tea"]
   
    stk = {"Latte": 200,
           "Mate Tea": 317,
           "Cappuccino": 130,
           "Americano": 318,
           "White Americano": 214,
           "Espresso": 123,
           "Hot Chocolate": 230,
           "Chai Latte": 190,
           "Mocha": 228,
           "Macchiato": 141,
           "Breakfast Tea": 120,
           "Green Tea": 78,
           "Peppermint Tea": 93}

    prc = {"Latte": 10.20,
           "Mate Tea": 16.20,
           "Cappuccino": 10.20,
           "Americano": 9.80,
           "White Americano": 9.80,
           "Espresso": 8.80,
           "Hot Chocolate": 10.20,
           "Chai Latte": 9.80,
           "Mocha": 7.60,
           "Macchiato": 8.80,
           "Breakfast Tea": 8.20,
           "Green Tea": 8.20,
           "Peppermint Tea": 8.20}

    mn.sort()

    for it in mn:
        if it in stk:
            it_stk = stk[it]
            if it in prc:
                it_prc = prc[it]
                pnt_itm_dtls(it, it_stk, it_prc)
            else:
                print(f"Error: Price information missing for item {it}")
        else:
            print(f"Error: Stock information missing for item {it}")
   
    ttl_stk_vl = c_ttl_stk_vl(stk, prc)
    print(f"\nTotal Stock Value: £{ttl_stk_vl:.2f}")
   
    ck_stk_prc(stk, prc)

if __name__ == "__main__":
    main()