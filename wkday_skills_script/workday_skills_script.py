import pyautogui as auto
import time
import os
def initial_set_up():
    print("Type in your skills! Set up once and never worry about it again!")
    print("Type \"Done\" or \"done\" to end the list")
    with open("workday_skills_list.txt", "w") as file:
        skill = input()
        while(skill.lower() != "done"):
            file.write(skill+"\n")
            skill = input()
    print("Set up complete, now you can run the script!")

def script_start(delay:int, txt_file:str, interval:int)->int:
    time.sleep(delay)

    with open (txt_file,"r") as skills_list:
        for line in skills_list:
            auto.type_write(line, interval=interval)

    return 1

if __name__ == "__main__":
    print("Type in the delay before the script starts: ", sep="")
    delay = input()
    if os.path.getsize("workday_skills_list.txt")==0:
        print("Skills list empty.")
        print("Starting set up...")
        initial_set_up()
    print("Script starting...")
    script_start(delay,"workday_skills_list.txt",0.1)
    print("Script Done")
    
