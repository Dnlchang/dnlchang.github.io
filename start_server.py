from platform import python_version
from subprocess import call
if (int(python_version()[0]) < 3) :
    call(["python", "-m", "SimpleHTTPServer"])
else :
    call(["python", "-m", "http.server", "8000"])
