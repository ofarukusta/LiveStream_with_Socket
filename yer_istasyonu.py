from distutils.log import error
import socket
import cv2
import pickle
import struct

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = "169.254.54.38"
port = 5050
client_socket.connect((host_ip,port))
data = b""
payload_size = struct.calcsize("Q")

while True:
    
    datas= "client gönderildi".encode()
    client_socket.send(datas)

    try:
        while len(data) < payload_size:
            packet = client_socket.recv(4*1024) #4k için
            if not packet: break
            data += packet

        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(1024*4)

        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)

        b = cv2.resize(frame,(640,480),fx=0,fy=0, interpolation= cv2.INTER_CUBIC)
        cv2.imshow("Client Frame", b)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
 
    except struct.error as e:
        print(e)

client_socket.close()
