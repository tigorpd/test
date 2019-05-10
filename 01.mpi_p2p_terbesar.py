# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
ranking = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if ranking == size-1:
    data = ("anda berada dalam rank 0 s.d -1")
    for x in range(0, size):
        comm.send(data, dest=x)
# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    data = comm.recv(source=size-1)
    print(data, "received form ", size-1, "to ", ranking)
