#!/usr/bin/env python

import requests
import threading
import time
import os

os.system('clear')

BLUE = '\33[94m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\33[93m'
LIGHTCYAN = '\033[96m'
BOLD = '\033[1m'
END = '\033[0m'


def banner():
    print(GREEN+"""  
  dP""b8 Yb  dP 88""Yb 888888 88""Yb
 dP   `"  YbdP  88__dP 88__   88__dP 
 Yb        8P   88""Yb 88""   88"Yb 
  YboodP  dP    88oodP 888888 88  Yb"""+END)
    print(GREEN+""" 
888888  dP"Yb  88""Yb 888888 88b 88 .dP"Y8 88  dP""b8 .dP"Y8 
88__   dP   Yb 88__dP 88__   88Yb88 `Ybo." 88 dP   `" `Ybo." 
88""   Yb   dP 88"Yb  88""   88 Y88 o.`Y8b 88 Yb      o.`Y8b 
88      YbodP  88  Yb 888888 88  Y8 8bodP' 88  YboodP 8bodP' """+END)
    print(BOLD+BLUE+"\t\t\tCheckusr v1.0"+RED +" Coded by: iSHFRh"+END)
    print(BLUE+"""
                .-`                     
              .++oo:                    
          :-.:o+++oo+/::.               
          -+oyhyo+++ooo+o`              
           oyosyhhyo++++/               
          /y+::/syyhhys:                
          o+:---hMmhsso/.               
        `+++o+/--/oo `.-.               
       -++oooo+o+/-.   `..              
     .++++o++oso`     -`  ..            
    :oo+++os++++//::/--....`            
   /ossssossso/+oo/::`                  
  -o+++++oooo/   `                      
  /o+o++++ooss-                         
  `..ssss+/ssss                         
    /ssso``sss+                         
   -hys+`  sddhy+`       `       ``.`   
   /mNNMm/./sssss/-.-+++//: ..:+oo::-   
          `..          ``.`        `            
    """ + END)
banner()
username = input(GREEN+"\033[1m["+BLUE+"\033[1m?"+END+"\033[1m"+GREEN+"]" "\033[1m USERNAME: "+END)

instagram = (f'https://www.instagram.com/{username}')
facebook = (f'https://www.facebook.com/{username}')
twitter = (f'https://www.twitter.com/{username}')
youtube = (f'https://www.youtube.com/{username}')
twitch = (f'https://www.twitch.tv/{username}')
github = (f'https://www.github.com/{username}')
reddit = (f'https://www.reddit.com/user/{username}')
tumblr = (f'https://{username}.tumblr.com')
wordpress = (f'https://{username}.wordpress.com')
blogger = (f'https://www.blogger.com/profile/{username}')
basecamp = (f'https://{username}.basecamphq.com/login')
wikipedia = (f'https://www.wikipedia.org/wiki/User:{username}')
pinterest = (f'https://soundcloud.com/{username}')
flickr = (f'https://www.flickr.com/people/{username}')
bandcamp = (f'https://www.bandcamp.com/{username}')
hackernews = (f'https://news.ycombinator.com/user?id={username}')
soundcloud = (f'https://www.flickr.com/people/{username}')
vimeo = (f'https://vimeo.com/{username}')
ebay = (f'https://www.ebay.com/usr/{username}')
aboutme = (f'https://about.me/{username}')
spotify = (f'https://open.spotify.com/user/{username}')
blipfm = (f'https://blip.fm/{username}')
trip = (f'https://www.trip.skyscanner.com/user/{username}')
flipboard = (f'https://flipboard.com/@{username}')
steam = (f'https://steamcommunity.com/id/{username}')
medium = (f'https://medium.com/@{username}')
fiveHundredPx = (f'https://500px.com/{username}')
behance = (f'https://www.behance.net/{username}')
ello = (f'https://ello.co/{username}')
okcupid = (f'https://www.okcupid.com/profile/{username}')
disqus = (f'https://disqus.com/by/{username}')
dailymotion = (f'https://www.dailymotion.com/{username}')
ifttt = (f'https://www.ifttt.com/p/{username}')
creativeMarket = (f'https://creativmarket.com/{username}')
slack = (f'https://{username}.slack.com')
codementor = (f'https://www.codementor.io/{username}')
tracky = (f'https://tracky.com/user/~{username}')
deviantart = (f'https://deviantart.com/{username}')
vk = (f'https://vk.com/{username}')
livejournal = (f'https://{username}.livejournal.com')
canva = (f'https://www.canva.com/{username}')
foursquare = (f'https://foursquare.com/{username}')
colourlovers = (f'https://www.colourlovers.com/love/{username}')
imgur = (f'https://imgur.com/user/{username}')
scribd = (f'https://www.scribd.com/{username}')
slideshare = (f'https://slideshare.net/{username}')
keybase = (f'https://keybase.io/{username}')
reverbNation = (f'https://www.reverbnation.com/{username}')
etsy = (f'https://www.etsy.com/shop/{username}')
mixcloud = (f'https://www.mixcloud.com/{username}')
fotolog = (f'https://fotolog.com/{username}')
designspiration = (f'https://www.designspiration.net/{username}')
patreon = (f'https://patreon.com/{username}')
cashme = (f'https://cash.me/{username}')
bitbucket = (f'https://bitbucket.org/{username}')
pastebin = (f'https://pastebin.com/u/{username}')
gumroad = (f'https://www.gumroad.com/{username}')
dribbble = (f'https://dribbble.com/{username}')
buzzfeed = (f'https://buzzfeed.com/{username}')
goodreads = (f'https://www.goodreads.com/{username}')
angellist = (f'https://angel.co/{username}')
houzz = (f'https://houzz.com/user/{username}')
gravatar = (f'https://en.gravatar.com/{username}')
contently = (f'https://{username}.contently.com')
kongregate = (f'https://kongregate.com/accounts/{username}')
roblox = (f'https://www.roblox.com/user.aspx?username={username}')
lastFm = (f'https://last.fm/user/{username}')
hubpages = (f'https://{username}.hubpages.com')
codecademy = (f'https://www.codecademy.com/{username}')
newsground = (f'https://{username}.newgrounds.com')
trakt = (f'https://www.trakt.tv/users/{username}')
wattpad = (f'https://www.wattpad.com/user/{username}')
tripadvisor = (f'https://tripadvisor.com/members/{username}')

