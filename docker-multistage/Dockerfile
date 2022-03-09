FROM multi-stage1 as multi-stage1

FROM ubuntu

COPY --from=multi-stage1 /tmpfile/test.txt /data/
