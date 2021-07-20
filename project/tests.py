from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Projects,Rating,UserProfile

        
class CategoryTest(TestCase):

    def setUp(self):
        self.html = Category(name='Music')

    def test_instance(self):
        self.assertTrue(isinstance(self.html,Category))

    def test_save(self):
        self.html.save_category()
        categoriess = Category.objects.all()
        self.assertTrue(len(categoriess) > 0)

    def test_delete(self):
        self.html.save_category()
        self.html.delete_category()
        categoriess = Category.objects.all()
        self.assertTrue(len(categoriess) == 0)



class ProjectsTest(TestCase):

    def setUp(self):
        # Creating a new editor and saving it

        self.html = Projects(description = 'Music')
        self.html.save_project()

        # Creating a new tag and saving it
        self.new_project = Category(name = 'testing')
        self.new_project.save()

        self.new_project = Projects(description = 'This is a random test project', image='', category = self.html)
        self.new_project.save()
        self.new_project.category.add(self.new_project)

    def tearDown(self):

        Category.objects.all().delete()
        Projects.objects.all().delete()


class RatingTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1,username='Mwangi')
        self.user.save()
        self.user_profile = UserProfile(user=self.user,image="pic.png",bio=" bio")
        self.new_project = Projects(id=1,name="project",image="",description=" project1",user=self.user_profile )
        self.new_project.save()
        self.project_rating = Rating(id=1,design=7,usability=8,content=9,user=self.user_profile,project=self.new_project)
   
    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        Projects.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.project_rating,Rating))
    
    def test_save_rating(self):
        self.project_rating.save_rating()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)>0)
        
    def test_delete_rating(self):
        self.project_rating.save_rating()
        self.project_rating.delete_rating()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)==0)
        
    # def test_get_project_rating(self):
    #     id=1
    #     self.project_rating.get_project_rating(id)
    #     self.assertEquals(self.project_rating.id,1)
        
