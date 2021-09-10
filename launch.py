import tkinter as tk
import requests
import json
window = tk.Tk()

currentPage = 0

# def toggleText():
#     global toggled
#     try:
#         toggleAble.pack_info()
#         toggled = False 
#         toggleAble.pack_forget()
#     except tk.TclError:
#         toggled = True 
#         toggleAble.pack()

def nextPage() -> None:
    global currentPage

    homeFrame.pack_forget()
    nextPageButton.pack_forget()

    getLevelFrame.pack_forget()
    getProfileFrame.pack_forget()

    if currentPage == 0:
        homeFrame.pack()
    elif currentPage == 1:
        getLevelFrame.pack()
    elif currentPage == 2:
        getProfileFrame.pack()
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
    # print(level.text)

    levelData = json.loads(level.text)
    print(levelData)

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
    basic = tk.Label(master=getLevelFrame, text=f"{levelData['description']}\n{levelData['songName']}")
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
    print(profile.text)

    try:
        clear('user')
    except NameError:
        print(NameError)
        pass 

    username = tk.Label(master=getProfileFrame, text=profileData['username'])
    status = tk.Label(master=getProfileFrame, text=f"{profileData['stars']} Stars\n{profileData['diamonds']} Diamonds\n{profileData['coins']} Coins\n{profileData['userCoins']} User Coins\n{profileData['demons']} Demons\n{profileData['cp']} Creator Points")

    username.pack()
    status.pack()

def clear(type: str) -> None:
    global levelName 
    global basic 
    global further
    global everythingElse
    global toggleEverythingElseButton

    global username
    global status

    if type == 'level':
        levelName.pack_forget()
        basic.pack_forget()
        further.pack_forget()
        everythingElse.pack_forget()
        toggleEverythingElseButton.pack_forget()
    elif type == 'user':
        username.pack_forget()
        status.pack_forget()




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