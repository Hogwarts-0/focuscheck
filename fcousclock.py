import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus timer started for {minutes} minutes.")
    time.sleep(seconds)
    print("Focus timer ended!")

if __name__ == "__main__":
    minutes = int(input("Enter focus duration (in minutes): "))
    focus_timer(minutes)
