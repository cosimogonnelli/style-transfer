#
# # giphy - create gif of all .png's
# # usage: giphy <outfile> <delay> <loops> <png's>
giphy () {
  pngs=$(ls -1 ${@:4} | sort -V)
  convert -delay $2 -loop $3 ${pngs} $1
}

declare -a arr=('64' '128' '256' '512' '1024')

for i in "${arr[@]}"
do
  giphy ${i}/loss_graphs.gif 300 0 ${i}/*/graph.png
  giphy ${i}/mem_graphs.gif 300 0 ${i}/*/mem_graph.png
done
