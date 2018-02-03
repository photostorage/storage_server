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
