file_data = open('sample_log.txt', 'r')
Lines = file_data.readlines()

count = 0
# Strips the newline character
min_min = 111111
max_max = 0
average = 0
for line in Lines:
    data_stream = line.strip().split(" Old=")
    if len(data_stream) == 1:
        continue
    time = data_stream[0].split(' ')[0]
    old = float(data_stream[1].split('(')[0])
    new = float(data_stream[1].split('(')[1].split("New=")[1].split("(")[0])
    print("Time --->  " , time)
    print("Old Rate --->  " , old)
    print("New Rate --->  " , new)
    print(150*"#")
