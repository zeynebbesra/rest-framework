from rest_framework import serializers
from .models import Person, Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model=Job
        fields = ['job_name']

class PersonSerializer(serializers.ModelSerializer):
    job = JobSerializer()   #Burada foreign key'i serileştirmiş olduk.
    job_info = serializers.SerializerMethodField()
    class Meta:
        model=Person
        fields='__all__'
        #depth = 1  # Bu ise foreign key'nin sahip olduğu her özelliği gösterir.

    def get_job_info(self, obj):
        job_obj = Job.objects.get(id = obj.job.id)

        return {'job_name': job_obj.job_name, 'place':'Trabzon'}
    
    def validate(self, data):
        special_characters="!@#$%^&*()-+/?=,<>"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('name cannot contain special chars')

        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        return data