from django.test import TestCase
from tasks.models import Tasks



# Test that the model can be saved to the database.
# Test that the model can be retrieved from the database.
class TaskModelTest(TestCase):
    def test_saving_and_retrieving_tasks(self):
        first_task = Tasks()
        first_task.title = 'Go to the gym'
        first_task.description = 'Work out at 10.00 a.m'
        first_task.save()

        second_task = Tasks()
        second_task.title = 'Study Django'
        second_task.description = 'Study for 2 hours'
        second_task.save()

        saved_tasks = Tasks.objects.all()
        self.assertEqual(saved_tasks.count(), 2)

        first_saved_task = saved_tasks[0]
        second_saved_task = saved_tasks[1]
        self.assertEqual(first_saved_task.title, 'Go to the gym')
        self.assertEqual(first_saved_task.description, 'Work out at 10.00 a.m')
        self.assertEqual(second_saved_task.title, 'Study Django')
        self.assertEqual(second_saved_task.description, 'Study for 2 hours')



# Test that the model can be updated in the database.
class TasksModelTest(TestCase):
    def test_update_tasks(self):

        # create a new task
        task = Tasks.objects.create(
            title='Task 1', description='Task description')

        # update a task
        task.title = 'New Task 1'
        task.description = 'New Task description'
        task.save()

        # retrieve the task from database
        updated_task = Tasks.objects.get(pk=task.pk)
        self.assertEqual(updated_task.title, 'New Task 1')
        self.assertEqual(updated_task.description, 'New Task description')


#Test that the model can be deleted from the database.
class TasksModelDeleteTestCase(TestCase):
    def test_delete_task(self):
        task = Tasks.objects.create(
            title="New Task", description="New Task description")
        task.delete()
        self.assertEqual(Tasks.objects.count(), 0)
