import sqlite3

con = sqlite3.connect('video_manager.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY,"
            "name TEXT NOT NULL,"
            "time TEXT NOT NULL)")


def load_data():
    pass


def list_videos():
    cur.execute('''
SELECT * FROM videos''')
    print("*"*50)
    rows = cur.fetchall()
    if not rows:
        print('No videos found')
    else:
        for row in rows:
            print(f'{row[0]}. {row[1]} -- Duration-{row[2]}')
    print("*"*50)


def add_video():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    cur.execute('''
                INSERT INTO videos (name, time) VALUES (?, ?)''', (name, time))
    con.commit()


def update_video():
    id = int(input("Enter video no.: "))
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",
                (name, time, id))
    con.commit()


def delete_video():
    id = int(input("Enter video no.: "))
    cur.execute("DELETE FROM videos where id = ?", (id,))
    con.commit()


def main():

    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print('1. List all yt videos')
        print('2. Add a yt video')
        print('3. Update a yt video details')
        print('4. Delete a yt video')
        print('5. Exit the app')

        choice = int(
            input("Enter number from 1 to 5 based on above choices: "))

        match choice:
            case 1: list_videos()
            case 2: add_video()
            case 3: update_video()
            case 4: delete_video()
            case 5: break
            case _: print("Invalid choice!")

    con.close()


if __name__ == "__main__":
    main()
