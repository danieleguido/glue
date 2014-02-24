from django.db import models


class FakeTag(models.Model):
  '''
  Fake tag class, for testing m2m purposes only.
  '''
  content = models.CharField(max_length=32)
  
  def json(deep=False):
    d = {
      'pk': self.pk,
      'content' : self.content
    }



class Fake(models.Model):
  '''
  Fake item class, for test purposes only.
  '''
  name = models.CharField(max_length=32)
  date_created = models.DateTimeField(auto_now=True)

  tags = models.ManyToManyField(FakeTag, related_name="%(app_label)s_%(class)s_related")

  class Meta:
    abstract = True


  def json(deep=False):
    d = {
      'pk': self.pk,
      'name' : self.name,
      'date_created': self.date_created.isoformat(),
    }
    if(deep):
      d.update({
        'tags': [t.json for t in tags]
      })
    return d