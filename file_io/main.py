# Programmed By : Moosa Raheel
# Created at : 11 March 2024
# Purpose : For Practice and Mini Project

import json

# File Name 
file = "videos.json"

# Update Helper Function 
def update_helper(new_videos):
    '''This is helper update function which take new videos list and update it and also update from text file'''
    global videos
    videos = new_videos
    try:
        with open(file,'w') as f:
            json.dump(new_videos,f)
    except Exception as err:
        print(err)

#Load videos function
def load_videos():
    '''This Function return a json list from text file if file exist else it will return empty list'''
    global videos
    try:
        with open(file) as data:
            content = json.loads(data.read())
            return content
            
    except FileNotFoundError:
        return []
    
# List Videos Function 
def list_videos():
    message = "  Your Videos List  "
    print(f"\n{message.center(len(message)+16,"*")}\n")
    for index,value in enumerate(videos,start=1):
        print(f"{index}. Title => {value['name']} : Duration => {value['duration']} : Link => {value['link']}")
    else:
        print("\n")
            
# Add video function 
def add_videos(name,duration,link):
    '''This function will add a videos in text file and update a videos list'''
    video_info = {"name":name,"duration":duration,"link":link}
    videos.append(video_info)
    try:
        with open(file,"w") as f:
            json.dump(videos,f)
    except Exception as err:
        print(err)
    finally:
        print("\nVideo add successfully....\n")
        
# Update Video Function 
def update_video():
    '''This function update videos using index and also update from text file'''
    list_videos()
    index = int(input("Enter video Number which you want to update : "))
    if index <= len(videos):
        name  = input("Enter video name : ")
        duration = input("Enter video duration")
        link = input("paste video link : ")
        new_video = {"name":name,"duration":duration,"link":link}
        videos[index-1] = new_video
        update_helper(videos)
        print("\nupdate successfully.........\n")
    else:
        print("Invalid Index\n")
        
# Delete Function 
def delete_video(index):
    '''This function Delete Video from list using index and also delete from text file'''
    if index<=len(videos):
        del videos[index-1]
        update_helper(videos)
    else:
        print("Invalid Index\n")

# Main Function 

def main():
    '''This function is a entry point of application'''
    global videos
    videos = []
    videos = load_videos()
    while True:
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        
        # Variable for choose 
        choice = input("Enter your choice : ")
        
        # Condition Checking
        match choice:
            
            # List Videos Case 
            case '1':
               list_videos()
                    
            # Add Video Case 
            case '2':
                name  = input("Enter video name : ")
                duration = input("Enter video duration")
                link = input("paste video link : ")
                add_videos(name,duration,link)
                
            # Update Video Case 
            case '3':
                update_video()
                
            
            # Delete Video Case 
            case '4':
                list_videos()
                index = int(input("Enter video number : "))
                delete_video(index)
            
            # Exit Program 
            case '5':
                break
            case _:
                print("Invalid Input")

if __name__ == "__main__":
    main()