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
def test_sample_query():
	"""
	Sample record from cdm_synthea10.person table
	:return: List of [person_id, gender_concept_id]
	"""
	per_id = "324"
	gender_concept_id = 8532
	return [f"select distinct gender_concept_id from cdm_synthea10.person where person_id='{per_id}';", gender_concept_id]


@pytest.fixture
def test_sample_person_data():
	"""
	Sample record from native.observations table
	:return: List of [person id, person id]
	"""
	return [["43"], 43]

