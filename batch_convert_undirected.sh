file[1]="livejournal"
file[2]="baidu"
file[3]="flickr-growth"
file[4]="zhishi-hudong-relatedpages"
file[5]="pokec"
file[6]="wikipedia_link_en"
file[7]="wikipedia_en"
file[8]="dbpedia"
file[9]="facebook"
file[10]="twitter_www"
file[11]="wiki_talk_en"
file[12]="wiki_communication"
file[13]="random"
file[14]="RMAT"
file[15]="twitter_mpi"
file[16]="friendster"
#file[17]="citeseer"
#file[18]="scale25"

deal () {
    echo python directed_edge_list_to_undirected.py /mnt/raid0_huge/yuede/data/${file[$1]}/edge_list.txt /mnt/raid0_huge/yuede/data/${file[$1]}/edge_list_undirected.txt

    python directed_edge_list_to_undirected.py /mnt/raid0_huge/yuede/data/${file[$1]}/edge_list.txt /mnt/raid0_huge/yuede/data/${file[$1]}/edge_list_undirected.txt
    
#    python edge_list_to_GTgraph.py /mnt/raid0_huge/yuede/data/${file[$1]}/edge_list.txt /mnt/raid0_huge/yuede/data/${file[$1]}/gtgraph.txt

}
for index in `seq 7 16`;
do
    deal $index
done


