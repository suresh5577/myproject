from django.conf import settings
def saveall(inst):
	[inst.save(using=db) for db in settings.DATABASES.keys()]