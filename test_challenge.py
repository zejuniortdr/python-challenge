import csv
from pathlib import Path

from tree import Tree

################################
# SE O ENV EXISTE
################################

def env_exist():
	env = Path("flask")
	if env.is_dir():
		return True
	return False

def test_env_exist():
	assert env_exist() == True

################################
# SE O ARQUIVO EXISTE
################################

def file_exist():

	patients_list = Path("patients.csv")
	if patients_list.is_file():
		return True
	return False

def test_file_exist():
	assert file_exist() == True

################################
# SE O ARQUIVO PODE SER LIDO
################################

def count_patients():

	with open('patients.csv', 'r+') as csvfile:
		content = csv.reader(csvfile, delimiter=';')
		row_count = sum(1 for row in content)

	return row_count

def test_count_patients():
	assert count_patients() > 0

################################
# SE A ARVORE PODE SER MONTADA
################################
def loaddata():
	T = Tree()
	with open('patients.csv', 'r+') as csvfile:
		content = csv.reader(csvfile, delimiter=';')
		for row in content:
			T.insert(row[0])
	return T


def test_loaddata():
	T = loaddata()
	assert isinstance(T, Tree)


################################
# SE PODE SER FEITO UMA BUSCA
################################
def search(T):
	search_for = str('Mar').lower()
	results = T.search(search_for)
	return (results)

def test_search():
	T = loaddata()
	assert len(search(T)) >= 0

def search_with_no_q(T):
	results = T.search(None)
	return (results)

def test_search_with_no_q():
	T = loaddata()
	assert len(search_with_no_q(T)) >= 0

def search_with_no_q_and_limit(T):
	results = T.search(None,3)
	return (results)

def test_search_with_no_q_and_limit():
	T = loaddata()
	assert len(search_with_no_q_and_limit(T)) >= 0


def search_with_q_and_limit(T):
	search_for = str('Mar').lower()
	results = T.search(search_for,3)
	return (results)

def test_search_with_q_and_limit():
	T = loaddata()
	assert len(search_with_q_and_limit(T)) >= 0

