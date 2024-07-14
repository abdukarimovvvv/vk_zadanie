import json
import os

import jsonschema
from jsonschema import Draft7Validator


def validate_json_schema(schema):
	try:
		Draft7Validator.check_schema(schema)
		print("JSON Schema is valid.")
		return True
	except jsonschema.exceptions.SchemaError as e:
		print(f"JSON Schema is invalid: {str(e)}")
		return False


def generate_pydantic_model(schema, output_dir):
	kind = schema.get('properties', {}).get('kind', {}).get('const', 'BaseModel')
	with open(os.path.join(output_dir, f"{kind.lower()}_model.py"), 'w') as f:
		f.write("from pydantic import BaseModel\n\n")
		f.write(f"class {kind.capitalize()}Model(BaseModel):\n")
		for prop, details in schema.get('properties', {}).items():
			prop_type = details.get('type', 'Any')
			f.write(f"    {prop}: {prop_type} = None\n")


def generate_fastapi_controller(kind, output_dir):
	with open(os.path.join(output_dir, f"{kind.lower()}_controller.py"), 'w') as f:
		f.write("from fastapi import APIRouter, HTTPException, Depends\n")
		f.write("from sqlalchemy.orm import Session\n")
		f.write(f"from ..models.{kind.lower()}_model import {kind.capitalize()}Model\n")
		f.write("from ..database import get_db\n\n")
		f.write(f"router = APIRouter()\n\n")
		
		# POST endpoint
		f.write(f"@router.post('/{kind.lower()}/')\n")
		f.write(f"async def create_{kind.lower()}(item: {kind.capitalize()}Model, db: Session = Depends(get_db)):\n")
		f.write(f"    # TODO: Implement creation logic\n")
		f.write(f"    return {{'message': '{kind} created'}}\n\n")
		
		# GET endpoint
		f.write(f"@router.get('/{kind.lower()}/{{uuid}}')\n")
		f.write(f"async def get_{kind.lower()}(uuid: str, db: Session = Depends(get_db)):\n")
		f.write(f"    # TODO: Implement retrieval logic\n")
		f.write(f"    return {{'message': '{kind} retrieved'}}\n\n")
		
		# PUT endpoints
		f.write(f"@router.put('/{kind.lower()}/{{uuid}}/configuration')\n")
		f.write(f"async def update_configuration(uuid: str, configuration: dict, db: Session = Depends(get_db)):\n")
		f.write(f"    # TODO: Implement update logic\n")
		f.write(f"    return {{'message': 'Configuration updated'}}\n\n")
		
		f.write(f"@router.put('/{kind.lower()}/{{uuid}}/settings')\n")
		f.write(f"async def update_settings(uuid: str, settings: dict, db: Session = Depends(get_db)):\n")
		f.write(f"    # TODO: Implement update logic\n")
		f.write(f"    return {{'message': 'Settings updated'}}\n\n")
		
		f.write(f"@router.put('/{kind.lower()}/{{uuid}}/state')\n")
		f.write(f"async def update_state(uuid: str, state: str, db: Session = Depends(get_db)):\n")
		f.write(f"    # TODO: Implement update logic\n")
		f.write(f"    return {{'message': 'State updated'}}\n\n")
		
		# DELETE endpoint
		f.write(f"@router.delete('/{kind.lower()}/{{uuid}}')\n")
		f.write(f"async def delete_{kind.lower()}(uuid: str, db: Session = Depends(get_db)):\n")
		f.write(f"    # TODO: Implement deletion logic\n")
		f.write(f"    return {{'message': '{kind} deleted'}}\n\n")


if __name__ == "__main__":
	schema_path = input("Enter JSON schema path: ")
	output_dir = input("Enter output directory: ")
	
	with open(schema_path, 'r') as f:
		schema = json.load(f)
	
	if validate_json_schema(schema):
		os.makedirs(output_dir, exist_ok=True)
		generate_pydantic_model(schema, output_dir)
		kind = schema.get('properties', {}).get('kind', {}).get('const', 'base')
		generate_fastapi_controller(kind, output_dir)
		print("Generation completed.")
	else:
		print("Generation failed due to invalid schema.")
		