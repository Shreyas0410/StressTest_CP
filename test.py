#Testing the code
import os
import sys
import shutil

run = {
    "c": "gcc {0} && a.exe < {1} > {2}",
    "cpp": "g++ -std=c++11 {0} && a.exe < {1} > {2}",
    "java": "javac {0} && java {3} < {1} > {2}",
    "py": "python {0} < {1} > {2}"
}

m = {}
try:
    for i in range(1, len(sys.argv), 2):
        m[sys.argv[i]] = sys.argv[i+1]
except IndexError:
    print("Error: Missing arguments. Usage: python test.py -g <generator> -c <correct> -w <wrong> [-t <testcases>]")
    sys.exit(1)

def runCode(fileType, input, output):
    file = m[fileType]
    filename, language = file.split(".")
    cmd = run[language].format(file, input, output, filename)
    result = os.system(cmd)
    if result != 0:
        print(f"Error: Command failed - {cmd}")
        sys.exit(1)

def getData(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    with open(filename, "r") as file:
        data = [line.rstrip() for line in file if len(line.rstrip()) > 0]
    return data

# Execution starts here
with open("dummy", "w") as f:
    pass

testcase = int(m["-t"]) if "-t" in m else 1
t = 0

while t < testcase:
    runCode("-g", "dummy", "input")  # Run generator code
    runCode("-c", "input", "correct")  # Run correct code
    runCode("-w", "input", "wrong")  # Run wrong code
    if getData("correct") != getData("wrong"):
        shutil.copy("input", f"input{t}")
        os.remove("input")
        shutil.copy("correct", f"correct{t}")
        os.remove("correct")
        shutil.copy("wrong", f"wrong{t}")
        os.remove("wrong")
        t += 1
        print(f"{t} testcase found!")
os.remove("dummy")
