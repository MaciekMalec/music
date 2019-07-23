from music_import_data import import_all_data
artist=import_all_data()[0]
album=import_all_data()[1]
year=import_all_data()[2]
genre=import_all_data()[3]
leng=import_all_data()[4]
def display_albums():
    i=1
    for name in album:
        print(i, ' - ',name)
        i+=1
    alb=input('Chose specific album :')
    return alb


print(album)
ans=0
print(' Music database ')
print(' Currently there are ', len(album), ' albums')
print('--------------------------------------')
print('to display all albums [a];')
print('to display list of artist [s];')
print('to display genres [g];')
ans=input('what do you want to do? ')
# basic user interface, by typing a, s or g, next program is run
# other letter quits the program
print('-------------------------------------')
if ans == 'a':
    x=0
    x=int(display_albums())-1
    print(artist[x],' - ',album[x], ' produced in ',year[x],' that is ', leng[x],' long')