import socket
import cv2
import pickle
import struct
import imutils


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name= socket.gethostname()
host_ip = "192.168.1.20"
port = 5050
print("Sunucu {0}:{1} adresine kuruldu".format(host_ip,port))
socket_adress = (host_ip,port)

server_socket.bind(socket_adress)

server_socket.listen(5)

#603DEB1015CA71BE2B73AEF0857D77811F352C073B6108D72D9810A30914DFF4
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
writer=cv2.VideoWriter("output.avi",fourcc,30,(640,480))

while True:
    client_socket, addr = server_socket.accept()
    print("baglanti kuruldu",addr)
    
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while (vid.isOpened()):
            
            

            
                
            #DataFromServer= client_socket.recv(1024).decode()
            #print(DataFromServer)
            
            img, frame = vid.read(0)
            writer.write(frame)
            frame = imutils.resize(frame, width = 320)
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            cv2.imshow("Server Frame", frame)
            key = cv2.waitKey(25) & 0xFF
            if key == ord("q"):
                client_socket.close()
writer.relase()
vid.release()
cv2.destroyAllWindows()