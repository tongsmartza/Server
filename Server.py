# Group Network need some Carry
#       58070501006 Karntawan   Udomluksopin
#       58070501046 Peerakit    Boonkittiporn
#       58070501054 Methawat    Thanapairin
#       58070501069 Sirapong    Phoosawan
 
from socket import * 
import sys

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number

addr = ('127.0.0.1', SERV_PORT)          # Socket address
s = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
s.bind(addr)        # Bind socket to address
print ('UDP server started ...')

topicpub = ''   #set data in topicpub is null
topicsub = []   #set data in list of topic sub is null
portpub = ''    #set number portpub is null
portsub = []    #set number list portsub is null
payloadpub = '' #set data from publisher is null
payloadsub = '' #set data from subscriber is null

count = 0   #set variable count is 0

while(1):
    txtin,addr = s.recvfrom(MAX_BUF)  # Received Data
    txtin = txtin.decode('utf-8')   #decode data
    status , topic , payload , commander = txtin.split(",") #Split Data Pattern
    ip , port = addr    #define value in port
    if(status == 'pub'):    #check pattern status from publisher
            topicpub = topic    #define topicpub is topic
            payloadpub = payload    #define payloadpub is data from publisher
            portpub = port  #define port number from Publisher
            print('\n**Publisher Detail : **')
            print('\tPort of Publisher > '+str(portpub))    #print port from publisher
            print('\tPublish-Topic > '+topicpub)    #print topic from publisher
            print('\tMessage from Publisher > '+str(payloadpub)) #print data from publisher

    elif(status == 'sub'):  #check pattern status from subscriber
            topicsub.append(topic)  #define list of topicsub are topic
            payloadsub = payload    #define payloadsub is data from subscriber
            portsub.append(port)    #define list of port are port subscriber
            print('\n**Subscriber Detail : **')
            print('\tPort of Subscriber > '+str(portsub))   #print all port subscriber

            for itemtopic in topicsub: #counting value in topicsub
                print('\tSubscriber-Topic > '+str(itemtopic))   #print all topic subscriber

    if(commander == 'cancel'):  #check command from publisher is cancel
                print('\n---Publisher is Cancel Topic ... ---\n') #show message
                topicpub = ''   #reset topicpub is null
                payloadpub = '' #reset data from publisher is null
                payloadsub = '' #reset data from subscriber is null
       
    for index,item in enumerate(topicsub):  #counting index from topicsub
        if(topicpub == item): #check topic publisher is same topic subscriber
            addrsub = ('127.0.0.1', int(portsub[index])) #define address subscriber
            print('\tMessage send to Subscribe is > '+payloadpub)      #print data for send to subscriber
            s.sendto(payloadpub.encode('utf-8'), addrsub)   #send data to subscriber
            payloadpub = '' #reset data from publisher is null
        
s.close()