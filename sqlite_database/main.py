import os
import sqlite3

# Database connection code 
def deb_connection():
    '''This function will create connection with database and create a table name videos'''
    if not os.path.exists("data"):
        os.mkdir("data")
    try:
        global cursor,connection
        connection = sqlite3.connect("data/videos.db")
        cursor = connection.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS videos (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR NOT NULL,
                        time VARCHAR NOT NULL,
                        link VARCHAR NOT NULL
                    )
                    ''')
        
    # Handle the error 
    except Exception as err:
        print("Some error occured. see connection_error.log file for more information")
        if not os.path.exists("log"):
            os.mkdir("log")
        with open("log/connection_error.log","w") as f:
            f.write(str(err))
        exit()

# List videos function 
def list_videos():
    '''This Fuction will list all videos'''
    data = cursor.execute("SELECT * FROM videos")
    for index,i in enumerate(data,start=1):
        print(f"{index}. id => {i[0]}, title => {i[1]}, duration => {i[2]}, link => {i[3]}")
    else:
        print("\n")

    
# Add video function 
def add_videos(title,duration,link):
    '''This function will add video in database'''
    try:
        cursor.execute("INSERT INTO videos (name, time, link) VALUES (?, ?, ?)",(title,duration,link))
        connection.commit()
        print("\nvideo add successfull........\n")
    # Handle error 
    
    except Exception as err:
        print("some error occured. see insert_error.log file for more information")
        if not os.path.exists("log"):
            os.mkdir("log")
        with open("log/insert_error.log","w") as f:
            f.write(str(err))
        exit()
        
# Update video function
def update_video(vid_id,title,duration,link):
    '''This function will update video using id'''
    try:
        cursor.execute('''
                       UPDATE videos SET name = ?, time = ?, link = ? WHERE id = ?
                       ''',(title,duration,link,vid_id))
        connection.commit()
        print("\nupdate video successfully.....\n")
        
    # Handle error 
    except Exception as err:
        print("some error occured. see update_error.log file for more information")
        if not os.path.exists("log"):
            os.mkdir("log")
        with open("log/update_error.log","w") as f:
            f.write(str(err))
        exit()
            
# Delete Function 
def delete_video(vid_id):
    '''This video will delete video using id'''
    try:
        cursor.execute("DELETE FROM videos WHERE id = ?",(vid_id,))
        connection.commit()
        print("\ndelete video successfully.....\n")
        
    # Handle error 
    except Exception as err:
        print("some error occured. see delete_error.log file for more information")
        if not os.path.exists("log"):
            os.mkdir("log")
        with open("log/delete_error.log","w") as f:
            f.write(str(err))
        exit()
        

# Main function of application 
def main():
    '''This is entry point of application'''
    welcome = " welcome to videos manager "
    print(welcome.center((len(welcome)+16),"*"))
    deb_connection()
    while True:
        print("1. List videos : ")
        print("2. Add video : ")
        print("3. Update video : ")
        print("4. Delete video : ")
        print("5. Exit : ")
        choice = input("Enter your choice : ")
        match choice:
            case "1":
                print(f"\n{"*"*50}\n")
                print("\t\tList of all videos")
                print(f"\n{"*"*50}\n")
                list_videos()
                
            case "2":
                title = input("Enter a video title : ")
                duration = input("Enter a video duration : ")
                link = input("Enter a video link : ")
                add_videos(title,duration,link)

            case "3":
                list_videos()
                vid_id = input("Enter id of video which you want to update : ")
                title = input("Enter new title : ")
                duration = input("Enter duration : ")
                link = input("Enter link : ")
                update_video(vid_id,title,duration,link)
                
            case "4":
                list_videos()
                vid_id = input("Enter video id : ")
                delete_video(vid_id)
        
            case "5":
                connection.close()
                break
            
            case _:
                print("Invalid input")

if __name__ == "__main__":
    main()