websites = [
instagram, facebook, twitter, youtube, twitch, github, reddit, tumblr,
wordpress, blogger, basecamp, wikipedia, pinterest, flickr, bandcamp, hackernews, soundcloud, vimeo, ebay, aboutme,
spotify, blipfm, trip, flipboard, steam, medium, fiveHundredPx, behance, ello, okcupid, disqus, dailymotion, ifttt,
creativeMarket, slack, codementor, tracky, deviantart, vk, livejournal, canva, foursquare, colourlovers, imgur, scribd,
slideshare, keybase, reverbNation, etsy, mixcloud, fotolog, designspiration, patreon, cashme, bitbucket,
pastebin, gumroad, dribbble, buzzfeed, goodreads, angellist, houzz, gravatar, contently, kongregate,
roblox, lastFm, hubpages, codecademy, newsground, trakt, wattpad, tripadvisor
]

def search():
    try:
        print(GREEN+"\033[1m["+BLUE+"\033[1m*"+END+"\033[1m"+GREEN+"]" "\033[1m Checking username "+END+f"{BOLD+username}" +GREEN+" :"+END)
        time.sleep(0.5)
        for url in websites:
            r = requests.get(url)

            if r.status_code == 200:
                print(BOLD+"["+BOLD+GREEN+"+"+END+"\033[1m]"+END+BOLD+YELLOW,f"Found: {END+url}")
                with open(f'{username}.txt', 'a') as found:
                    found.write(url + '\n')
            elif r.status_code == 404:
                print(BOLD+"["+BOLD+RED+"-"+END+"\033[1m]"+BOLD+YELLOW,f"Not Found: {END+url}")

    except Exception as e:
        print(f'ERROR: {e}')
    except KeyboardInterrupt:
        print(BOLD+" ["+BOLD+RED+"!"+END+"\033[1m]"+BOLD,"Exiting the program...."+END)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh)
    except requests.exceptions.ProxyError as errp:
        print("Proxy Error")
        print(errp)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting")
        print(errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error")
        print(errt)
    except requests.exceptions.RequestException as err:
        print("Unknown Error")
        print(err)

        threads = []
        for i in range(100):
            thread1 = threading.Thread(target=search)
            thread1.start()
            threads.append(thread1)
        for thread2 in threads:
            thread2.join()

if __name__ == '__main__':
    search()