from system.core.model import Model

class Course(Model):
	def __init__(self):
		super(Course, self).__init__()

	def add_course(self, course_details):
		insert_query = "INSERT INTO courses (name, description, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(course_details['name'], course_details['description'])
		return self.db.query_db(insert_query)

	def get_all_courses(self):
		get_all_query = "SELECT * FROM courses"
		return self.db.query_db(get_all_query)

	def get_course_by_id(self, course_id):
		get_one_query = "SELECT * FROM courses WHERE id = {}".format(course_id)
		return self.db.query_db(get_one_query)

	def destroy(self, id):
		delete_one_query = "DELETE FROM courses WHERE id = {}".format(id)
		return self.db.query_db(delete_one_query)