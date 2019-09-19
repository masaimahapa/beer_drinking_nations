import alcohol_reader

def main():
    print('Alcohol Program')
    print()
    #initialize our reader in the alcohol_reader program
    alcohol_reader.init()

    #top 10 beer drinkers nations
    countries = alcohol_reader.top_beer_drinkers()
    print(countries)
    for idx, d in enumerate(countries[:10]):
        print('{}. {} {} '.format(idx+1 , d.country, d.beer_servings))

    #10 lowest beer drinking nations
    print('10 lowest drinking nattions')
    countries= alcohol_reader.lowest_beer_drinkers()
    for idx, d in enumerate(countries[:10]):
        print('{}. {} {}'.format(idx+1, d.country, d.beer_servings))


if __name__ == "__main__":
    main()