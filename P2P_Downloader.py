import socket
import json
import time
import logging

content_dictionary = { }
list_of_sources = { }
port = 5001

while 1:
    with open('content_dictionary.json', 'r') as f:
        data = json.load(f)
    content_dictionary = data
    print(content_dictionary)

    file_name = input('Enter file name to download: ')
    chunk_name = file_name + "_" + str(1)
    source_IP = content_dictionary[chunk_name]

    print("Connected...")

    logging.basicConfig(filename='download.log', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.debug(f'File name: {file_name}'  "-"  "IP:" f'{source_IP}')

    for chunk_index in range(1,6):
        chunk_name = file_name + "_" + str(chunk_index)
        requested_chunk = {"filename": " "}
        requested_chunk['filename'] = chunk_name
        print(source_IP)
        requested_chunk_name = json.dumps(requested_chunk)
        download_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        download_socket.connect((source_IP, port))
        download_socket.send(requested_chunk_name.encode())
        print(requested_chunk)
        file = open("filedirectory/" + chunk_name, "ab")  # append mode
        data = download_socket.recv(10000)
        file.write(data)
        file.close()
        download_socket.close()
        time.sleep(3)

    chunknames = ['filedirectory/' + file_name + '_1', 'filedirectory/' + file_name + '_2','filedirectory/' + file_name + '_3'
        ,'filedirectory/' + file_name + '_4','filedirectory/' + file_name + '_5']

    # with open(content_name+'.png', 'w') as outfile:
    with open(file_name, 'ab') as outfile:
        for chunk in chunknames:
            with open(chunk,'rb') as infile:
                outfile.write(infile.read())


