import tkinter as tk
import requests
import json

print("Hello world")
print('GDUI 1.0 by sudocode1 and community')
print('API by GDColon (GDBrowser)')
print('License: AGPL-3.0')

window = tk.Tk()

currentPage = 0

def nextPage() -> None:
    global currentPage

    homeFrame.pack_forget()
    nextPageButton.pack_forget()

    getLevelFrame.pack_forget()
    getProfileFrame.pack_forget()
    searchFrame.pack_forget()
    songVerifyFrame.pack_forget()

    if currentPage == 0:
        homeFrame.pack()
    elif currentPage == 1:
        getLevelFrame.pack()
    elif currentPage == 2:
        getProfileFrame.pack()
    elif currentPage == 3:
        searchFrame.pack()
    elif currentPage == 4:
        songVerifyFrame.pack()
    else:
        currentPage = 0
        homeFrame.pack()

    nextPageButton.pack()
    currentPage = currentPage + 1

def getLevel() -> None:
    global levelName
    global basic
    global further
    global everythingElse
    global toggleEverythingElseButton

    level = requests.get(f"https://gdbrowser.com/api/level/{enterId.get()}")
    # # printlevel.text)

    levelData = json.loads(level.text)
    # printlevelData)

    featured = 'Not Featured'

    if levelData['featured'] == True:
        featured = 'Featured'

    if levelData['epic'] == True:
        featured = 'Epic'

    try:
        clear('level')
    except NameError:
        pass 

    levelName = tk.Label(master=getLevelFrame, text=f"{levelData['name']} ({levelData['id']})\n{levelData['author']}")
    basic = tk.Label(master=getLevelFrame, text=f"{levelData['description']}\n{levelData['songName']} ({levelData['songID']})")
    further = tk.Label(master=getLevelFrame, text=f"{levelData['stars']} Stars\n{levelData['difficulty']}\n{featured}\n{levelData['length']}\nMade in {levelData['gameVersion']}")
    everythingElse = tk.Label(master=getLevelFrame, text=f"{levelData['downloads']} Downloads\n{levelData['likes']} Likes\nDisliked/Negative: {levelData['disliked']}\nStars Requested: {levelData['starsRequested']}")

    levelName.pack()
    basic.pack()
    further.pack()

    def toggleEverythingElse() -> None:
        try:
            everythingElse.pack_info()
            everythingElse.pack_forget()
        except tk.TclError:
            everythingElse.pack()


    toggleEverythingElseButton = tk.Button(
        master=getLevelFrame,
        text="Toggle Everything Else",
        command = toggleEverythingElse
    )

    toggleEverythingElseButton.pack()

def getProfile() -> None:
    global username 
    global status

    profile = requests.get(f"https://gdbrowser.com/api/profile/{enterUsername.get()}")
    profileData = json.loads(profile.text)
    # print(profile.text)

    try:
        clear('user')
    except NameError:
        print(NameError) 

    username = tk.Label(master=getProfileFrame, text=profileData['username'])
    status = tk.Label(master=getProfileFrame, text=f"{profileData['stars']} Stars\n{profileData['diamonds']} Diamonds\n{profileData['coins']} Coins\n{profileData['userCoins']} User Coins\n{profileData['demons']} Demons\n{profileData['cp']} Creator Points")

    username.pack()
    status.pack()

def searchLevel() -> None:
    global level1
    global level2
    global level3
    global level4
    global level5 

    search = requests.get(f"https://gdbrowser.com/api/search/{enterSearch.get()}")
    searchData = json.loads(search.text)
    # print(searchData[0])

    try:
        clear('search')
    except NameError:
        print(NameError)

    level1 = tk.Label(master=searchFrame, text=f"{searchData[0]['name']} ({searchData[0]['id']})\n{searchData[0]['author']}\n{searchData[0]['description']}\n{searchData[0]['difficulty']}\n{searchData[0]['songName']}\n")
    level2 = tk.Label(master=searchFrame, text=f"{searchData[1]['name']} ({searchData[1]['id']})\n{searchData[1]['author']}\n{searchData[1]['description']}\n{searchData[1]['difficulty']}\n{searchData[1]['songName']}\n")
    level3 = tk.Label(master=searchFrame, text=f"{searchData[2]['name']} ({searchData[2]['id']})\n{searchData[1]['author']}\n{searchData[2]['description']}\n{searchData[2]['difficulty']}\n{searchData[2]['songName']}\n")
    level4 = tk.Label(master=searchFrame, text=f"{searchData[3]['name']} ({searchData[3]['id']})\n{searchData[3]['author']}\n{searchData[3]['description']}\n{searchData[3]['difficulty']}\n{searchData[3]['songName']}\n")
    level5 = tk.Label(master=searchFrame, text=f"{searchData[3]['name']} ({searchData[3]['id']})\n{searchData[3]['author']}\n{searchData[3]['description']}\n{searchData[3]['difficulty']}\n{searchData[3]['songName']}\n")

    level1.pack()
    level2.pack()
    level3.pack()
    level4.pack()
    level5.pack()

