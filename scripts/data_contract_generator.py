import yaml
import re

def generate_data_contract(column_info):
    data_contract = {
        'dataset': column_info['table_name'],
        'columns': [],
    }

    for column in column_info['columns']:
        column_name, data_type, is_nullable = column
        column_data = {
            'name': column_name,
            'data_type': re.sub(r'(varchar|char)\s*\(\s*\d+\s*\)', lambda match: match.group(1).capitalize(), data_type),
            'not_null': not is_nullable
        }

        data_contract['columns'].append(column_data)

    return yaml.dump(data_contract, default_flow_style=False)
