from traceback import print_tb
import requests
import multiprocessing
import os

def downloadFile(url, name):
    print(f"downloading start {name}")
    response = requests.get(url)
    with open(f"files/file{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Download ending {name}")

def main():
    url = "https://picsum.photos/200/300"
    
    # Create the 'files' directory if it doesn't exist
    if not os.path.exists('files'):
        os.makedirs('files')

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        processes.append(p)
        p.start()
    
    # Wait for all processes to finish
    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
