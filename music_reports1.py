def import_all_data(filename = "/home/maciek/codecool/music/text_albums_data.txt"):
    with open(filename, 'r') as musicdata:
        artist_name=[]
        album_name=[]
        release_year=[]
        genre=[]
        album_lenght=[]
        record2=[]
        for line in musicdata:
            record = line.split(',')
            record[-1]=record[-1].strip()
            artist_name.append(record[0])
            album_name.append(record[1])
            release_year.append(record[2])
            genre.append(record[3])
            album_lenght.append(record[4])
            record2.append(record)
        musictable=[artist_name, album_name, release_year, genre, album_lenght]
        # print(artist_name)
        # print(musictable[1][2])
        return musictable,record2   # I get 2 matrices: 1st is 5xY the other Yx5, Y is number of records


def display_albums(albums,categ):
    if not albums:
        print('empty list')
    else:
        lista=[]
        amount=[]
        amount.append(0)
        for name in albums:
            if name[categ] not in lista:
                lista.append(name[categ])
                amount.append(1)
            else:
                for i,item in enumerate(lista,1):
                    if item == name[categ]:
                        amount[i]+=1 
        for i,name in enumerate(lista,1):
            print(i,' - ',name,' - ',amount[i]) 


        


def add_to_list(playlist,z):
    x=int(z)-1
    record=[artist[x],album[x],genre[x],year[x],leng[x]]
    if record in playlist:
        print('That position is already in your playlist.')
    else:
        print(artist[x],' - ',album[x],' from ',year[x],' which is ', genre[x], ' that is ' ,leng[x],' long')
        y=input('Add this position to your current list? (y/n): ')
        if y=='y':
            playlist.append([artist[x],album[x],genre[x],year[x],leng[x]])
    return playlist

def remove_from_playlist(playlist,z):
    temp_playlist=[]
    i=1
    if str.isdigit(z):
        for item in playlist:
            if i!=int(z):
                temp_playlist.append(item)
            i+=1
        playlist=temp_playlist
    elif z=='c':
        playlist=[]
    return playlist

def shortest_album(leng):
    shortst=99999999999999
    i=0 
    for time in leng:
        dur=int(time.split(':')[0])*60+int(time.split(':')[1])
        if shortst>dur:
            shortst=dur
            z=i
        elif shortst==dur:
            z.append(i)
        i+=1
    return z,leng[z]
        
def longest_album(leng):
    shortst=0
    i=0 
    for time in leng:
        dur=int(time.split(':')[0])*60+int(time.split(':')[1])
        if shortst<dur:
            shortst=dur
            z=i
        elif shortst==dur:
            z.append(i)
        i+=1
    return z,leng[z]


    

def main_menu(user_playlist):
    print('-------------------------------------------------')
    print('-----------------Main menu-----------------------')
    print('to display all albums by album names [a];')
    print('to display list of artist [s];')
    print('to display genres [g];')
    print('your list contains ',len(user_playlist),' positions. to see the list [l]')
    print('to exit [x]')
    ans=input('what do you want to do? ')
    # basic user interface, by typing a, s or g, next program is run
    # other letter quits the program
    print('-------------------------------------------------')

    if ans == 'a':
        alb=0
        while alb != 'b':
            display_albums(album)
            alb=input('Chose specific number of the album or [b] to return to main menu:')
            if str.isdigit(alb):
                add_to_list(user_playlist,alb)
    if ans == 's':
        alb=0
        while alb !='b':
            display_albums(artist)
            alb=input('Chose specific number of the album or [b] to return to main menu:')
            if str.isdigit(alb):
                add_to_list(user_playlist,alb)    
    if ans == 'g':
        alb=0
        while alb !='b':
            display_other(genre)
            

    if ans == 'l':
        alb=0
        while alb != 'b':
            print('Your current playlist is:')
            display_albums(user_playlist)
            alb=input('choose number to remove from the list, [c] to clear list or [b] to main menu:')
            user_playlist=remove_from_playlist(user_playlist,alb)
    
    return ans, user_playlist

# Global variables
artist=import_all_data()[0][0]
album=import_all_data()[0][1]
year=import_all_data()[0][2]
genre=import_all_data()[0][3]
leng=import_all_data()[0][4]
user_playlist=import_all_data()[1]
an=0


print(' Music database ')
print(' Currently there are ', len(album), ' albums in the database')
print(' Shortest album is number ', shortest_album(leng)[0],' and its length is ', shortest_album(leng)[1])
print(' Longest album is number', longest_album(leng)[0],' and its length is ', longest_album(leng)[1])
while an !='x':
    an,user_playlist=main_menu(user_playlist)
    print('Your playlist is:')
    display_albums(user_playlist)
if user_playlist:
    y=input('Would you like to export that playlist to "Playlist.txt" [y/n]? ')
    if y=='y':
        print('Exporting playlist.')
        # export the playlist
    else:
        print('Have a nice day.')
else:
    an=input('Your playlist is empty. type [x] to quit or go back to main menu.')



# t=import_all_data()[0]
# u=user_playlist
# record2=import_all_data()[1]
# print(t,record2)
