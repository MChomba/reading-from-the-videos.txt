
def main():
    #open the video_file for reading
    video_file=open("video.txt","r")
    #accumulator to zero
    total=0
    #counter to zero
    count=0
    #use for loop to read file
    print("these are the running times for each video")
    for line in video.txt:
        #convert line into float
        running_time=float(line)
        count+=1
        #display time
        print("video #",count,":",running_time,sep="")
        #add time to total
        total+=running_time
    #close the file
    video_file.close()
    #display total running time
    print("the total running time is",total,"seconds")
main()
