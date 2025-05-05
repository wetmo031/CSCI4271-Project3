import subprocess

# number of requests to send
attacks = 1000

# url to send requests to
url = "http://localhost:8888/999999/add/full/bookmark123/http%3A%2F%2Fexample.com/example/5"

# send the requests
for i in range(attacks):
    subprocess.run(["curl", "-v", url])

# uncomment the following code to run infinitely
# while True:
