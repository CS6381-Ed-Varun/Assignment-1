
import zmq

def main():

    context = zmq.Context()

    # pub side 
    frontend = context.socket(zmq.XPUB)
    frontend.bind("tcp://127.0.0.1:5559")
        
    #sub side
    backend = context.socket(zmq.XSUB)
    backend.bind("tcp://127.0.0.1:5560")

    zmq.device(zmq.FORWARDER, frontend, backend)

if __name__ == "__main__":
    main()