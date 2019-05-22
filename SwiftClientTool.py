import swiftclient
import swiftclient.service
from swiftclient.utils import generate_temp_url

class ConnUtil:
    bucket_name = "user_uploads"
    con = None
    end_point = None

    @staticmethod
    def init_param(user, key, endpoint):
        ConnUtil.con = swiftclient.Connection(
            user=user,
            key=key,
            authurl=endpoint,
        )
        if ConnUtil.bucket_name not in [i['name'] for i in ConnUtil.con.get_account()[1]]:
            ConnUtil.con.put_container(ConnUtil.bucket_name)

    @staticmethod
    def init(c):
        ConnUtil.con = c

    @staticmethod
    def getList():
        return ConnUtil.con.get_container(ConnUtil.bucket_name)[1] if ConnUtil.con is not None else None

    @staticmethod
    def uploadFile(f, filename):
        if filename is None or f is None:
            return False
        return ConnUtil.con.put_object(ConnUtil.bucket_name, filename,
                                       contents=f.read()) if ConnUtil.con is not None else False

    @staticmethod
    def downloadFile(filename):
        if ConnUtil.con is None:
            return False
        with open("temp_file/"+filename, "wb") as f:
            f.write(ConnUtil.con.get_object(ConnUtil.bucket_name, filename)[1])
        return True

    @staticmethod
    def deleteFile(filename):
        if ConnUtil.con is None or filename is None:
            return False
        ConnUtil.con.delete_object(ConnUtil.bucket_name, filename)
        return True

    @staticmethod
    def getTempUrl(filename):
        # f = open("mykey.txt")
        # mykey = f.read()
        ConnUtil.con.post_account(headers={"X-Account-Meta-Temp-Url-Key": "mykey"}) # temp account
        return ConnUtil.end_point+generate_temp_url("/v1/AUTH_test/user_uploads/"+filename,seconds=3600,key="mykey",method='GET')
        f.close()
        
