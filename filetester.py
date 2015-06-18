import sys
import os.path
import os
import subprocess

def main():

    if len(sys.argv) ==2:
        folderpath = sys.argv[1]
        try:
            os.chdir(folderpath)
        except:
            print("folder doesn't exist, try running again")
            exit()

    txtfiles = [f for f in os.listdir() if f.endswith(".txt")]         
   
    for f in txtfiles:
        javacmd = "java -Xss64m MergeSort "+ f + " -1"
        try:    
            response = subprocess.Popen(javacmd, stdout=subprocess.PIPE,shell = True)
            response = response.stdout.read().decode("utf-8")
            
            
            if "is sorted."  in response:
                print("Output correctly sorted for file: " + f)
            else:

                print("Output did not return a sorted list for file: " + f)

        except:
            print('error')





main()    
