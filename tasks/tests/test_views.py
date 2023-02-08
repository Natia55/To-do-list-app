from django.test import Client, TestCase
from tasks.models import Tasks
from django.urls import reverse
from tasks.views import list_tasks


# Test that the view returns a status code of 200.
class ListViewTest(TestCase):
    def test_list_tasks_status_code(self):
        client = Client()
        response = client.get(reverse('list_tasks'))
        self.assertEqual(response.status_code, 200)


# Test that the view returns a queryset of all the objects.
class ListViewQueryTest(TestCase):

    def create(self):
        Tasks.objects.create(title='Task 1', description='This is task 1')
        Tasks.objects.create(title='Task 2', description='This is task 2')

    def test_list_tasks(self):
        response = self.client.get(reverse('list_tasks'))
        tasks = response.context['tasks']
        self.assertEqual(tasks.count(), 2)
        self.assertEqual(tasks[0].title, 'Task 1')
        self.assertEqual(tasks[1].title, 'Task 2')


# Test that the view returns the correct template.
class ListViewTemplate(TestCase):
    def test_list_tasks_template(self):
        client = Client()
        response = client.get(reverse('list_tasks'))
        self.assertTemplateUsed(response, 'tasks/task_list.html')


# Test that the view returns a status code of 200.
class UpdateTasksView(TestCase):
    def create(self):
        self.client = Client()
        self.task = Tasks.objects.create(
            title='My Task', description='This is a task description.')

    def test_update_tasks_view(self):
        response = self.client.get(
            reverse('update_tasks', args=(self.task.pk,)))
        self.assertEqual(response.status_code, 200)


# Test that the view updates the object correctly.
class UpdateTasksViewObj(TestCase):
    def create(self):
        self.client = Client()
        self.task = Tasks.objects.create(
            title='My Task', description='This is a task description.')

    def test_update_tasks_view(self):
        data = {'title': 'Updated Task',
                'description': 'This is an updated task description.'}
        response = self.client.post(
            reverse('update_tasks', args=(self.task.pk,)), data=data)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.description,
                         'This is an updated task description.')

# Test that the view returns the correct template.


class UpdateTasksViewTemplate(TestCase):
    def create(self):
        self.client = Client()
        self.task = Tasks.objects.create(
            title="New Task", description='New Task description')

    def test_template(self):
        response = self.client.get(
            reverse('update_tasks', args=(self.task.pk,)))
        self.assertTemplateUsed(response, 'tasks/update_tasks.html')


# Test that the view returns a status code of 302 (redirect).
class DeleteTasksViewTestCase(TestCase):
    def create(self):
        self.client = Client()
        self.task = Tasks.objects.create(
            title='New Test', description='New Task Description')

    def test_delete_tasks_view(self):
        self.create()
        response = self.client.post(
            reverse('delete_tasks', args=(self.task.pk,)))
        self.task.delete()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

        # Test that the view deletes the object correctly.
        task = Tasks.objects.filter(pk=self.task.pk)
        self.assertFalse(task.exists())
