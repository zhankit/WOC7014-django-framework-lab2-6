from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Brand(models.Model):
	name = models. CharField(max_length=100)
	origin = models.CharField(max_length=100)
	manufacturing = models.CharField(max_length=100)
	manufacturingYear = models.DateField(null=True, blank=True)
	slug = models.SlugField(unique=True,null=True)
	# prepopulated_fields = {"slug": ("name")}

	def __str__(self):
		return self.name.replace(" ", "-")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Brand, self).save(*args, **kwargs)

class Model(models.Model):
	OPERATING_SYSTEM = [
        ("AN", "Android"),
		("AP", "Apple"),
		("OT", "Other"),
    ]

	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	modelName = models. CharField(max_length=100)
	launchDate = models.DateField(null=True, blank=True)
	platform = models.CharField(max_length=100)
	operatingSystem = models.CharField(
        max_length=2,
        choices=OPERATING_SYSTEM,
    )
	slug = models.SlugField(unique=True,null=True)

	def __str__(self):
		return self.modelName

	def save(self, *args, **kwargs):
		self.slug = self.modelName.replace(" ", "-")
		super().save(*args, **kwargs)

class Review(models.Model):
	OPERATING_SYSTEM = [
        ("1", "1"),
		("2", "2"),
		("3", "3"),
		("4", "4"),
		("5", "5"),
    ]

	model = models.ManyToManyField(Model)
	description = models.CharField(null=True,max_length=400)
	review = models.CharField(
        max_length=1,
        choices=OPERATING_SYSTEM,
    )
	createdDate = models.DateField(null=True, blank=True)
	slug = models.SlugField(unique=True,null=True)

	def __str__(self):
		return self.description

	def save(self, *args, **kwargs):
		super(Review, self).save()
		self.slug = '%i-%s' % (
			self.id, slugify(self.model.name)
		)
		super().save(*args, **kwargs)