# Chat-App-SOCKETS


#### Sequence of socket API calls and data flow for TCP:
<img height="500" src="https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg"/>
<br /><br /><br /><p>We’ll create a socket object using socket.socket() and specify the socket type as socket.SOCK_STREAM. When you do that, the default protocol that’s used is the Transmission Control Protocol (TCP). This is a good default and probably what you want.

Why should you use TCP? The Transmission Control Protocol (TCP):

Is reliable: packets dropped in the network are detected and retransmitted by the sender.
Has in-order data delivery: data is read by your application in the order it was written by the sender.
In contrast, User Datagram Protocol (UDP) sockets created with socket.SOCK_DGRAM aren’t reliable, and data read by the receiver can be out-of-order from the sender’s writes.

Why is this important? Networks are a best-effort delivery system. There’s no guarantee that your data will reach its destination or that you’ll receive what’s been sent to you.

Network devices (for example, routers and switches), have finite bandwidth available and their own inherent system limitations. They have CPUs, memory, buses, and interface packet buffers, just like our clients and servers. TCP relieves you from having to worry about packet loss, data arriving out-of-order, and many other things that invariably happen when you’re communicating across a network.</p>
<br /><br /><br /><br /><br /><br /><br /><br />
#### References:
<p>https://realpython.com/python-sockets/
<p>https://youtu.be/i824zN0DGIo</p>
https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170