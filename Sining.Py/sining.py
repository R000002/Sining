import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Pinsala'y ikinamada", 0.08),
        ("Oh binibining may salamangka", 0.07),
        ("You've turned my limbics into a bouquet", 0.06),
        ("", 0.06),
        ("Ikaw ay tila sining sa museong 'di naluluma", 0.09),
        ("Binibini kong ginto hanggang kaluluwa", 0.1),
        ("Gonna keep you like the nu couché", 0.10),
        ("All my life.......", 0.2),
        ("", 0.0),
        ("At kung sa tingin mo na ang oras mo'y lumipas na", 0.09),
        ("Ako'y patuloy na mararahuyo sa ganda", 0.10),
        ("I'd still kiss you every single day", 0.09),
        ("All my life.......", 0.3),
        

    ]
    delays = [0.1, 2.0, 4.0, 7.0, 7.0, 11.5, 13.0, 14.5, 22.0, 23.0, 25.0, 29.0, 31.5]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()