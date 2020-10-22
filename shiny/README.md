# image-shiny

```
sudo docker run --rm -p 1900:3838 \
    -v /home/zanyuan/apps/:/srv/shiny-server/ \
    -v /home/zanyuan/logs/:/var/log/shiny-server/ \
    registry.cn-beijing.aliyuncs.com/seqyuan/shiny:v0.1 
```

/home/zanyuan/apps/ 里放apps

浏览器地址栏载入: `docker服务所在IP:1900`即可访问

