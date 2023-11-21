from soda.scan import Scan # importing the Soda library

scan = Scan() # loading the function
scan.set_data_source_name("vertica_local") # initialising the datasource name

# Loading the configuration file
scan.add_configuration_yaml_file(
    file_path="/Users/amit.sharma/PycharmProjects/sodadatacontract/soda-contract-poc/configuration/configuration.yml"
)
# Adding scan date variable to label the scan date
scan.add_variables({"date": "2023-04-11"})

# Loading the check yaml file
scan.add_sodacl_yaml_file("/Users/amit.sharma/PycharmProjects/sodadatacontract/soda-contract-poc/configuration/freshness.yml")

# Executing the scan
scan.execute()

# Setting logs to verbose mode
scan.set_verbose(True)

# Inspect the scan result
result=scan.get_scan_results()
scan.assert_no_checks_fail()
print(result)