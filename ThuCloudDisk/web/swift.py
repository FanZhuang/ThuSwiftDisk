from swiftclient import client
import os
import magic
class Swift:
    def __init__(self,host,tenant,user_name,user_pass,port= '5000'):
        self.host = host
        self.user_name = user_name
        self.user_pass = user_pass
        self.port = port
        self.authurl ='http://'+ self.host+':'+self.port+'/v2.0'
        self.tenant = tenant
        self.temp_path = '/~/temppath'

    def connect(self):
        auth = client.get_auth(self.authurl,self.user_name,self.user_pass,tenant_name=self.tenant,auth_version='2')
        self.storage_url = auth[0]
        self.http_conn = client.http_connection(self.storage_url)
        self.token = auth[1]

    def list_container(self,container_name,prefix=None,delimiter=None):
        try:
            return client.get_container(self.storage_url,self.token,container_name,prefix=prefix,delimiter=delimiter,http_conn=self.http_conn)
        except:
            return None
    def put_container(self,container_name):
        if(self.list_container(container_name) == None):
            client.put_container(self.storage_url,self.token,container_name,http_conn=self.http_conn)
            return True
        return False

    def get_object(self,container,object):
        try:
            return client.get_object(self.storage_url,self.token,container,object,http_conn = self.http_conn)
        except:
            return None

    def get_object_to_file(self,container,name):
	filepath = '/home/admin/ThuSwiftDisk/ThuCloudDisk/static/download/'
        filepath += name
	GetBufferSize = 1024*1024*10
	try:
	    res = client.get_object(self.storage_url,self.token,container,name)
            fileSize = res[0]['content-length']
            fileDate = res[0]['last-modified']
            filename = name
	    data = res[1]
            f = file(filepath, 'wb')
	    f.write(data)
            f.close()
	    return fileSize, fileDate, filepath, name
	except:
	    return False
 	
    def put_object_from_file(self,container,prefix,filepath):
        try:
            content_length = os.path.getsize(filepath);
            content_type = magic.from_file(filepath,mime=True);
	    strlist = filepath.split('/')
	    for value in strlist:
		object = value
	    print object
            fp = open(filepath,'rb')
            client.put_object(self.storage_url,self.token,container,object,fp,content_length=content_length,content_type=content_type)
            return True
        except:
            return False
    
    def delete_object(self, container, name):
        try:
    	    print client.delete_object(self.storage_url, self.token, container, name)
	    return True
        except:
            return False 

#def get_new_file_path(container,object):
#swift = Swift('swift.strawberrycode.com','demo','admin','secrete','5000')
#swift.connect();
#print swift.list_container('xiaohe-container');
#print swift.put_container('ThuCloudDisk-container');
#swift.put_object_from_file('ThuCloudDisk-container',prefix='',filepath='/home/chengls10/Desktop/2')
#print swift.get_object_to_file('ThuCloudDisk-container','1.py')
#print swift.delete_object('ThuCloudDisk-container','1.py')