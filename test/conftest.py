import pytest
import os


@pytest.fixture
def database_creds():
	"""
	Read the database connection credentials from environment variables
	and return them.
	"""
	host = os.environ.get('host')
	database = os.environ.get('database')
	username = os.environ.get('username')
	password = os.environ.get('password')
	return {'username':username, 'password':password, 'host':host, 'database':database}


@pytest.fixture
def test_sample_organization_data():
	"""
	Sample record from native.organizations table
	:return: List of [organization id, organization name]
	"""
	org_id = "43e22208-dae0-3196-b30b-17b3c50679c2"
	org_name = "GREATER LAWRENCE FAMILY HEALTH CENTER INC"
	return [f"select distinct name from native.organizations where id='{org_id}';", org_name]


@pytest.fixture
def test_sample_person_data():
	"""
	Sample record from cdm_synthea10.person table
	:return: List of [person id, person id]
	"""
	return [["43"], ""]


