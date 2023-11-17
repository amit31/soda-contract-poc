from soda.contracts.data_contract_translator import DataContractTranslator
from soda.scan import Scan

class DataContractScanner:
    def __init__(self):
        self.scan = Scan()

    def read_data_contract(self, file_path):
        with open(file_path) as f:
            return f.read()

    def translate_data_contract(self, data_contract_str):
        data_contract_parser = DataContractTranslator()
        return data_contract_parser.translate_data_contract_yaml_str(data_contract_str)

    def prepare_scan(self, sodacl_str):
        self.scan.set_verbose(True)
        self.scan.set_data_source_name("vertica_local")
        self.scan.add_configuration_yaml_file(file_path="configuration/configuration.yml")
        self.scan.add_sodacl_yaml_str(sodacl_str)

    def execute_scan(self):
        result = self.scan.execute()
        return result

    def display_results(self):
        checks = self.scan.get_scan_results()['checks']
        print(f"check counts: {len(checks)}")
        for check in checks:
            status = check['outcome']
            outcomes = ''
            if status != 'pass':
                outcomes = f" with outcomes: {check['diagnostics']}"
            print(f"{check['name']} with status: {status}{outcomes}")

    def run_checks(self, data_contract_path):
        # Read data contract
        data_contract_str = self.read_data_contract(data_contract_path)

        # Translate data contract
        sodacl_str = self.translate_data_contract(data_contract_str)
        print(sodacl_str)

        #Prepare scan
        self.prepare_scan(sodacl_str)
        
        # Execute scan
        result = self.execute_scan()
        print(result)

        # Display results
        self.display_results()
