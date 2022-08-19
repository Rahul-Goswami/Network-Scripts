import xlrd


class VPCConfigCheck:
    """
    Method to get network work plan parameters for a server

    Arguments: None

    Returns: None
    """
    @staticmethod
    def vpc_config_check(data):

        server = input("\nEnter the server name to validate vPC plan for: ")

        # Iterate through the rows in the Excel file
        rows_count = data.nrows
        print(f"\nNumber of Server Entries: {rows_count-1}")
        # print(data.cell_value(1, 15))
        # print(data.cell_value(1, 23))
        server_exist_flag = False
        for rows in range(1, rows_count):
            # print(f"Data Type for ever row entry of Excel: {type(data.row_values(rows))}")
            # print(f"Value of every row entry of Excel: {data.row_values(rows)}")
            if data.cell_value(rows, 0) == server:  # Check for particular server entry
                server_exist_flag = True
                print(f"\nFetching details for {data.cell_value(rows, 0)} -> {data.cell_value(rows, 1)}")
                # Checking conditions
                if data.cell_value(rows, 2) == data.cell_value(rows, 4):  # Condition to check IP between Check Network and Pre-Checks
                    if str(int(data.cell_value(rows, 3))) == data.cell_value(rows, 14) and str(int(data.cell_value(rows, 3))) == data.cell_value(rows, 22):  # Condition to check Speed of interface
                        if data.cell_value(rows, 5) == data.cell_value(rows, 9) and data.cell_value(rows, 5) == data.cell_value(rows, 17):  # Condition to check Switch name
                            if data.cell_value(rows, 6) == data.cell_value(rows, 10) and data.cell_value(rows, 6) == data.cell_value(rows, 18):  # Condition to check Interface
                                if data.cell_value(rows, 7) == data.cell_value(rows, 11) and data.cell_value(rows, 7) == data.cell_value(rows, 19):  # Condition to check Tenant
                                    if data.cell_value(rows, 8) == data.cell_value(rows, 12) and data.cell_value(rows, 8 == data.cell_value(rows, 20)):  # Condition to check EPG
                                        if data.cell_value(rows, 13) == data.cell_value(rows, 21):  # Condition to check prod/backup network
                                            if data.cell_value(rows, 15) == 1 and data.cell_value(rows, 23) == 0:  # Condition to check vPC status
                                                if data.cell_value(rows, 16) == "untagged" and data.cell_value(rows, 24) == "untagged":  # Condition to check Trunk mode
                                                    print(f"\nvPC validation is successful {data.cell_value(rows, 0)} -> {data.cell_value(rows, 1)}")
                                                else:
                                                    print(f"\nPlease re-check Trunk mode for {data.cell_value(rows, 0)}")
                                            else:
                                                print(f"\nPlease re-check vPC status for {data.cell_value(rows, 0)}")
                                        else:
                                            print(f"\nPlease re-check PROD/BACKUP network for {data.cell_value(rows, 0)}")
                                    else:
                                        print(f"\nPlease re-check EPG name for {data.cell_value(rows, 0)}")
                                else:
                                    print(f"\nPlease re-check Tenant name for {data.cell_value(rows, 0)}")
                            else:
                                print(f"\nPlease re-check Interface number for {data.cell_value(rows, 0)}")
                        else:
                            print(f"\nPlease re-check Switch name for {data.cell_value(rows, 0)}")
                    else:
                        print(f"\nPlease re-check Interface Speed for {data.cell_value(rows, 0)}")
                else:
                    print(f"\nPlease re-check IP used to get pre-checks output with IP provided in Check Network for {data.cell_value(rows, 0)}")

        # Check the server flag to confirm if the server entered by user does not exist
        if not server_exist_flag:
            print("\nThe server name you entered does not exist in the excel file...")


# Main function for script execution
if __name__ == "__main__":
    print("\nWelcome :-D")

    # Get user input for excel file location
    file_loc = input("\nEnter file name: ")

    # Open the excel file (MUST BE ".XLS") entered by user
    xlfile = xlrd.open_workbook(file_loc)
    # Read first sheet in workbook
    sheet_data = xlfile.sheet_by_index(0)

    # Loop to keep script running for multiple uses from same excel file input
    flag = "y"
    while flag == "y" or flag == "Y":
        VPCConfigCheck.vpc_config_check(sheet_data)
        flag = input("\nDo you want to continue (y/Y) (Press any key to exit): ")
    print("\nExiting script...")
