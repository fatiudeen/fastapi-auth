import subprocess                                                               
                                                                                   
def start():                                                                   
    cmd =['uvicorn', 'src.main:app', '--reload']                                                                 
    subprocess.run(cmd)  