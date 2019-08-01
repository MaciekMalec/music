def print_single_album(album):
        print(' | '.join(album))

def print_multiple_albums(albums):
        for album in albums:
                print(' | '.join(album))

def print_specific_type(albums,type):
        if type==0:
                text='Author'
        elif type==1:
                text='Album name'
        elif type==2:
                text='Year'
        elif type==3:
                text='genre'
        i=0
        amount=[]
        amount.append(0)
        lista=[]
        for album in albums:
                if  album[type] not in lista:
                        lista.append(album[type])
                        i+=1
                        amount.append(1)
                else:
                        j=1
                        for item in lista:
                                if album[type]==item:
                                        amount[j]+=1
                        else:
                                j+=1
        i=1
        for item in lista:
                print(i, ' - ', item, ' - ', amount[i], ' albums.')
                i+=1
        ans=input('Which ',text, '?')
        if str.isdigit(ans):
                ans=lista[int(ans)-1]
        return ans

def print_start_menu(albums):
        print("Music database")
        print("Currently, there are ", len(albums))
        print("* - display all albums")
        print("g - display albums by genre")
        print("t - display albums from giving time range")
        print("s - display shortest album")
        print("l - display longest album")
        print("a - display albums by artist")
        print("n - display albums by name")
        print("- - delete an album")
        print("+ - add an album")
        print("e - save album to external file")
        print("q - exit program")

def print_add_playlist():
        print("Would you like to add this track to playlist?")

