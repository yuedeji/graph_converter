file[1]="livejournal"
file[2]="baidu"
#file[3]="flickr-growth"
#file[4]="zhishi-hudong-relatedpages"
file[3]="pokec"
file[4]="wikipedia_link_en"
file[5]="wikipedia_en"
#file[6]="dbpedia"
file[6]="facebook"
file[7]="twitter_www"
#file[11]="wiki_talk_en"
#file[12]="wiki_communication"
file[8]="random"
file[9]="RMAT"
file[10]="twitter_mpi"
file[11]="friendster"
#file[16]="us_patent"
#file[17]="citeseer"
#file[18]="scale25"

#file[1]="wiki_talk_en"
#file[2]="wiki_communication"
#file[3]="friendster"

deal () {
    echo python edge_list_to_GTgraph.py /mnt/raid0_huge/yuede/data/${file[$1]}/edge_list.txt /mnt/raid0_huge/yuede/data/${file[$1]}/gtgraph.txt

    python edge_list_to_GTgraph.py /mnt/raid0_huge/yuede/data/${file[$1]}/edge_list.txt /mnt/raid0_huge/yuede/data/${file[$1]}/gtgraph.txt

}
for index in `seq 1 11`;
do
    deal $index
done


