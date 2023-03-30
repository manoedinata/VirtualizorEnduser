from requests import Session
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

class Api(object):
    def __init__(self, server_URL: str, api_key: str, api_password: str) -> None:
        # Base URL
        self.BASE_URL = server_URL

        # Setup session
        self.session = Session()
        self.session.verify = False
        disable_warnings(InsecureRequestWarning)

        # Base params
        # API & authentication params preparation
        self.baseParams = {
            "api": "json",
            "apikey": api_key,
            "apipass": api_password,
            "do": 1
        }


    def request(self, method: str, paramsDict: dict, dataDict: dict):
        """
        Make a request to API
        Specifically for automatic parameters handle.

        :param method: Request method
        :param paramsDict: Required parameters, in dictionary
        """
        params = self.baseParams
        params.update(paramsDict)

        req = self.session.request(method=method, url=self.BASE_URL, params=params, data=dataDict)
        return req.json()


    # Functions: List VM
    def listVM(self):
        """
        List VMs in an account.
        """
        req = self.request("GET", {
            "act": "listvs"
        })
        
        return req

    # Functions: VM info
    def VMInfo(self, vps_id):
        """
        Get specific VM information.
        """
        req = self.request("GET", {
            "act": "vpsmanage",
            "svs": int(vps_id)
        })
        
        return req

    # Functions: Start VM
    def StartVM(self, vps_id):
        """
        Start a specific VM.
        """
        req = self.request("GET", {
            "act": "start",
            "svs": int(vps_id),
        })
        
        return req

    # Functions: Stop VM
    def stopVM(self, vps_id):
        """
        Stop a specific VM.
        """
        req = self.request("GET", {
            "act": "stop",
            "svs": int(vps_id),
        })
        
        return req

    # Functions: List OS
    def listOS(self, vps_id):
        """
        List available OSes for a specific VM.
        """
        req = self.request("GET", {
            "act": "ostemplate",
            "svs": int(vps_id),
        })

        return req["oslist"]["vzo"]

    # Functions: Restart VM
    def restartVM(self, vps_id):
        """
        Restart a specific VM.
        """
        req = self.request("GET", {
            "act": "restart",
            "svs": int(vps_id),
        })
        
        return req


    # Functions: List VDF
    def listVDF(self, vps_id):
        """
        List VDFs for a specific VM.
        """
        req = self.request("GET", {
            "act": "managevdf",
            "svs": int(vps_id),
        })
        
        return req

    # Functions: Add VDF
    def addVDF(self, vps_id, protocol, src_port, src_hostname, dest_ip, dest_port):
        """
        Add a VDF for a specific VM.
        """
        req = self.request("POST", paramsDict={
            "act": "managevdf",
        }, dataDict={
            "svs": int(vps_id),
            "vdf_action": "addvdf",
            "protocol": protocol,
            "src_port": src_port,
            "src_hostname": src_hostname,
            "dest_ip": dest_ip,
            "dest_port": dest_port,
        })
        
        return req
