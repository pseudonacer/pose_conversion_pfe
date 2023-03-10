from datetime import time, timedelta
from yt_dlp import YoutubeDL

def download_video(url, filename):
    """ Video Downloader """
    ydl_opts = {
        "no_warnings": True,
        "quiet" : 1,
        'logtostderr' : True,
        "noprogress": False,
        "outtmpl" : filename
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

def draw_skeleton(ax, ar,  pose, default_skeleton, color):
    """ Skeleton drawing util
        @param :
            ax : matplotlib axis 
            ar : artists array, useful when using matplotlib.animation.ArtistAnimation
            pose : pose joints coordinates, numpy.ndarray(shape = (52,3))
            default_skeleton : skeleton links, between each joint
            color : plot color 
        ---------
        @return :
            ax : maptlotlib axis 
            ar : updated artists list
    """
    data = pose.reshape(52,3)
    # Plot joints using scatter
    x_, y_, z_ = data.T
    artist = ax.scatter(x_, z_, y_,  s = 10, color = color) # invert drawing axis (x, z, y) instead of (x, y, z)
    ar.append(artist)
    # Plot links using plot
    for origin, end in default_skeleton :
        x, y , z   = data[origin]
        xx, yy, zz = data[end]
        line, = ax.plot([x, xx],[z, zz],[y,yy], color = color,  linewidth = 2)
        ar.append(line)
    return ax, ar

def subset(df, column, key) :
    """ Select a subset that verifies a condition """
    return df[df[column] == key]



def get_time(isoformat):
    """ Creates a time object from the ISOformat 
        @param  : str ISOformat (hh:mm:ss.sss)
        ---------
        @return : time object
    """
    try :
        # split the microseconds with the rest
        s, microsecond = isoformat.split(".")
    except :
        # if failed then microseconds are not included and it equal to 0
        s = isoformat
        microsecond = 0
    # clip to max if greater than 999999
    microsecond = min( int(microsecond) , time.max.microsecond)
    hour, minute , second =  list(map(int, s.split(":")))
    return time(hour, minute, second, microsecond).isoformat()

def deltatime(isoformat):
    """ Converts to timedelta object from the ISOformat (used for `start_time` and `end_time`)
        @param  : str ISOformat (hh:mm:ss.sss)
        ---------
        @return : timedelta object
    """
    try :
        s, microsecond = isoformat.split(".")
    except :
        s = isoformat
        microsecond = 0
    microsecond = min( int(microsecond) , timedelta.max.microseconds)
    hour, minute , second =  list(map(int, s.split(":")))
    return timedelta(minutes = minute, seconds = second, microseconds = microsecond)


def speakers() :
    """ src     : https://github.com/chahuja/pats/blob/master/data/common.py
        ---------
        @return : List of all present speakers in the dataset
    """
    return [ "almaram", "angelica", "chemistry", "conan", "ellen", "jon", "oliver", "rock", "seth", "shelly", "maher", "huckabee", "fallon", "lec_cosmic", 
             "colbert", "corden", "lec_evol", "minhaj", "bee", "lec_law", "ytch_dating", "lec_hist", "ytch_charisma", "ytch_prof", "ferguson", "noah" ]



def parent() :
    """ src     : https://github.com/chahuja/pats/blob/master/data/skeleton.py
        ---------
        @return : List of the parent's index for each joint index 
                    - parent of index 9 --> joint 7
    """
    return [-1,
            0, 1, 2,
            0, 4, 5,
            0, 7, 7,
            6,
            10, 11, 12, 13,
            10, 15, 16, 17,
            10, 19, 20, 21,
            10, 23, 24, 25,
            10, 27, 28, 29,
            3,
            31, 32, 33, 34,
            31, 36, 37, 38,
            31, 40, 41, 42,
            31, 44, 45, 46,
            31, 48, 49, 50]



def skeleton_connections():
    """ Create skeleton by connecting each joint to its parent.
        ---------
        @return : List of interjoint connections 
                    [ (joint1, joint2), (joint3, joint4) ... ]
    """
    return [ (joint, _parent) for joint, _parent in enumerate(parent())][1:]
