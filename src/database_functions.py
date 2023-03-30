""" This module covers all the database functions like connecting and quering on the Synthea ETL data from postgres
database"""
import traceback
import psycopg2
import pandas as pd
import os


class DatabaseObjects:
	"""DatabaseObjects class has a class instance conn which can be used without creating multiple instances
	and to call the functions. It is initialized to None.
	The class functions include database_connect, database_query and get_person."""

	def __init__(self):
		self.host = os.environ.get('host')
		self.database = os.environ.get('database')
		self.username = os.environ.get('username')
		self.password = os.environ.get('password')
		self.conn = None

	def database_connect(self):
		"""
		This function takes 4 parameters, namely, username, password, host and database name for
		connecting to the postgres Synthea database and returns the database version as a
		successful connection sign.
		:param user: postgres username
		:param password: password for the given username
		:param host: host name where the database is hosted
		:param database: postgres database name
		:return: Current date
		"""
		try:
			self.conn = psycopg2.connect(
				host=self.host,
				database=self.database,
				user=self.username,
				password=self.password)
			cur = self.conn.cursor()
			cur.execute('SELECT CURRENT_DATE ;')
			db_version = cur.fetchone()
			return db_version
			cur.close()
		except Exception:
			print("Caught exception", traceback.format_exc())
			cur.close()

	def database_query(self, query):
		"""
		This function takes a query as a parameter and returns the query results in a pandas
		DataFrame format.
		:param query: SQL query to be executed on the database.
		:return Return the query results as a dataframe
		"""
		try:
			if not self.conn:
				self.conn = psycopg2.connect(
					host=self.host,
					database=self.database,
					user=self.username,
					password=self.password)

			cur = self.conn.cursor()
			cur.execute(query)
			results = cur.fetchall()
			cur.close()
			df = pd.DataFrame(results)
			return df
		except Exception:
			print("Caught exception", traceback.format_exc())
			cur.close()

	def get_person(self, ids):
		"""
		This function takes a list of person ids as a parameter, executes the query on the person
		table and returns the results in dataframe format.
		:param ids:
		:return:
		"""
		try:
			if not self.conn:
				self.conn = psycopg2.connect(
					host=self.host,
					database=self.database,
					user=self.username,
					password=self.password)

			cur = self.conn.cursor()
			all_ids = '(' + ', '.join(f"'{i}'" for i in ids) + ')'
			cur.execute(f'select * from cdm_synthea10.person where person_id in {all_ids}')
			results = cur.fetchall()
			cur.close()
			df = pd.DataFrame(results)
			return df
		except Exception:
			print("Caught exception", traceback.format_exc())
			cur.close()

