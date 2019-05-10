# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
    data = "Anda melakukan broadcast"
# jika saya bukan rank 0 maka saya menerima pesan
else:
    data = None
data = comm.bcast(data, root= 0)
print(data, "received from", 0, "to", rank)
