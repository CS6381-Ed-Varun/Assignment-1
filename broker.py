
import zmq

def main():

    context = zmq.Context(1)

    # pub side (change to XSUB when adding more subscribers)
    frontend = context.socket(zmq.SUB)
    frontend.bind("tcp://*:5559")
        
    frontend.setsockopt_string(zmq.SUBSCRIBE, "")
        
    #sub side (change to XPUB when adding more publishers)
    backend = context.socket(zmq.PUB)
    backend.bind("tcp://*:5560")

    zmq.device(zmq.FORWARDER, frontend, backend)

if __name__ == "__main__":
    main()