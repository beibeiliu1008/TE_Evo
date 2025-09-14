##RUN

##RUN

/group/jrigrp10/tebeiliu/te_evo/relate/relate_v1.2.1_x86_64_static/scripts/RelateParallel/RelateParallel.sh -m 3.3E-8 -N 300000  \
--haps te.snp.combined.chr.$chr.masked.prepared.haps.gz --sample te.snp.combined.chr.$chr.masked.prepared.sample.gz --map ./genetic_m>
--ancestor ./ancestor_genome/$chr.fa --num_iter 20  \
--dist te.snp.combined.chr.$chr.masked.prepared.dist.gz
--output te.snp.combined.chr.$chr.$RANDOM.masked.relate --threads 40 --memory 10


