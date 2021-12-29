#! /bin/bash
pre='s3://dev-et-data/out/DelawareRiverBasin/Run10_07_2020'
#cmd='aws s3 ls --human --sum --recur'
cmd='aws s3 rm --recur'
for i in `cat mess` ; do $cmd $pre/$i ; done
