import os
import time
import socket

nodeID = os.environ.get('SLURM_NODEID', "BAD NODE")
procID = os.environ.get('SLURM_PROCID', "BAD PROC")
arrayID = os.environ.get('SLURM_ARRAY_TASK_ID', "BAD ARRAY")

if __name__ == "__main__":
    print( "=== Host Runtime ===" )
    print( f"Running on {socket.gethostname()}" )

    print( "=== Slurm Specific Environment ===" )
    print( f"SLURM_NODEID = {nodeID}" )
    print( f"SLURM_PROCID = {procID}" )
    print( f"SLURM_ARRAY_TASK_ID = {arrayID}" )

    time.sleep( 3 )

    print( "=== End of Task ===" )

