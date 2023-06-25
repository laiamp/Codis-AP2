from yogi import tokens

def paraules():
    '''escriu les diferents paraules del text llegit ordenades alfabèticament'''
    paraules: set[str] = {s.lower() for s in tokens(str)} # afegim la paraula en minúscules
    
    for paraula in sorted(paraules): 
        print(paraula)


def main():
    paraules()


if __name__ == "__main__":
    main()