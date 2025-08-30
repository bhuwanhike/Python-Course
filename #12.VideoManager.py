import json


def load_data():
    try:

        with open('yt.txt', 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('yt.txt', 'w') as file:
        json.dump(videos, file)


def list_videos(videos):
    print("\n")
    print("*"*50)
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']} -- Duration: {video['time']}')
    print("*"*50)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):

    videoQuery = int(
        input("Enter the video number which you want to update: "))
    list_videos(videos)

    choice = input(
        "Press 1 for updating time or press 2 for updating video name: ")

    if choice == '1':
        new_time = input("Enter new time: ")
        for index, video in enumerate(videos, start=1):
            if videoQuery == index:
                print("saving video")
                video['time'] = new_time
                save_data_helper(videos)
                break

    if choice == '2':
        new_name = input("Enter new name: ")
        for index, video in enumerate(videos, start=1):
            if videoQuery == index:
                video['name'] = new_name
                save_data_helper(videos)
                break


def delete_video(videos):
    choice = int(input('Enter the video no. you want to delete: '))
    del videos[choice-1]
    save_data_helper(videos)


def main():

    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print('1. List all yt videos')
        print('2. Add a yt video')
        print('3. Update a yt video details')
        print('4. Delete a yt video')
        print('5. Exit the app')

        userInput = int(
            input("Enter number from 1 to 5 based on above choices: "))

        match userInput:
            case 1: list_videos(videos)
            case 2: add_video(videos)
            case 3: update_video(videos)
            case 4: delete_video(videos)
            case 5: break
            case _: print("Invalid choice!")


if __name__ == '__main__':
    main()
