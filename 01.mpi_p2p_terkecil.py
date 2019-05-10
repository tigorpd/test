# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
ranking = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if ranking == 0:
    data = ("Anda termasuk dalam kategori Rank 0 S.D size")
    for x in range(1, size):
        comm.send(data, dest= x)

# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    data = comm.recv(source=0)
    print(data, "from process %d to %d"%(0, ranking))

