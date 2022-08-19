from netmiko import ConnectHandler


class NetworkDevice:
    """
    Class to define network device types and parameters

    Methods are purely to cater to command sending and not formatting the command outputs received.
    Methods will return output from CLI to the method call.
    """
    def __init__(self, device_type, hostname, username, password):
        """
        Method to instantiate the device type and params
        :param hostname [str]: IP/Hostname
        :param username [str]: Username to login
        :param password [str]: Password to login
        """

        # Make sure to use the key names exactly as the ConnectHandler function definition arguments
        self.cisco_device = {
            "device_type": device_type,
            "host": hostname,
            "username": username,
            "password": password
        }

        # Establish SSH connection to device
        self.connection = ConnectHandler(**self.cisco_device)

    def disconnect_from_device(self):
        """
        Method to disconnect SSH from device
        :return:
        """
        self.connection.disconnect()

    def get_version(self):
        """
        Method to obtain "show version" command output for device

        NOTE: NO OUTPUT FORMATTING IS DONE IN THIS METHOD

        :return: Command output [str]
        """
        command = "show version\n"
        return self.connection.send_command(command)

    def get_interface_status(self):
        """
        Method to obtain "show interface status" command output

        NOTE: NO OUTPUT FORMATTING IS DONE IN THIS METHOD

        :return: Command output [str]
        """
        command = "show interface status\n"
        return self.connection.send_command(command)



