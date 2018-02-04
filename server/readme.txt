just for testing python,
the server is storage photo .

run server:
1. set python env: export PYTHONPATH="../platform/bottle"
2. run #python hello.py

run client:
1. curl http://localhost:8080/upload -F "photofile=@1.txt" 
   提交本地1.txt文件到远端，其中photofile是与里面有关联的
2. curl -G http://localhost:8080/getphoto/new1.txt -o 0.txt -v
   获取远端服务器的一个文件到本地
3. curl -G http://localhost:8080/checkphoto/new1.txt -v
   检查远端服务器的某个文件是否存在

后续可能补齐的能力：
1. 查询以及返回查询消息，改成json ，可以支持查询单个或者一批文件是否存在。
2. 上传文件的时候，携带文件的生成信息，最后修改时间，文件大小等信息。

