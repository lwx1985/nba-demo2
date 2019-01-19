# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Games(models.Model):
    home = models.CharField(max_length=255, blank=True, null=True)
    away = models.CharField(max_length=255, blank=True, null=True)
    h_score = models.IntegerField(blank=True, null=True)
    a_score = models.IntegerField(blank=True, null=True)
    h_1 = models.IntegerField(blank=True, null=True)
    h_2 = models.IntegerField(blank=True, null=True)
    h_3 = models.IntegerField(blank=True, null=True)
    h_4 = models.IntegerField(blank=True, null=True)
    a_1 = models.IntegerField(blank=True, null=True)
    a_2 = models.IntegerField(blank=True, null=True)
    a_3 = models.IntegerField(blank=True, null=True)
    a_4 = models.IntegerField(blank=True, null=True)
    h_ass = models.IntegerField(blank=True, null=True)
    h_reb = models.IntegerField(blank=True, null=True)
    h_stl = models.IntegerField(blank=True, null=True)
    h_blk = models.IntegerField(blank=True, null=True)
    h_tov = models.IntegerField(blank=True, null=True)
    h_fou = models.IntegerField(blank=True, null=True)
    a_ass = models.IntegerField(blank=True, null=True)
    a_reb = models.IntegerField(blank=True, null=True)
    a_stl = models.IntegerField(blank=True, null=True)
    a_blk = models.IntegerField(blank=True, null=True)
    a_tov = models.IntegerField(blank=True, null=True)
    a_fou = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class League(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    psg = models.FloatField(blank=True, null=True)
    trb = models.FloatField(blank=True, null=True)
    ast = models.FloatField(blank=True, null=True)
    stl = models.FloatField(blank=True, null=True)
    blk = models.FloatField(blank=True, null=True)
    ftp = models.FloatField(blank=True, null=True)
    fg = models.FloatField(blank=True, null=True)
    a_3pp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'league'


class Pos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pos'


class Season2017(models.Model):
    player = models.CharField(db_column='Player', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='Pos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='Tm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    mp = models.FloatField(db_column='MP', blank=True, null=True)  # Field name made lowercase.
    fgp = models.FloatField(db_column='FGP', blank=True, null=True)  # Field name made lowercase.
    fga = models.FloatField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    number_3p = models.FloatField(db_column='3P', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3pa = models.FloatField(db_column='3PA', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3pp = models.FloatField(db_column='3PP', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2p = models.FloatField(db_column='2P', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2pa = models.FloatField(db_column='2PA', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2pp = models.FloatField(db_column='2PP', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    efgp = models.FloatField(db_column='eFGP', blank=True, null=True)  # Field name made lowercase.
    ft = models.FloatField(db_column='FT', blank=True, null=True)  # Field name made lowercase.
    fta = models.FloatField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    ftp = models.FloatField(db_column='FTP', blank=True, null=True)  # Field name made lowercase.
    orb = models.FloatField(db_column='ORB', blank=True, null=True)  # Field name made lowercase.
    drb = models.FloatField(db_column='DRB', blank=True, null=True)  # Field name made lowercase.
    trb = models.FloatField(db_column='TRB', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    stl = models.FloatField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    blk = models.FloatField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    tov = models.FloatField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    psg = models.FloatField(db_column='PSG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'season2017'


class Teams(models.Model):
    name = models.CharField(db_column='Name', max_length=3)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coach = models.CharField(db_column='Coach', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gymnasium = models.CharField(db_column='Gymnasium', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field_region = models.CharField(db_column='\r\nRegion', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    chinesename = models.CharField(db_column='ChineseName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    win = models.IntegerField(blank=True, null=True)
    lose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


class Userinfo(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    sex = models.CharField(max_length=4, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    pics = models.CharField(max_length=200, blank=True, null=True)
    group = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'
