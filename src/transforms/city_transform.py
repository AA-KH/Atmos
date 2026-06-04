from src.validators.data_validator import validate_city

def transform_city(city_data):
    validated = validate_city(city_data)
    
    if not validated:
        return None
    
    return validated.model_dump()