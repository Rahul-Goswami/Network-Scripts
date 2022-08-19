"""
class VPCCheckNetwork:
    # List of parameters obtained from check network from server team
    serverName = ""
    bond = ""
    ip = ""
    interfaceSpeed = ""


    # Method to get check network parameters for a server

    # Arguments:
    # Row of excel file currently in the iteration in main function

    # Returns: None

    def get_check_network(self, row):
        # Instantiate the parameters with values from excel sheet
        self.serverName = row[0]
        self.ip = row[2]
        self.bond = row[1]
        self.interfaceSpeed = row[3]
        print(f"\nObtained check network for {self.serverName}")


class NetworkPreChecks:
    # List of parameters obtained from check network from server team
    ip = ""
    switchName = ""
    interfaceNumber = ""
    tenant = ""
    epg = ""


    # Method to get network pre-checks parameters for a server

    # Arguments:
    # Row of excel file currently in the iteration in main function

    # Returns: None

    def get_network_pre_checks(self, row):
        # Instantiate the parameters with values from excel sheet
        self.ip = row[4]
        self.switchName = row[5]
        self.interfaceNumber = row[6]
        self.tenant = row[7]
        self.epg = row[8]

        print(f"\nObtained network prechecks")


class NetworkWorkPlan:
    # List of parameters obtained from check network from server team
    switchName = ""
    interfaceNumber = ""
    tenant = ""
    epg = ""
    network = ""
    interfaceSpeed = ""
    vpcState = ""
    trunkMode = ""


    # Method to get network work plan parameters for a server

    # Arguments:
    # Row of excel file currently in the iteration in main function


    # Returns: None

    def get_network_work_plan(self, row):
        # Instantiate the parameters with values from excel sheet
        self.switchName = row[9]
        self.interfaceNumber = row[10]
        self.tenant = row[11]
        self.epg = row[12]
        self.network = row[13]
        self.interfaceSpeed = row[14]
        self.vpcState = row[15]
        self.trunkMode = row[16]

        print(f"\nObtained network work plan")


class NetworkBackoutPlan:
    # List of parameters obtained from check network from server team
    switchName = ""
    interfaceNumber = ""
    tenant = ""
    epg = ""
    network = ""
    interfaceSpeed = ""
    vpcState = ""
    trunkMode = ""


    # Method to get network work plan parameters for a server

    # Arguments:
    # Row of excel file currently in the iteration in main function

    # Returns: None

    def get_network_backout_plan(self, row):
        # Instantiate the parameters with values from excel sheet
        self.switchName = row[17]
        self.interfaceNumber = row[18]
        self.tenant = row[19]
        self.epg = row[20]
        self.network = row[21]
        self.interfaceSpeed = row[22]
        self.vpcState = row[23]
        self.trunkMode = row[24]

        print(f"\nObtained network rollback plan")

"""
word = ['text1', 'text2', ' ']
new_list = [text for text in word if text]
print(new_list)