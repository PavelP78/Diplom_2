from faker import Faker


fake = Faker('ru_RU')


def generate_user():
	email = fake.email(),
	password = fake.password(),
	name = fake.first_name()
	return {
		"email": email,
		"password": password,
		"name": name
	}


def generate_user_email():
	email = fake.email()
	return {
		"email": email
	}


def generate_user_password():
	password = fake.password()
	return {
		"password": password
	}


def generate_user_name():
	name = fake.first_name()
	return {
		"name": name
	}


def generate_user_without_email():
	password = fake.password(),
	name = fake.first_name()
	return {
		"password": password,
		"name": name
	}


def generate_user_without_password():
	email = fake.email(),
	name = fake.first_name()
	return {
		"email": email,
		"name": name
	}


def generate_user_without_name():
	email = fake.email(),
	password = fake.password(),
	return {
		"email": email,
		"password": password
	}
