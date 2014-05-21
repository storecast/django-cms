
from south.db import db
from django.db import models
from cms.plugins.snippet.models import *
from django.contrib.sites.models import Site

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Snippet.site'
        db.add_column('snippet_snippet', 'site', models.fields.related.ForeignKey(Site))     
    
    
    def backwards(self, orm):
        
        # Deleting field 'Snippet.site'
        db.delete_column('snippet_snippet', 'site')
        
        
    
    
        models = {
            'cms.cmsplugin': {
                'Meta': {'object_name': 'CMSPlugin'},
                'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'language': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
                'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
                'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cms.Placeholder']"}),
                'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
                'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
                'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'blank': 'True', 'default': 'True'}),
                'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
                'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True', 'default': '0'}),
                'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
                'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
            },
            'cms.placeholder': {
                'Meta': {'object_name': 'Placeholder'},
                'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'layout_level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
                'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
            },
            'sites.site': {
                'Meta': {'db_table': "'django_site'", 'object_name': 'Site'},
                'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
            },
            'snippet.snippet': {
                'Meta': {'object_name': 'Snippet'},
                'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
                'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
                'template': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
            },
            'snippet.snippetptr': {
                'Meta': {'_ormbases': ['cms.CMSPlugin'], 'db_table': "'cmsplugin_snippetptr'", 'object_name': 'SnippetPtr'},
                'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['cms.CMSPlugin']", 'primary_key': 'True'}),
                'snippet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['snippet.Snippet']"})
            }
        }

        complete_apps = ['snippet']

