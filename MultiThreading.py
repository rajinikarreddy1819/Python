
from threading import Thread
from time import sleep, time


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("HELLO....", i+1)
            sleep(0.3)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("HI.....",  i+1)
if __name__ == '__main__':
    t1 = Hello()
    t2 = Hi()
    t1.start()
    t2.start()
sleep(5)
print("====================== Function Approach ===========================")    

def download(file_name):
    print("Downloading File.........", file_name)
    sleep(0.5)
    print("Download Complete")

if __name__ == '__main__':
    file= ["video.mp4", "Image.png", "data.csv"]
    start = time()
    for f in file:
        download(f)
    end = time()
    print(f"serial time {end - start:.2f} seconds") 

    threads = []
    for f in file:
        t = Thread(target= download, args=(f,)) 
        threads.append(t)
    start = time()    
    for t in threads:
        t.start() 
    for t in threads:
        t.join()  

    end = time()  
    print(f"parallel time {end - start:.2f} seconds")         
        



