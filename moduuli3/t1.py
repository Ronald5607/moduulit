kuha = float(input('Kuhasi pituus senttimetreiss√§? '))

if kuha < 37:
    print(f'Laita kuha takaisin veteen, se on {37-kuha}cm liian lyhyt.')
else:
    print('Hieno kuha')