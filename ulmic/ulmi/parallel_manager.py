from ulmic.environment import UlmicEnvironment
import numpy as np

class ParallelManager:

    def __init__(self,medium):
        self.medium = medium

        self.n_threads = UlmicEnvironment.get_threads()
        ## try:
        ##     from mpi4py import MPI
        ##     self.comm = MPI.COMM_WORLD
        ##     self.rank = self.comm.Get_rank()
        ##     self.size = self.comm.Get_size()
        ##     self.n_processors = self.size
        ## except:
        ##     print('WARNING: MPI not detected!')
        ##     self.comm = 1
        ##     self.rank = 1
        ##     self.size = 1
        ##     self.n_processors = 1
        self.comm = 1
        self.rank = 1
        self.size = 1
        self.n_processors = 1

    def get_eval_k_mesh(self):
        return self.medium.nk_eval
        # nk_eval_range = np.arange(self.medium.nk_eval)
        # return nk_eval_range
