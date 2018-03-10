from socket import * 
import sys

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number

addr = ('127.0.0.1', SERV_PORT)          # Socket address
s = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
s.bind(addr)        # Bind socket to address
print ('UDP server started ...')

topicpub = ''
topicsub = []
portpub = ''
portsub = []
payloadpub = ''
payloadsub = ''
buf = ''


#txtin,addr = s.recvfrom(MAX_BUF)  # txtin stores receive text
#port = txtin.decode('utf-8')
#print(int(port))
#addrsub = ('127.0.0.1', int(port))

while(1):
    txtin,addr = s.recvfrom(MAX_BUF)  # txtin stores receive text
    txtin = txtin.decode('utf-8')
    status , topic , payload , commander = txtin.split(",")
    print(status + topic + payload + commander)
    ip , port = addr
    print(port)
    if(status == 'pub'):
            topicpub = topic
            payloadpub = payload
            portpub = port
            print('Publisher Topic : '+topicpub+' > '+payloadpub+' '+commander)
            addrpub = ('127.0.0.1', int(portpub))

    elif(status == 'sub'):
            print('hee')
            topicsub.append(topic)
            payloadsub = payload
            portsub.append(port)
            #print('Subscriber Topic is : '+topicsub+'\n\n')
            #addrsub = ('127.0.0.1', int(portsub))
            print('kuy')
            for item in topicsub:
                print('\t\tThis is a jubujubu'+item+' ')
            
            

    if(commander == 'cancel'):
                topicpub = ''
                topicsub = ''
                portpub = ''
                portsub = ''
                payloadpub = 'cancel'
                payloadsub = ''
                buf = ''
                print(payloadpub)
       

    if(topicpub == topicsub):
   
        print('portsend  '+str(portsub))
        s.sendto(payloadpub.encode('utf-8'), addrsub)

    print('Port Publisher > '+str(portpub))
    print('Port Subscriber > '+str(portsub))
        


s.close()