def checkSong():
    global isAvailable

    try:
        clear('songVerify')
    except NameError:
        print(NameError)

    # print(f"https://gdbrowser.com/api/song/{enterSongId.get()}")
    checkSongRequest = requests.get(f"https://gdbrowser.com/api/song/{enterSongId.get()}")
    checkSongRequestData = json.loads(checkSongRequest.text)

    # print(checkSongRequestData)

    available = ""

    if checkSongRequestData == -1:
        available = "Song doesn't exist."
    elif checkSongRequestData == True:
        available = "Song is allowed for use."
    elif checkSongRequestData == False:
        available = "Song is not allowed for use."

    isAvailable = tk.Label(master=songVerifyFrame, text=f"{available}")
    isAvailable.pack()

def clear(type: str) -> None:
    global levelName 
    global basic 
    global further
    global everythingElse
    global toggleEverythingElseButton

    global username
    global status

    global level1
    global level2
    global level3
    global level4
    global level5

    global isAvailable

    if type == 'level':
        levelName.pack_forget()
        basic.pack_forget()
        further.pack_forget()
        everythingElse.pack_forget()
        toggleEverythingElseButton.pack_forget()
    elif type == 'user':
        username.pack_forget()
        status.pack_forget()
    elif type == 'search':
        level1.pack_forget()
        level2.pack_forget()
        level3.pack_forget()
        level4.pack_forget()
        level5.pack_forget()
    elif type == "songVerify":
        isAvailable.pack_forget()
        




## home frame
homeFrame = tk.Frame()
tk.Label(
    master=homeFrame,
    text="Welcome to GDUI! A super simple tool for fetching and viewing data from Geometry Dash.\nCredit to GDColon for making the API utilisted by this program."
).pack()

## level frame
getLevelFrame = tk.Frame()
tk.Label(master=getLevelFrame, text="Get Level (ID)").pack()
enterId = tk.Entry(master=getLevelFrame, width=50)
requestLevel = tk.Button(master=getLevelFrame, text="Request", command=getLevel)
enterId.pack()
requestLevel.pack()

## profile frame
getProfileFrame = tk.Frame()
tk.Label(master=getProfileFrame, text="Get Profile (Username)").pack()
enterUsername = tk.Entry(master=getProfileFrame, width=50)
requestProfile = tk.Button(master=getProfileFrame, text="Request", command=getProfile)

enterUsername.pack()
requestProfile.pack()

## search frame
searchFrame = tk.Frame()
tk.Label(master=searchFrame, text="Search Levels").pack()
tk.Label(master=searchFrame, text="This feature is in beta! Filters are being worked on.").pack()
enterSearch = tk.Entry(master=searchFrame, width=50)
searchButton = tk.Button(master=searchFrame, text="Search", command=searchLevel)

enterSearch.pack()
searchButton.pack()

## song verification frame
songVerifyFrame = tk.Frame()
tk.Label(master=songVerifyFrame, text="Check if Song is available").pack()
tk.Label(master=songVerifyFrame, text="Enter New Grounds Song ID").pack()
enterSongId = tk.Entry(master=songVerifyFrame, width=50)
checkSongButton = tk.Button(master=songVerifyFrame, text="Check", command=checkSong)

enterSongId.pack()
checkSongButton.pack()

## base
tk.Label(
    text="GDUI",
    width=50,
    height=2
).pack()
nextPageButton = tk.Button(
    text="Next Page",
    width=25,
    height=1,
    command = nextPage
)
nextPageButton.pack()

nextPage()
window.mainloop()
