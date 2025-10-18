print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("TO FAMILIARIZE DIFFERENT FORMATS OF DISPLAYING DATE AND TIME USING THE DATE TIME MODULE")#Title
print()
from datetime import datetime as dt
print("Current Date and Time is:",dt.now())
print("[YYYY-MM-DD HH:MM:SS]:", dt.strftime('%Y-%m-%d','%h:%M:%S'))
