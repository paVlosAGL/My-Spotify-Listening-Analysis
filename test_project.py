from project import cleaning,function_2,function_3
import datetime

def test_cleaning():
    dictionary=[
        {"ts": "2025-01-01T14:46:58Z",
         "ms_played": 120000,
         "master_metadata_track_name": "She Likes",
         "master_metadata_album_artist_name": "Dyzen"
        }
    ]

    new = cleaning(dictionary)

    assert new[0]["date"] == "2025-01-01T14:46:58Z"
    assert new[0]["minutes"] == 2
    assert new[0]["track"] == "She Likes"
    assert new[0]["artist"] == "Dyzen"

def test_function_2():
    dictionaries = [
        {"track":"Track_1","artist":"artist_1","minutes":15},
        {"track":"Track_7","artist":"artist_7","minutes":5},
        {"track":"Track_1","artist":"artist_1","minutes":13},
        {"track":"Track_5","artist":"artist_5","minutes":4}
    ]

    fav_tr,times_listen_tr,total_minutes_tr,fav_ar,times_listen_ar,top5=function_2(dictionaries)

    assert fav_tr == "Track_1"
    assert times_listen_tr == 2
    assert total_minutes_tr == 28
    assert fav_ar == "artist_1"
    assert times_listen_ar == 2
    assert top5[0] == "Track_1"

def test_function_3():
    last_dictionaries=[
        {"date":"2025-10-20T18:00:08Z","minutes":81},
        {"date":"2025-10-22T21:56:37Z","minutes":8},
        {"date":"2025-10-22T21:58:06Z","minutes":23}
    ]

    date,minutes=function_3(last_dictionaries)

    assert date.isoformat() == "2025-10-22"
    assert minutes == 31

