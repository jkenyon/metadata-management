__author__ = "bgodfrey"

def main():
    print "Start"
    starttime = time.clock()
    file_count = 0
 
    # Create a list for all the files
    my_list = []
 
    # Loop through all the files (recursive)
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".xml") and not filename.endswith(".aux.xml"):
                metadataFile = os.path.join(root, filename)
                file_count += 1
                my_list.append(metadataFile)
 
    # Create a pool class and run the jobs.
    pool = multiprocessing.Pool()
    result_arrays = pool.map(update_metadata, my_list)
    for item in result_arrays:
        print str(item) + '\n'
 
    # Synchronize the main process with the job processes to ensure proper cleanup.
    pool.close()
    pool.join()
 
    print "Finish"
    stoptime = time.clock()
    ttime = ((stoptime - starttime) / 60)
    print str(ttime) + " minutes to process " + str(file_count) + " files"
 
if __name__ == "__main__":
    main()