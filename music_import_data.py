def import_all_data(filename = "text_albums_data.txt"):
    with open(filename, 'r') as musicdata:
        artist_name=[]
        album_name=[]
        release_year=[]
        genre=[]
        album_lenght=[]
        record2=[]
        for line in musicdata:
            record = line.strip().split(',')
            artist_name.append(record[0])
            album_name.append(record[1])
            release_year.append(record[2])
            genre.append(record[3])
            album_lenght.append(record[4])
            record2.append(record)
        musictable=[artist_name, album_name, release_year, genre, album_lenght]
        # print(artist_name)
        # print(musictable[1][2])
        return musictable     
# artist=import_all_data[0]
# print(import_all_data())

