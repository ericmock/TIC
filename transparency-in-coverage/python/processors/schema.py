SCHEMA = {
    'root':[
        'root_hash_id',
        'reporting_entity_name',
        'reporting_entity_type',
        'plan_name',
        'plan_id',
        'plan_id_type',
        'plan_market_type',
        'last_updated_on',
        'version',
        'url',],

    'in_network':[
        'root_hash_id',
        'in_network_hash_id',
        'negotiation_arrangement', 
        'name',
        'billing_code_type_version', 
        'description', 
        'billing_code', 
        'billing_code_type',
        ],

    'covered_services':[
        'root_hash_id',
        'in_network_hash_id',
        'billing_code_type_version', 
        'description', 
        'billing_code', 
        'billing_code_type',
        'covered_services_hash_id',
    ],

    'bundled_codes':[
        'root_hash_id',
        'in_network_hash_id',
        'bundled_codes_hash_id',
        'billing_code_type_version', 
        'description', 
        'billing_code', 
        'billing_code_type',
    ],

    'negotiated_rates':[
        'root_hash_id',
        'in_network_hash_id',
        'negotiated_rates_hash_id',
        ],

    'negotiated_prices':[
        'root_hash_id',
        'in_network_hash_id',
        'negotiated_rates_hash_id',
        'billing_class',
        'negotiated_type', 
        'service_code', 
        'expiration_date',         
        'additional_information',
        'billing_code_modifier',
        'negotiated_rate',
        ],

    'provider_groups':[
        'root_hash_id',
        'in_network_hash_id',
        'negotiated_rates_hash_id',
        'tin_type',
        'tin_value',
        'npi_numbers',
        ],
}