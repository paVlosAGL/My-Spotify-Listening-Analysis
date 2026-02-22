import json
import datetime
import sys
import matplotlib.pyplot as plt

#Results of the overall project.
def main():
    data=function_1()
    new_data=cleaning(data)
    fav_tr,times_listen_tr,total_minutes_tr,fav_ar,times_listen_ar,overall_time=function_2(new_data)
    most_active_day,most_minutes=function_3(new_data)
    print(f"""================================ Spotify Data Analysis =============================================
Total time listening to music: {overall_time:.2f} minutes
Favourite Track: {fav_tr}
Times Streamed: {times_listen_tr}
Minutes listening to it: {total_minutes_tr:.2f}
Favourite Artist: {fav_ar}
Streamed Favoutite Artist: {times_listen_ar} times
Most Active Date: {most_active_day} with Total Minutes: {most_minutes:.2f}
====================================================================================================""")


#convertion json file into python object list of dictionaries.
def function_1():
    with open("data_history.json") as file:
      data=json.load(file)
      return data

#New dictionary with data which i will use.
def cleaning(data):
    cleaned=[]
    for dictionary in data:
        clean={
            "date":dictionary.get("ts"),
            "minutes":dictionary.get("ms_played")/60000,
            "track":dictionary.get("master_metadata_track_name"),
            "artist":dictionary.get("master_metadata_album_artist_name")
        }
        cleaned.append(clean)

    return cleaned


#favourite artist + track θελω να εμφανισω και τα top 5 tracks +times listen
def function_2(new_data):
    tracks={}
    artists={}
    overall_time=0
    for i in new_data:
        track_id=i["track"]
        minutes=i["minutes"]
        artist=i["artist"]

        if track_id in tracks:
            tracks[track_id]["times_played"]+=1
            tracks[track_id]["total_minutes"]+=minutes
        else:
            tracks[track_id]={"times_played":1,"total_minutes":minutes}

        #total time spent listening to music
        overall_time+=minutes

        if artist in artists:
            artists[artist]["total"]+=1
        else:
            artists[artist]={"total":1}

    sort_list_tr=sorted(tracks,key=lambda track_id:tracks[track_id]["times_played"],reverse=True)
    sort_list_ar=sorted(artists,key=lambda artist:artists[artist]["total"],reverse=True)

    #stats for tracks
    fav_tr=sort_list_tr[0]
    times_listen_tr=tracks[fav_tr]["times_played"]
    total_minutes_tr=tracks[fav_tr]["total_minutes"]

    x=0
    print(f"""================Top Tracks================""")
    for top in range(5):
       x+=1
       if top==None:
           sys.exit("Couldn't find your top 5 tracks :(")
       else:
           print(f"{x}){sort_list_tr[top]}")

    #stats for artists
    fav_ar=sort_list_ar[0]
    times_listen_ar=artists[fav_ar]["total"]
    return fav_tr,times_listen_tr,total_minutes_tr,fav_ar,times_listen_ar,overall_time

#Most active hours
def function_3(new_data):
    my_dates={}
    for data in new_data:
        minutes=data["minutes"]
        ISO_date=datetime.datetime.strptime(data["date"],"%Y-%m-%dT%H:%M:%SZ")
        date=ISO_date.date()

        if date in my_dates:
            my_dates[date]+=minutes
        else:
            my_dates[date]=minutes

    music_surge=max(my_dates,key=my_dates.get)
    max_minutes=my_dates[music_surge]

    #thelw na kaleseis to function_4 sto opoio tha dvseis my_dates
    #kai na kanei ena histogram gia thn exelixi mesa sthn xronia
    function_4(my_dates)
    return music_surge,max_minutes

#Diagram through pandas library
def function_4(my_dates):
    x=[]
    y=[]
    for key,value in my_dates.items():
        x.append(key)
        y.append(value)

    plt.plot(x,y)
    plt.title("Minutes Per Date")
    plt.xlabel("Dates")
    plt.ylabel("Minutes")
    plt.show()


if __name__=="__main__":
    main()
