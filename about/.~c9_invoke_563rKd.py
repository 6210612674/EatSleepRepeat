from django.test import TestCase

# Create your tests here.

def test_about_view_page(self):
    reg = Reg.objects.get(course_code='CN210')
    c = Client()
    response = c.get(reverse('regs:index'))
    self.assertEqual(response.status_code, 200)