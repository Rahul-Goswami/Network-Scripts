from NetworkDevice import NetworkDevice
from authentication import get_credentials
from readCSV import readcsvfile


class NexusTest:
    def __init__(self, hostname, username, password):
        """
        Constructor method to instantiate device object with active SSH session
        """
        print(f"\nConnecting to {hostname}")
        self.device = NetworkDevice("cisco_nxos", hostname, username, password)

    def disconnect_device(self):
        """
        Method to disconnect the SSH connection
        :return:
        """
        print(f"\nDisconnecting...")
        self.device.disconnect_from_device()

    @staticmethod
    def get_device_list():
        """
        Method to obtain list of devices, if there are multiple devices to work with
        :return:
        """
        file_path = input("\nEnter the valid file location for the device list (CSV): ")
        return readcsvfile(file_path)

    def check_version_uptime(self):
        """
        Method to connect to device and run command to obtain "show version" output
        :return: None
        """
        output = self.device.get_version()
        print(f"\nVersion Details for {self.device.cisco_device['host']}")

        # Iterate through the text by using "\n" as text separator
        for sentence in output.split("\n"):
            # Check for the sentence containing System Version
            if "system:" in sentence:
                print(sentence)
            # Check for the sentence containing Kernel Uptime
            if "uptime" in sentence:
                print(sentence)

    def check_down_interfaces(self):
        """
        Method to connect to device and run command to obtain "show interface status" output
        :return: None
        """
        output = self.device.get_interface_status()
        print(f"\nConnected interfaces in {self.device.cisco_device['host']}")
        # Iterate through the text using "\n" as text separator
        for sentence in output.split("\n"):
            if "connected" in sentence:
                print(sentence)

if __name__ == "__main__":
    header, device_list = NexusTest.get_device_list()
    user, pwd = get_credentials()
    for row in device_list:
        worker = NexusTest(row[0], user, pwd)
        worker.check_version_uptime()
        worker.check_down_interfaces()
        worker.disconnect_device()
    print("\nGoodbye...")