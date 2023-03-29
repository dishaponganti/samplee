import src.database_functions as db
import pytest
import datetime


def test_database_connect_success():
	db_inst = db.DatabaseObjects()
	res = db_inst.database_connect()
	assert res[0] == datetime.datetime.now().date()


@pytest.mark.xfail
def test_database_connect_failure():
	with pytest.raises(Exception) as e_info:
		db_inst = db.DatabaseObjects()
		res = db_inst.database_connect()


def test_database_query_success(test_sample_organization_data):
	db_inst = db.DatabaseObjects()
	res = db_inst.database_query(test_sample_organization_data[0])
	assert res[0][0] == test_sample_organization_data[1]


@pytest.mark.xfail
def test_database_query_failure(test_sample_organization_data):
	with pytest.raises(Exception) as e_info:
		db_inst = db.DatabaseObjects()
		res = db_inst.database_query(test_sample_organization_data[0])


def test_get_person_success(test_sample_person_data):
	db_inst = db.DatabaseObjects()
	res = db_inst.get_person(test_sample_person_data[0])
	# assert res[0][0] == test_sample_person_data[1]
	assert res.empty


@pytest.mark.xfail
def test_get_person_failure(test_sample_person_data):
	with pytest.raises(Exception) as e_info:
		db_inst = db.DatabaseObjects()
		res = db_inst.get_person(test_sample_person_data[0])
