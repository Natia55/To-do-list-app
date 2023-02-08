
from tasks.forms import TasksForm
from django.test import TestCase


#Test that the form is valid with correct data.
class TasksFormTestCase(TestCase):
    def test_form_correct_data(self):
        data = {'title': 'New Task', 'description': 'New task description'}
        form = TasksForm(data=data)
        self.assertTrue(form.is_valid())


#Test that the form is invalid with incorrect data.
    def test_form_invalid_data(self):
        data = {'title': '', 'description': 'New task description'}
        form = TasksForm(data=data)
        self.assertFalse(form.is_valid())
