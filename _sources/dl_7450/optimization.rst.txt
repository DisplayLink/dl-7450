.. _dl_7450_optimization:

Optimization for Micropython
============================

Splashscreen's set_background method does accept `bytes` and `bytearray`. 
However, when passing slices of objects such as bytearray instances, Python creates 
a copy which involves allocation of the size proportional to the size of slice. 
This can be alleviated using a `memoryview` object. The memoryview itself is 
allocated on the heap, but is a small, fixed-size object, regardless of the
size of slice it points too. Slicing a memoryview creates a new memoryview, 
so this cannot be done in an interrupt service routine. 

For example::

    import vision_client
    from splashscreen import Splashscreen

    visionClient = vision_client.VisionClient()
    screen = Splashscreen()

    def cb(message): 
        messageType = message[0]   # a copy is passed
        message = message[1:] 

        mv = memoryview(message)   # small object is allocated
        messageType = mv[0]
        message = mv[1:]           # a pointer to memory is passed

