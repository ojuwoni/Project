from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _


####################################################################################
# Création d'une table permettant de renseigner toutes les informations concernant #
# le profil des utilisateurs 				                           #
#s###################################################################################
class UserProfile(models.Model):
	name		= models.CharField(max_length=50, verbose_name="Name")
	login		= models.CharField(max_length=25, verbose_name="Login")
	password	= models.CharField(max_length=100, verbose_name="Password")
	phone		= models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
	born_date	= models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
	last_connection	= models.DateField(verbose_name="date of last connection", null=True, default=None, blank=True)
	email		= models.EmailField(verbose_name="Email")
	years_seniority	= models.IntegerField(verbose_name="Seniority", default=0)
	date_created	= models.DateField(verbose_name="Date of birthday", auto_now_add=True)

	def __str__(self):
		return self.name

#####################################################################################
# Table definissant toutes les applications auxquelles l'utilisateur se connect     #
#####################################################################################
class Project(models.Model):
	title 		= models.CharField(max_length=50, verbose_name = "Title")
	description	= models.CharField(max_length=1000, verbose_name="Description")
	client_name	= models.CharField(max_length=1000, verbose_name="Client name")


###################################################################################
class Supervisor(UserProfile):
	specialisation	= models.CharField(max_length=50, verbose_name="Specialisation")

class Developer(UserProfile):
	supervisor_field	= models.ForeignKey(Supervisor, verbose_name="Supervisor", on_delete=models.CASCADE)


#####################################################################################
# Table definissant les tâches accomplies par un utilisateur                        #
#####################################################################################
class Task(models.Model):
	title		= models.CharField(max_length=50, verbose_name="Title")
	description	= models.CharField(max_length=1000, verbose_name="Description")
	time_elapsed	= models.IntegerField(verbose_name="Elapsed tiem", null=True, default=None, blank=True)
	importance	= models.IntegerField(verbose_name="Importance")
	project		= models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True, on_delete=models.CASCADE)
	developer	= models.ForeignKey(Developer, verbose_name="User", on_delete=models.CASCADE)



####################################################################################
# Création d'une table permettant de renseigner toutes les informations concernant #
#                les parents et reprise de celles des enfants                      #
####################################################################################
 
class Identity(models.Model):
 
    
	lastname = models.CharField(max_length=30, verbose_name='Nom de famille')
	firstname = models.CharField(max_length=30, verbose_name='Prénom(s)')
 
	def __str__(self):
		return '%s %s' % (self.lastname, self.firstname)


